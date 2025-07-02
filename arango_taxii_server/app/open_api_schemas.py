from enum import Enum
from textwrap import dedent
from typing import Any, Dict, List, Literal, Sequence, Tuple

from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.openapi import AutoSchema, whitelisted
from drf_spectacular.utils import _SchemaType, OpenApiParameter, OpenApiExample
from drf_spectacular.types import OpenApiTypes
from rest_framework import renderers
from rest_framework.fields import empty

from arango_taxii_server.app.utils import TaxiiEnvelope

from .. import conf
from .authentication import ArangoServerAuthentication
import uritemplate

Datetime = {
    "allOf": [
        {
            "$ref": "https://raw.githubusercontent.com/oasis-open/cti-stix2-json-schemas/v2.0-wd01-r2/schemas/common/timestamp.json#"
        },
        {"format": "timestamp"},
    ]
}

StixIdentifier = {
    "allOf": [
        {
            "$ref": "https://raw.githubusercontent.com/oasis-open/cti-stix2-json-schemas/stix2.1/schemas/common/identifier.json#"
        },
        {
            "format": "stix-identifier",
            "example": "ipv4-addr--fe91801c-7c35-467c-9254-a9c6bb405afa",
        },
    ]
}

StixType = {
    "title": "type",
    "type": "string",
    "pattern": "^([a-z][a-z0-9]*)+(-[a-z0-9]+)*\\-?$",
    "minLength": 3,
    "maxLength": 250,
    "description": "The type property identifies the type of STIX Object (SDO, Relationship Object, etc). The value of the type field MUST be one of the types defined by a STIX Object (e.g., `indicator`).",
    "example": "ipv6-addr",
}


StixObject = {
    "type": "object",
    "format": "stix-object",
    "properties": {
        "id": StixIdentifier,
        "type": StixType,
        "created": dict(type="string"),
        "modified": dict(type="string"),
    },
    "additionalProperties": True,
}


TaxiiMatchID = {
    "type": "array",
    "items": StixIdentifier,
    "uniqueItems": True,
}

TaxiiMatchVersion = {
    "type": "array",
    "items": {
        "type": "string",
        "pattern": "last|all|first|^[0-9]{4}-[0-9]{2}-[0-9]{2}T[0-9]{2}:[0-9]{2}:[0-9]{2}(\\.[0-9]+)?Z$",
        "format": "version",
    },
    "uniqueItems": True,
}

TaxiiMatchSpecVersion = {"enum": ["2.1", "2.0"]}

TaxiiMatchType = {
    "type": "array",
    "items": StixType,
    "uniqueItems": True,
}


added_after_query = OpenApiParameter(
    "added_after",
    type=Datetime,
    description=dedent(
        """
    A single timestamp that filters objects to only include those objects added after the specified timestamp. This filter considers the `modified` time in an object if exists, else it considers the stix2arango `_record_created` time. The value of this parameter is a timestamp. In the format `YYYY-MM-DDThh:mm:ss.sssZ`
    """
    ),
)
limit_query = OpenApiParameter(
    TaxiiEnvelope.page_size_query_param,
    type=int,
    description=dedent(
        """
    A single integer value that indicates the maximum number of objects that the client would like to receive in a single response. The default returned is `50`. `50` is also the maximum number of results that can be returned in any response.
    """
    ),
)

next_query = OpenApiParameter(
    TaxiiEnvelope.page_query_param,
    type=OpenApiTypes.STR,
    description=dedent(
        """
    A single string value that indicates the next record or set of records in the dataset that the client is requesting. This value can be found in the `next` property of the current response (current page). e.g. `48384495_2024-07-24T09:00:26.609560Z`
    """
    ),
)

match_id_query = OpenApiParameter(
    "match[id]",
    type=TaxiiMatchID,
    description=dedent(
        """
    The identifier of the object(s) that are being requested. This is the STIX `id` of the object, e.g. `indicator--00ee0481-1b16-4c0c-a0e6-43f51d172a81`
    """
    ),
    style="form",
    explode=False,
)

match_type_query = OpenApiParameter(
    "match[type]",
    type=TaxiiMatchType,
    description=dedent(
        """
    The type of the object(s) that are being requested. This is the STIX `type`, e.g. `attack-pattern`
    """
    ),
    style="form",
    explode=False,
)

match_version_query = OpenApiParameter(
    "match[version]",
    type=TaxiiMatchVersion,
    description=dedent(
        """
    The version of the object(s) that are being requested. If no version parameter is provided, the latest version of the object will be returned.

    Valid values for the version parameter are:

    - `last`: requests the latest version of an object. This is the default parameter value.
    - `first`: requests the earliest version of an object
    - `all`: requests all versions of an object
    - `<modified>`: requests a specific version of an object. For example: `2016-01-01T00:00:00.000Z` tells the server to give you the exact STIX object with a
    `modified` time of `2016-01-01T00:00:00.000Z`.

    Note, for objects with a `modified` time, this value will be considered as the version. For objects without a `modified` time, the stix2arango `_record_created` value will be used to determine version.
    """
    ),
    style="form",
    explode=False,
)

match_spec_version_query = OpenApiParameter(
    "match[spec_version]",
    type=TaxiiMatchSpecVersion,
    description="The specification version(s) of the STIX object that are being requested. Arango TAXII Server only support STIX 2.1, so `2.1` is not only the default value but also the only value that can be passed.",
    style="form",
    explode=False,
)

ObjectsQueryParams = [
    added_after_query,
    limit_query,
    next_query,
    match_id_query,
    match_type_query,
    match_version_query,
    match_spec_version_query,
]

VersionsQueryParams = [
    added_after_query,
    limit_query,
    next_query,
    match_spec_version_query,
]

SingleObjectQueryParams = [
    added_after_query,
    limit_query,
    next_query,
    match_version_query,
    match_spec_version_query,
]

ObjectDeleteParams = [
    match_version_query,
    match_spec_version_query,
]


class ArangoTaxiiOpenApiExample(OpenApiExample):
    def __init__(self, *args, **kwargs):
        kwargs["media_type"] = conf.taxii_type
        super().__init__(*args, **kwargs)


class OpenApiTags(Enum):
    API_ROOT = "Taxii API - Server Information"
    COLLECTIONS = "Taxii API - Collections"
    SCHEMA = "schema"

    @property
    def tags(self):
        return [self.value]


from drf_spectacular.settings import spectacular_settings

class CustomAutoSchema(AutoSchema):
    global_params = []
    url_path_params = {
        "collection_id": OpenApiParameter(
            "collection_id",
            type=str,
            location=OpenApiParameter.PATH,
            description="The identifier of the Collection being requested. You can get a Collection ID from the GET Collections for an API Root endpoint.",
        ),
        "api_root": OpenApiParameter(
            "api_root",
            type=str,
            location=OpenApiParameter.PATH,
            description="The API Root name. Do not include the full URL. e.g. use `my_api_root` NOT `http://127.0.0.1:8009/api/taxii2/my_api_root/`",
        ),
        "object_id": OpenApiParameter(
            "object_id",
            type=str,
            location=OpenApiParameter.PATH,
            description="The STIX ID of the object being requested. e.g. `indicator--00ee0481-1b16-4c0c-a0e6-43f51d172a81`. You can search for objects using the GET objects in a Collection endpoint.",
        ),
        "status_id": OpenApiParameter(
            "status_id",
            type=OpenApiTypes.UUID,
            location=OpenApiParameter.PATH,
            description="The status ID of the job being requested. The status ID is obtained in a successful response from the POST objects endpoint.",
        ),
    }

    def get_override_parameters(self):
        params = super().get_override_parameters()
        for path_variable in uritemplate.variables(self.path):
            if param := self.url_path_params.get(path_variable):
                params.append(param)
        if "taxii2/" not in self.path:
            return params

        return params + self.global_params

    def _is_list_view(self, *args, **kwargs):
        if getattr(self.view, "pagination_class", None):
            return True
        return False
    
    def is_excluded(self):
        if getattr(self.view, 'is_arango_taxii_server_view', None):
            return getattr(self.view, 'schema_exclude', True) #only show if we're using our generator
        return super().is_excluded()

    def map_renderers(self, attribute: str) -> list[Any]:
        assert attribute in ["media_type", "format"]

        # Either use whitelist or default back to old behavior by excluding BrowsableAPIRenderer
        def use_renderer(r):
            if spectacular_settings.RENDERER_WHITELIST is not None:
                return whitelisted(r, spectacular_settings.RENDERER_WHITELIST)
            else:
                return not isinstance(r, renderers.BrowsableAPIRenderer)

        keys = []
        for r in self.view.get_renderers():
            if use_renderer(r) and hasattr(r, attribute):
                media_type = getattr(r, attribute)
                keys.append(media_type)

        return keys


class ArangoServerAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = ArangoServerAuthentication
    name = "ArangoBasicAuth"
    priority = -1

    def get_security_definition(self, auto_schema):
        return {
            "type": "http",
            "scheme": "basic",
        }
