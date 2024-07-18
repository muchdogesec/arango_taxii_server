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
DB_NAME_RE = re.compile(r'(\w+)_database')

class ArangoFullPermissionParser:
    permissions_map = {
            "rw": (True, True),
            "ro": (True, False),
            "none": (False, False),
            "undefined": None,
        }

    @classmethod
    def get_permission(cls, permissions, db_name, collection):
        server_default = permissions.get('*', {}).get('permission')
        db_permission = permissions[db_name]['permission']
        collection_default = permissions[db_name]['collections']['*']
        actual_permission = permissions[db_name]['collections'][collection]
        if actual_permission != "undefined":
            return cls.parse_permission(actual_permission)
        for default_permission in ["rw", "ro", "none", "undefined"]:
            if default_permission in [server_default, collection_default, db_permission]:
                return cls.parse_permission(default_permission)


    @classmethod
    def parse_permission(cls, value):
        p = None
        
        if isinstance(value, str):
            p = cls.permissions_map[value]
        elif isinstance(value, dict):
            p = cls.parse_permission(value['permission'])
        return p


class ArangoSession:
    HOST_URL = os.environ['ARANGODB']
    stix2arango_path = conf.stix2arango_path
    def __init__(self, arango_auth) -> None:
        self.user, self.password = arango_auth
        self.session = requests.Session()
        self.session.auth = arango_auth
        
    def get_permissions(self, db_name=None):
        url = urljoin(self.HOST_URL, f"/_api/user/{self.user}/database")
        resp = self.parse_response(self.session.get(url, params=dict(full=1)))
        retval = resp.result
        return retval

    def get_collection_permission(self, db_name, collection):
        url = urljoin(self.HOST_URL, f"/_api/user/{self.user}/database/{db_name}/{collection}")
        resp = self.parse_response(self.session.get(url, params=dict(full=1)))
        retval = resp.result
        return ArangoFullPermissionParser.parse_permission(retval)

    def get_databases(self):
        url = urljoin(self.HOST_URL, f"/_api/user/{self.user}/database")
        resp = self.parse_response(self.session.get(url))
        return list(resp.result.keys())

    def get_database(self, db_name):
        url = urljoin(self.HOST_URL, f"/_db/{db_name}/_api/user/{self.user}/database/{db_name}")
        resp = self.parse_response(self.session.get(url))
        return self.parse_permission(resp.result)

    def get_collections(self, db_name):
        url = urljoin(self.HOST_URL, f"/_db/{db_name}/_api/collection")
        resp = self.parse_response(self.session.get(url))
        permissions = self.get_permissions()
        collections = {}
        for c in resp.result:
            if c['isSystem']:
                continue
            alias = c['name']
            title, ctype = self.split_collection_info(alias)
            if not ctype:
                continue
            if title in collections:
                collections[title].update(id=title, description='vertex+edge')
                continue
            can_read, can_write = ArangoFullPermissionParser.get_permission(permissions, db_name, alias)
            collections[title] = {
                'id': alias,
                'title': title,
                'description': ctype,
                'can_read': can_read,
                'can_write': can_write,
            }
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
            'id': alias,
            'title': title,
            'description': ctype,
            'can_read': can_read,
            'can_write': can_write,
        }
   
    def get_objects_all(self, db_name, collection_id, query_params, query_type):
        url = urljoin(self.HOST_URL, f"/_db/{db_name}/_api/cursor/")
        payload = None
        if next:=query_params.get('next'):
            cursor_id, batch_id = next.split('_')
            url = urljoin(url, cursor_id)
        else:
            payload = self.build_query(collection_id, query_params, query_type)
        resp = self.parse_response(self.session.post(url, json=payload))
        if resp.dict.get('hasMore'):
            resp.dict['next'] = f"{resp.dict['id']}_{resp.dict.get('nextBatchId', f'undef+{random.random()}')}"

        # if query_type == 'versions':
        #     resp.result = [x["modified"] for x in resp.result]
        
        # delete _record_modified and add set first and last dates
        if resp.result:
            added_last = "0000"
            added_first = "9999"
            for r in resp.result:
                date_added = r['_record_modified']
                if date_added < added_first:
                    added_first = date_added
                if date_added > added_last:
                    added_last = date_added
                del r['_record_modified']
            resp.dict.update(added_last=added_last, added_first=added_first)

        return resp

    def remove_object(self, db_name, collection, object_id, match_version=None, match_spec_version=""):
        vertex, edge = f"{collection}_vertex_collection", f"{collection}_edge_collection"

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
        resp = self.parse_response(self.session.post(url, json=dict(query=AQL, bindVars={"object_id":object_id, "@vertex_collection": vertex, "@edge_collection": edge, "spec_versions": match_spec_version.split(",")})))
        
        versions = (match_version or "all").split(",")
        objects_to_remove = []
        results = sorted(resp.result, key=lambda result: result["modified"])

        for i, result in enumerate(results):
            if result['modified'] in versions or "all" in versions:
                objects_to_remove.append(result)
            elif "first" in versions and result['modified'] == results[0]['modified']:
                objects_to_remove.append(result)
            elif "last" in versions  and result['modified'] == results[-1]['modified']:
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
        resp = self.parse_response(self.session.post(url, json=dict(query=DELETE_AQL, bindVars={"object_ids":objects_to_remove, "@vertex_collection": vertex, "@edge_collection": edge})))
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
            vertex, edge = f"{collection}_vertex_collection", f"{collection}_edge_collection"
            binding = {"@vertex_collection": vertex, "@edge_collection": edge}

        AQL = f"""
            LET documents = {aql_documents_str}
            FOR doc IN documents
                FILTER NOT STARTS_WITH(doc.id, "_")

        """
        retval = {"bindVars":binding}
        if versions := set(query_params.get("match[version]", 'last').split(",")):
            filters = []
            if 'last' in versions:
                versions.remove('last')
                filters.append("id_doc.modified == MAX(docs_by_id[*].doc.modified)")
            if 'first' in versions:
                versions.remove('first')
                filters.append("id_doc.modified == MIN(docs_by_id[*].doc.modified)")
            if versions:
                filters.append("CONTAINS(SPLIT(@versions,','), id_doc.modified)")
                binding['versions'] = ",".join(versions)


            if 'all' not in versions:
                aql_filters = "FILTER " + " OR ".join(filters)
                AQL += f"""
            COLLECT id = doc.id into docs_by_id
            RETURN (
                FOR id_doc in docs_by_id[*].doc
                {aql_filters}
                RETURN id_doc
            )
                """
                AQL = f"FOR doc in FLATTEN({AQL})"
            else:
                binding.pop('versions', None)

        batchSize = query_params.get('limit', settings.DEFAULT_PAGINATION_LIMIT)
        retval['batchSize'] = int(batchSize)
        
        if added_after := query_params.get('added_after'):
            AQL += """
            FILTER doc._record_modified > @added_after
            """
            binding["added_after"] = added_after

        if stix_type := query_params.get("match[type]", ""):
            AQL += """
            FILTER CONTAINS(@match_type, doc.type)
            """
            binding['match_type'] = stix_type.split(",")

        
        if match_id := query_params.get("match[id]"):
            AQL += """
            FILTER CONTAINS(@match_id, doc.id)
            """
            binding['match_id'] = match_id.split(',')

        if match_spec_version := query_params.get("match[spec_version]"):
            AQL += """
            FILTER CONTAINS(@spec_versions, doc.spec_version) OR LENGTH(@spec_versions) == 0
            """
            binding['spec_versions'] = match_spec_version.split(',')
        
        AQL += """
        /* START ---- make sure only one id, modified time pair ----- */
        COLLECT d_id = doc.id, d_version = doc.modified INTO grouped
        LET document = FIRST(
            FOR d in grouped[*].doc
            SORT d._record_modified
            LIMIT 1
            RETURN d
        )
        /* END ---- make sure only one id, modified time pair ----- */

        FILTER document.id != NULL
        SORT document._record_modified ASC

        """
        ###
        if req_type in ["manifest", "versions"]:
            AQL += """
            RETURN { 
                id: document.id,
                date_added: document._record_modified,
                _record_modified: document._record_modified,
                version: document.modified or document.created,
            }
            """
        elif req_type=="objects":
            AQL += """
            RETURN KEEP(document, PUSH(ATTRIBUTES(document, true), "_record_modified"))
            """
        else:
            raise ArangoError(500, f"unknown request type: {req_type}")
        retval["query"] = AQL
        return retval

    @classmethod
    def parse_permission(cls, value):
        p = None
        permissions_map = {
            "ro": (True, False),
            "rw": (True, True),
            "undefined": None,
            "none": (False, False)
        }
        if isinstance(value, str):
            p = permissions_map[value]
        elif isinstance(value, dict):
            p = cls.parse_permission(value['permission'])
        return p
    @staticmethod
    def parse_response(response: requests.Response):
        resp = ArangoResponse(response)
        if resp.error:
            raise resp.error
        return resp

    def stix2arango(self, db_name, collection, bundle_path, status_id):
        uri = urlparse(self.HOST_URL)
        env = {
            **os.environ,
            "ARANGODB_HOST": uri.hostname,
            "ARANGO_HOST": uri.hostname,
            "ARANGODB_PORT": str(uri.port),
            "ARANGODB_USERNAME": self.user,
            "ARANGODB_PASSWORD": self.password,
        }
        database, collection = self.stix2arango_validate(db_name, collection)
        args = [
            "python",
            self.stix2arango_path,
            "--file", bundle_path,
            "--database", database,
            "--collection", collection,
            "--stix2arango_note", f"arango_taxii_status_id={status_id}"
        ]
        # with tempfile.NamedTemporaryFile(delete=False) as f:
        return subprocess.check_call(args, env=env, cwd=self.stix2arango_path.parent)

    def stix2arango_validate(self, db_name, collection_id):
        db_m = DB_NAME_RE.match(db_name)
        cname_m = COLLECTION_INFO_RE.match(collection_id)
        if not db_m:
            raise ArangoError(400, f"unsupported value for {{arango_database_name}}: `{db_name}`, must be in form {{str}}_database")
        if cname_m:
            collection_id = cname_m.group(1)
        return db_m.group(1), collection_id

class ArangoError(Exception):
    def __init__(self, http_code, message) -> None:
        self.http_code = http_code
        self.message = message
        super().__init__(message)
    pass

class ArangoResponse:
    error = None
    result = None
    def __init__(self, reponse: requests.Response) -> None:
        json = reponse.json()
        if json['error']:
            self.error = ArangoError(reponse.status_code, "remote error: {errorNum} - {errorMessage}".format_map(json))
            return
        self.result = json.get('result', json)
        self.dict = json
