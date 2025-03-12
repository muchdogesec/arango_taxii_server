import json
import schemathesis, schemathesis.schemas
from schemathesis.specs.openapi.schemas import BaseOpenAPISchema
from schemathesis import Case
from schemathesis.transports.responses import GenericResponse

@schemathesis.hook
def before_call(context, case: Case):
    case.headers["accept"] = "application/taxii+json;version=2.1"

@schemathesis.hook
def after_call(context, case: Case, response: GenericResponse):
    if case.path == "/api/taxii2/" and response.status_code == 200 and response.request.method == 'GET':
        parsed = response.json()
        parsed['api_roots'] = [api_root.split('/')[-2] for api_root in parsed['api_roots']]
        response._content = json.dumps(parsed).encode()


@schemathesis.hook
def after_load_schema(
    context: schemathesis.hooks.HookContext,
    schema: BaseOpenAPISchema,
) -> None:
    
    schema.add_link(
        source=schema["/api/taxii2/"]['GET'],
        target=schema["/api/taxii2/{api_root}/"]['GET'],
        status_code=200,
        parameters={"path.api_root": '$response.body#/api_roots/0'}
    )

    schema.add_link(
        source=schema["/api/taxii2/"]['GET'],
        target=schema["/api/taxii2/{api_root}/collections/"]['GET'],
        status_code=200,
        parameters={"path.api_root": '$response.body#/api_roots/0'}
    )

    for target in ["", "manifest/", "objects/"]:
        schema.add_link(
            source=schema["/api/taxii2/{api_root}/collections/"]['GET'],
            target=schema["/api/taxii2/{api_root}/collections/{collection_id}/"+target]['GET'],
            status_code=200,
            parameters={
                "path.api_root": '$request.path.api_root',
                "path.collection_id": "$response.body#/collections/0/id",
            }
        )