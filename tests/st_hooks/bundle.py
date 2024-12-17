bundle = {
    "id": "bundle--4b948b5a-3ce9-53f5-b48a-da95c3964cb5",
    "objects": [
        {
            "type": "attack-pattern",
            "spec_version": "2.1",
            "id": "attack-pattern--6b948b5a-3c09-5365-b48a-da95c3964cb7",
            "created_by_ref": "identity--d2916708-57b9-5636-8689-62f049e9f727",
            "created": "2020-01-01T11:21:07.478851Z",
            "modified": "2020-01-01T11:21:07.478851Z",
            "name": "Spear Phishing",
            "description": "Used for tutorial content",
            "object_marking_refs": ["marking-definition--34098fce-860f-48ae-8e50-ebd3cc5e41da"]
        },
        {
            "type": "attack-pattern",
            "spec_version": "2.1",
            "id": "attack-pattern--6b948b5a-3c09-5365-b48a-da95c3964cb5",
            "created_by_ref": "identity--d2916708-57b9-5636-8689-62f049e9f727",
            "created": "2020-01-02T11:21:07.478851Z",
            "modified": "2020-01-02T11:21:07.478851Z",
            "name": "Spear Phishing Updated ONCE",
            "description": "Used for tutorial content",
            "object_marking_refs": ["marking-definition--34098fce-860f-48ae-8e50-ebd3cc5e41da"]
        },
        {
            "type": "attack-pattern",
            "spec_version": "2.1",
            "id": "attack-pattern--6b948b5a-3c09-5365-b48a-da95c3964cb6",
            "created_by_ref": "identity--d2916708-57b9-5636-8689-62f049e9f727",
            "created": "2020-01-03T11:21:07.478851Z",
            "modified": "2020-01-03T11:21:07.478851Z",
            "name": "Spear Phishing Updated TWICE",
            "description": "Used for tutorial content",
            "object_marking_refs": ["marking-definition--34098fce-860f-48ae-8e50-ebd3cc5e41da"]
        }
    ]
}
TEST_DB = "ats_test"
TEST_COLLECTION = "ats_test"
TEST_API_ROOT = f"{TEST_DB}_database"

from base64 import b64encode
import os
from typing import Optional
import schemathesis, schemathesis.schemas
from schemathesis.specs.openapi.schemas import BaseOpenAPISchema
from schemathesis import Case, hooks
from schemathesis.transports.responses import GenericResponse
import logging

@schemathesis.hook
def after_load_schema(
    context: schemathesis.hooks.HookContext,
    schema: BaseOpenAPISchema,
) -> None:

    schema.add_link(
        source=schema["/api/taxii2/{api_root}/collections/{collection_id}/objects/"]["POST"],
        target=schema["/api/taxii2/{api_root}/status/{status_id}/"]['GET'],
        status_code=200,
        parameters={
            "path.api_root": '$request.path.api_root',
            "path.status_id": "$response.body#/id",
        }
    )

    schema.add_link(
        source=schema["/api/taxii2/{api_root}/collections/{collection_id}/objects/"]["POST"],
        target=schema["/api/taxii2/{api_root}/collections/"]['GET'],
        status_code=200,
        parameters={
            "path.api_root": '$request.path.api_root',
        }
    )

@schemathesis.hook
def add_case(
    context: hooks.HookContext, case: Case, response: GenericResponse
) -> Optional[Case]:
    if case.method == 'POST':
        if not getattr(case.operation.schema, 'test_post', None):
            case.operation.schema.test_post = 1
            case.body = bundle
            case.path_parameters = dict(api_root=TEST_API_ROOT, collection_id=TEST_COLLECTION)
            return case

@schemathesis.hook
def after_load_schema(
    context: schemathesis.hooks.HookContext,
    schema: BaseOpenAPISchema,):
    logging.info("Running stix2arango")
    
    username = os.getenv('ARANGODB_USERNAME', 'root')
    password = os.getenv('ARANGODB_PASSWORD', '')

    @schema.auth()
    class MyAuth:
        def get(self, case, context):
            return True

        def set(self, case, data, context):
            case.headers = case.headers or {}

            token = b64encode(f"{username}:{password}".encode('utf-8')).decode("ascii")
            case.headers["Authorization"] = f'Basic {token}'

    try:
        from stix2arango.stix2arango import Stix2Arango
        Stix2Arango(database=TEST_DB, collection=TEST_COLLECTION, file=None, host_url=os.getenv('ARANGODB_HOST_URL'), username=username, password=password)
    except:
        logging.info("failed to auth")
    