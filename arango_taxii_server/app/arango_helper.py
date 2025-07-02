import json
import logging
import os
import random
import re
import subprocess
from urllib.parse import urljoin, urlparse
from datetime import datetime
from .settings import arango_taxii_server_settings
import requests

from .. import conf

COLLECTION_INFO_RE = re.compile(r"(\w+)_(vertex|edge)_collection")
DB_NAME_RE = re.compile(r"(\w+)_database")


class ArangoFullPermissionParser:
    permissions_map = {
        "rw": (True, True),
        "ro": (True, False),
        "none": (False, False),
        "undefined": None,
    }

    @classmethod
    def get_permission(cls, permissions, db_name, collection):
        server_default = permissions.get("*", {}).get("permission")
        db_permission = permissions[db_name]["permission"]
        collection_default = permissions[db_name]["collections"]["*"]
        actual_permission = permissions[db_name]["collections"][collection]
        if actual_permission != "undefined":
            return cls.parse_permission(actual_permission)
        for default_permission in ["rw", "ro", "none", "undefined"]:
            if default_permission in [
                server_default,
                collection_default,
                db_permission,
            ]:
                return cls.parse_permission(default_permission)

    @classmethod
    def parse_permission(cls, value):
        p = (False, False)

        if isinstance(value, str):
            p = cls.permissions_map[value]
        elif isinstance(value, dict):
            p = cls.parse_permission(value["permission"])
        can_read, can_write = p
        if not arango_taxii_server_settings.SUPPORT_WRITE_OPERATIONS:
            can_write = False
        return can_read, can_write


class ArangoSession:
    HOST_URL = arango_taxii_server_settings.ARANGODB_HOST_URL

    def __init__(self, username, password, visible_to_ref=None) -> None:
        self.session = requests.Session()
        self.session.auth = username, password
        self.user, self.password = (self.session.auth)
        self.visible_to_ref = visible_to_ref

    def make_request(self, method, url, **kwargs):
        try:
            response = self.session.request(method, url, **kwargs)
            resp = ArangoResponse(response)
            if resp.error:
                raise resp.error
            return resp
        except ArangoError:
            raise
        except Exception as e:
            logging.exception(e)
            raise ArangoError(400, "arangodb could not process request")

    def is_authorized(self, db_name=None):
        try:
            return self.verify_auth(db_name)
        except:
            return False

    def verify_auth(self, db_name=None):
        if db_name:
            can_read, can_write = self.get_database(db_name)
            return can_read or can_write
        else:
            self.get_databases()
        return True

    def get_permissions(self, db_name=None):
        url = urljoin(self.HOST_URL, f"/_api/user/{self.user}/database")
        resp = self.make_request("GET", url, params=dict(full=1))
        retval = resp.result
        return retval

    def get_collection_permission(self, db_name, collection):
        url = urljoin(
            self.HOST_URL, f"/_api/user/{self.user}/database/{db_name}/{collection}"
        )
        resp = self.make_request('GET', url, params=dict(full=1))
        retval = resp.result
        return ArangoFullPermissionParser.parse_permission(retval)

    def get_databases(self):
        url = urljoin(self.HOST_URL, f"/_api/user/{self.user}/database")
        resp = self.make_request('GET', url)
        return list(resp.result.keys())

    def get_database(self, db_name):
        url = urljoin(
            self.HOST_URL, f"/_db/{db_name}/_api/user/{self.user}/database/{db_name}"
        )
        resp = self.make_request('GET', url)
        return self.parse_permission(resp.result)

    def get_collections(self, db_name):
        url = urljoin(self.HOST_URL, f"/_db/{db_name}/_api/collection")
        resp = self.make_request('GET', url)
        permissions = self.get_permissions()
        collections = {}
        collection_set = {c["name"] for c in resp.result}
        for c in resp.result:
            if c["isSystem"]:
                continue
            title, _ = self.split_collection_info(c["name"])

            if  not collection_set.issuperset([f"{title}_vertex_collection", f"{title}_edge_collection"]):
                continue
            if title in collections:
                continue
            can_read, can_write = ArangoFullPermissionParser.get_permission(
                permissions, db_name, c["name"]
            )
            collections[title] = {
                "id": title,
                "title": title,
                "description": None,
                "can_read": can_read,
                "can_write": can_write,
                "media_types": [
                    "application/stix+json;version=2.1"
                ],
            }
        # remove all collections without vertex or edge collection
        return list(collections.values())

    @staticmethod
    def split_collection_info(collection_id):
        match = COLLECTION_INFO_RE.match(collection_id)
        if not match:
            return collection_id, None
        return match.group(1), match.group(2)

    def get_collection(self, db_name, collection_id):
        alias = collection_id
        title, ctype = self.split_collection_info(collection_id)
        if not ctype:
            collection_id = f"{collection_id}_vertex_collection"
        url = urljoin(self.HOST_URL, f"/_db/{db_name}/_api/collection/{collection_id}")
        resp = self.make_request('GET', url)
        can_read, can_write = self.get_collection_permission(db_name, alias)
        return {
            "id": alias,
            "title": title,
            "description": ctype,
            "can_read": can_read,
            "can_write": can_write,
            "media_types": [
                "application/stix+json;version=2.1"
            ],
        }

    def get_objects_all(self, db_name, collection_id, query_params, query_type):
        url = urljoin(self.HOST_URL, f"/_db/{db_name}/_api/cursor/")
        payload = None
        if next := query_params.get("next"):
            splits = next.split("_")
            query_params['added_after'] = splits[-1]

        payload = self.build_query(collection_id, query_params, query_type)
        resp = self.make_request('POST', url, json=payload)

        # delete _record_created and add set first and last dates
        if resp.result:
            added_last = "0000"
            added_first = "9999"
            for r in resp.result:
                date_added = r["_record_created"]
                if date_added < added_first:
                    added_first = date_added
                if date_added > added_last:
                    added_last = date_added
                del r["_record_created"]
            resp.dict.update(added_last=added_last, added_first=added_first)

        if resp.dict.get("hasMore"):
            resp.dict["next"] = (
                f"{resp.dict['id']}_{resp.dict.get('added_last')}"
            )

        return resp

    def remove_object(
        self, db_name, collection, object_id, match_version=None, match_spec_version=[]
    ):
        vertex, edge = (
            f"{collection}_vertex_collection",
            f"{collection}_edge_collection",
        )

        AQL = """
        LET vertices = (
            FOR doc in @@vertex_collection  OPTIONS {indexHint: "taxii_search", forceIndexHint: true}
                FILTER doc.id == @object_id
                FILTER doc.spec_version IN @spec_versions OR LENGTH(@spec_versions) == 0
                RETURN {type: "vertex", _key: doc._key, modified: doc.modified}
        )
        LET edges = (
            FOR doc in @@edge_collection  OPTIONS {indexHint: "taxii_search", forceIndexHint: true}
                FILTER doc.id == @object_id
                FILTER doc.spec_version IN @spec_versions OR LENGTH(@spec_versions) == 0
                RETURN {type: "edge", _key: doc._key, modified: doc.modified}
        )

        FOR doc in APPEND(vertices, edges)
        RETURN doc
        """
        url = urljoin(self.HOST_URL, f"/_db/{db_name}/_api/cursor/")
        resp = self.make_request('POST', 
            url,
            json=dict(
                query=AQL,
                bindVars={
                    "object_id": object_id,
                    "@vertex_collection": vertex,
                    "@edge_collection": edge,
                    "spec_versions": match_spec_version,
                },
            ),
        )

        versions = (match_version or "all").split(",")
        objects_to_remove = []
        results = sorted(resp.result, key=lambda result: result["modified"])

        for i, result in enumerate(results):
            if result["modified"] in versions or "all" in versions:
                objects_to_remove.append(result)
            elif "first" in versions and result["modified"] == results[0]["modified"]:
                objects_to_remove.append(result)
            elif "last" in versions and result["modified"] == results[-1]["modified"]:
                objects_to_remove.append(result)

        DELETE_AQL = """
        LET a = (
            FOR doc in @object_ids
                FILTER doc.type == "vertex"
                REMOVE doc in @@vertex_collection
                RETURN NULL
        )

        LET b = (
            FOR doc in @object_ids
                FILTER doc.type == "edge"
                REMOVE {_key: doc._key} in @@edge_collection
                RETURN NULL
        )

        RETURN NULL
        """

        url = urljoin(self.HOST_URL, f"/_db/{db_name}/_api/cursor/")
        resp = self.make_request('POST', 
            url,
            json=dict(
                query=DELETE_AQL,
                bindVars={
                    "object_ids": objects_to_remove,
                    "@vertex_collection": vertex,
                    "@edge_collection": edge,
                },
            ),
        )
        
        return resp

    def build_query(self, collection, query_params, req_type="manifest"):
        _, ctype = self.split_collection_info(collection)
        if ctype:
            """
            if specific collection is used
            """
            binding = {"@collection": collection}
        else:
            vertex, edge = (
                f"{collection}_vertex_collection",
                f"{collection}_edge_collection",
            )
            binding = {"@vertex_collection": vertex, "@edge_collection": edge}

        


        collection_query = """
        FOR doc IN @@collection OPTIONS {indexHint: "taxii_search", forceIndexHint: true}
        FILTER doc._record_created > @added_after
        // [MORE_FILTERS]
        SORT doc._record_created ASC
        LIMIT @limit
        RETURN doc
        """

        binding['added_after'] = query_params.get('added_after', '')
        version_filters = []
        match_versions = []
        match_version = list(set(query_params.get("match[version]", "last").split(",")))
        for v in match_version:
            match v:
                case 'last':
                    version_filters.append('doc._taxii.last == TRUE')
                case 'first':
                    version_filters.append('doc._taxii.first == TRUE')
                case 'all':
                    version_filters = ['doc._taxii.visible == TRUE']
                    break
                case _:
                    match_versions.append(v)
        if match_versions:
            binding['match_versions'] = match_versions
            version_filters.append('(doc._taxii.visible == TRUE AND doc.modified IN @match_versions)')

        more_filters = []

        more_filters.append('({})'.format(' OR '.join(version_filters)))

        if self.visible_to_ref:
            binding['visible_to_ref'] = self.visible_to_ref
            binding['marking_visible_to_all'] = ["marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487", "marking-definition--bab4a63c-aed9-4cf5-a766-dfca5abac2bb"]
            more_filters.append("(doc.created_by_ref IN [NULL, @visible_to_ref] OR (@marking_visible_to_all ANY IN doc.object_marking_refs))")

        if stix_type := query_params.get("match[type]", ""):
            more_filters.append("doc.type IN @match_type")
            binding["match_type"] = stix_type.split(",")

        if match_id := query_params.get("match[id]"):
            more_filters.append('doc.id IN @match_id')
            binding["match_id"] = match_id.split(",")

        if match_spec_version := query_params.get("match[spec_version]"):
            more_filters.append("doc.spec_version IN @spec_versions")
            binding["spec_versions"] = match_spec_version.split(",")

        if more_filters:
            collection_query = collection_query.replace("// [MORE_FILTERS]", "FILTER " + " AND ".join(more_filters))


        retval = {"bindVars": binding}

        batchSize = int(query_params.get("limit", arango_taxii_server_settings.DEFAULT_PAGINATION_LIMIT))
        retval["batchSize"] = batchSize
        binding['limit'] = batchSize + 1

        AQL = f"""
        LET vertices = (
            {collection_query.replace("@@collection", "@@vertex_collection")}
        )
        LET edges = (
            {collection_query.replace("@@collection", "@@edge_collection")}
        )

        FOR doc in UNION(vertices, edges)
        SORT doc._record_created ASC
        LIMIT @limit
        
        """


        if req_type in ["manifest", "versions"]:
            AQL += """
            RETURN { 
                id: doc.id,
                date_added: doc._record_created,
                _record_created: doc._record_created,
                version: doc.modified or doc.created or doc._record_created,
            }
            """
        elif req_type == "objects":
            AQL += """
            RETURN KEEP(doc, PUSH(ATTRIBUTES(doc, true), "_record_created"))
            """
        else:
            raise ArangoError(500, f"unknown request type: {req_type}")
        retval["query"] = AQL
        # print(json.dumps(binding))
        # print(AQL, json.dumps(binding))
        return retval

    @classmethod
    def parse_permission(cls, value):
        p = None
        permissions_map = {
            "ro": (True, False),
            "rw": (True, True),
            "undefined": None,
            "none": (False, False),
        }
        if isinstance(value, str):
            p = permissions_map[value]
        elif isinstance(value, dict):
            p = cls.parse_permission(value["permission"])
        return p

    @staticmethod
    def parse_response(response: requests.Response):
        resp = ArangoResponse(response)
        if resp.error:
            raise resp.error
        return resp

    
    def validate_bundle(self, objects):
        obj_set = set()
        for obj in objects:
            id = obj.get('id')
            if id in obj_set:
                raise StixValidationError(f"duplicate object with id: {id}")
            obj_set.add(id)
        return True


class ArangoError(Exception):
    def __init__(self, http_code, message) -> None:
        self.http_code = http_code
        self.message = f"arango server: {message}"
        super().__init__(message)

    def __str__(self) -> str:
        return f"{self.__class__}(http_code={self.http_code}, message={self.message})"
    
class StixValidationError(Exception):
    def __init__(self, message) -> None:
        self.http_code = 400
        self.message = f"object validation error: {message}"
        super().__init__(message)



class ArangoResponse:
    error = None
    result = None

    def __init__(self, reponse: requests.Response) -> None:
        json = reponse.json()
        if json["error"]:
            self.error = ArangoError(
                reponse.status_code,
                "remote error: {errorNum} - {errorMessage}".format_map(json),
            )
            return
        self.result = json.get("result", json)
        self.dict = json
