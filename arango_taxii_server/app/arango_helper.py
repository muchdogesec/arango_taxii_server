import json
import os
import random
import re
import subprocess
from urllib.parse import urljoin, urlparse
from django.conf import settings
from datetime import datetime

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
        p = None

        if isinstance(value, str):
            p = cls.permissions_map[value]
        elif isinstance(value, dict):
            p = cls.parse_permission(value["permission"])
        return p


class ArangoSession:
    HOST_URL = os.environ["ARANGODB"]

    def __init__(self, arango_auth) -> None:
        self.user, self.password = arango_auth
        self.session = requests.Session()
        self.session.auth = arango_auth

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
        resp = self.parse_response(self.session.get(url, params=dict(full=1)))
        retval = resp.result
        return retval

    def get_collection_permission(self, db_name, collection):
        url = urljoin(
            self.HOST_URL, f"/_api/user/{self.user}/database/{db_name}/{collection}"
        )
        resp = self.parse_response(self.session.get(url, params=dict(full=1)))
        retval = resp.result
        return ArangoFullPermissionParser.parse_permission(retval)

    def get_databases(self):
        url = urljoin(self.HOST_URL, f"/_api/user/{self.user}/database")
        resp = self.parse_response(self.session.get(url))
        return list(resp.result.keys())

    def get_database(self, db_name):
        url = urljoin(
            self.HOST_URL, f"/_db/{db_name}/_api/user/{self.user}/database/{db_name}"
        )
        resp = self.parse_response(self.session.get(url))
        return self.parse_permission(resp.result)

    def get_collections(self, db_name):
        url = urljoin(self.HOST_URL, f"/_db/{db_name}/_api/collection")
        resp = self.parse_response(self.session.get(url))
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
        resp = self.parse_response(self.session.get(url))
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
            cursor_id, added_after = next.split("_")
            query_params['added_after'] = added_after
        #     url = urljoin(url, cursor_id)
        # else:
        payload = self.build_query(collection_id, query_params, query_type)
        resp = self.parse_response(self.session.post(url, json=payload))

        # delete _record_modified and add set first and last dates
        if resp.result:
            added_last = "0000"
            added_first = "9999"
            for r in resp.result:
                date_added = r["_record_modified"]
                if date_added < added_first:
                    added_first = date_added
                if date_added > added_last:
                    added_last = date_added
                del r["_record_modified"]
            resp.dict.update(added_last=added_last, added_first=added_first)

        if resp.dict.get("hasMore"):
            resp.dict["next"] = (
                f"{resp.dict['id']}_{resp.dict.get('added_last')}"
            )

        return resp

    def remove_object(
        self, db_name, collection, object_id, match_version=None, match_spec_version=""
    ):
        vertex, edge = (
            f"{collection}_vertex_collection",
            f"{collection}_edge_collection",
        )

        AQL = """
        LET vertices = (
            FOR doc in @@vertex_collection
                FILTER doc.id == @object_id
                FILTER CONTAINS(@spec_versions, doc.spec_version) OR LENGTH(@spec_versions) == 0
                RETURN {type: "vertex", _key: doc._key, modified: doc.modified}
        )
        LET edges = (
            FOR doc in @@edge_collection
                FILTER doc.id == @object_id
                FILTER CONTAINS(@spec_versions, doc.spec_version) OR LENGTH(@spec_versions) == 0
                RETURN {type: "edge", _key: doc._key, modified: doc.modified}
        )

        FOR doc in APPEND(vertices, edges)
        RETURN doc
        """
        url = urljoin(self.HOST_URL, f"/_db/{db_name}/_api/cursor/")
        resp = self.parse_response(
            self.session.post(
                url,
                json=dict(
                    query=AQL,
                    bindVars={
                        "object_id": object_id,
                        "@vertex_collection": vertex,
                        "@edge_collection": edge,
                        "spec_versions": match_spec_version.split(","),
                    },
                ),
            )
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
        resp = self.parse_response(
            self.session.post(
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
        )
        return resp

    def build_query(self, collection, query_params, req_type="manifest"):
        _, ctype = self.split_collection_info(collection)
        if ctype:
            """
            if specific collection is used
            """
            binding = {"@collection": collection}
            aql_documents_str = "(FOR doc IN @@collection RETURN doc)"
        else:
            aql_documents_str = "APPEND((FOR doc IN @@edge_collection RETURN doc), (FOR doc IN @@vertex_collection RETURN doc))"
            vertex, edge = (
                f"{collection}_vertex_collection",
                f"{collection}_edge_collection",
            )
            binding = {"@vertex_collection": vertex, "@edge_collection": edge}

        collection_query = """
        FOR doc IN @@collection
        FILTER doc._record_modified > @added_after
        // [MORE_FILTERS]
        SORT doc._record_modified
        LET versions = MERGE(
        FOR inner IN @@collection
        FILTER inner.id == doc.id
        COLLECT version = inner.modified OR inner.created AGGREGATE createdAt = MAX(inner._record_modified)
        RETURN {[version]: createdAt}
        )
        LET current_version = doc.modified OR doc.created
        LET all_versions = MERGE(versions, {"first": versions[MIN(KEYS(versions))], "last": versions[MAX(KEYS(versions))]})
        LET match_version = "all" IN @match_version ? KEYS(versions) : @match_version OR ["last"]

        FILTER LENGTH(
        FOR v in match_version
        FILTER doc._record_modified == all_versions[v]
        RETURN 1
        )
        LIMIT @limit
        RETURN doc
        """

        binding['added_after'] = query_params.get('added_after', '')
        binding['match_version'] = list(set(query_params.get("match[version]", "last").split(",")))
        more_filters = []
        if stix_type := query_params.get("match[type]", ""):
            more_filters.append("CONTAINS(@match_type, doc.type)")
            binding["match_type"] = stix_type.split(",")

        if match_id := query_params.get("match[id]"):
            more_filters.append('CONTAINS(@match_id, doc.id)')
            binding["match_id"] = match_id.split(",")

        if match_spec_version := query_params.get("match[spec_version]"):
            more_filters.append("(CONTAINS(@spec_versions, doc.spec_version) OR LENGTH(@spec_versions) == 0)")
            binding["spec_versions"] = match_spec_version.split(",")

        if more_filters:
            collection_query = collection_query.replace("// [MORE_FILTERS]", "FILTER " + " AND ".join(more_filters))


        retval = {"bindVars": binding}

        batchSize = int(query_params.get("limit", settings.DEFAULT_PAGINATION_LIMIT))
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
        SORT doc._record_modified
        LIMIT @limit
        
        """


        if req_type in ["manifest", "versions"]:
            AQL += """
            RETURN { 
                id: doc.id,
                date_added: doc._record_modified,
                _record_modified: doc._record_modified,
                version: doc.modified or doc.created,
            }
            """
        elif req_type == "objects":
            AQL += """
            RETURN KEEP(doc, PUSH(ATTRIBUTES(doc, true), "_record_modified"))
            """
        else:
            raise ArangoError(500, f"unknown request type: {req_type}")
        retval["query"] = AQL
        # print(json.dumps(binding))
        # print(AQL)
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
