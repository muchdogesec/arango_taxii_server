from enum import Enum
from textwrap import dedent

from drf_spectacular.extensions import OpenApiAuthenticationExtension
from drf_spectacular.openapi import AutoSchema
from drf_spectacular.utils import OpenApiParameter
from drf_spectacular.types import OpenApiTypes

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
    "description": "The type property identifies the type of STIX Object (SDO, Relationship Object, etc). The value of the type field MUST be one of the types defined by a STIX Object (e.g., indicator).",
    "example": "ipv6-addr"
}


EnvelopeObjectsObject = {
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


added_after_query = OpenApiParameter("added_after", type=Datetime, description=dedent("""
    A single timestamp that filters objects to only include those objects added after the specified timestamp. The value of this parameter is a timestamp.
    """))
limit_query = OpenApiParameter(
    "limit",
    type=int,
    description=dedent(
        """
    A single integer value that indicates the maximum number of objects that the client would like to receive in a single response.
    """
    ),
    default=10,
)

next_query = OpenApiParameter(
    "next",
    type=int,
    description=dedent(
        """
    A single string value that indicates the next record or set of records in the dataset that the client is requesting.
    """
    ),
)

match_id_query = OpenApiParameter(
    "match[id]",
    type=TaxiiMatchID,
    description=dedent(
        """
    The identifier of the object(s) that are being requested. When searching for a STIX Object, this is a STIX ID.
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
    The type of the object(s) that are being requested. Only the types listed in this parameter are permitted in the response.
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
    The version of the object(s) that are being requested. If no version parameter is provided, the server MUST
    return the latest version of the object.
    Valid values for the version parameter are:
    - `last`: requests the latest version of an object. This is the default parameter value.
    - `first`: requests the earliest version of an object
    - `all`: requests all versions of an object
    - `<modified>`: requests a specific version of an object. For example: "2016-01-01T01:01:01.000Z" tells the server to give you the exact STIX object with a
    modified time of "2016-01-01T01:01:01.000Z".
    """
    ),
    style="form",
    explode=False,
)

match_spec_version_query = OpenApiParameter(
    "match[spec_version]",
    type=TaxiiMatchSpecVersion,
    description="The specification version(s) of the STIX object that are being requested.",
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
]

VersionsQueryParams = [
    added_after_query,
    limit_query,
    next_query,
]

SingleObjectQueryParams = [
    added_after_query,
    limit_query,
    next_query,
    match_version_query,
]


class OpenApiTags(Enum):
    API_ROOT = {
        "name": "Taxii API - Server Information",
        "description": dedent("""
        Information about this TAXII Server, the available API Roots, and to retrieve the status of requests.
        """)
    }
    COLLECTIONS = {
        "name": "Taxii API - Collections",
        "description": dedent("""
        Collections are hosted in the context of an API Root. Each API Root MAY have zero or more Collections. As with other TAXII Endpoints, the ability of TAXII Clients to read from and write to Collections can be restricted depending on their permissions level.
        """)
    }
    SCHEMA = {
        "name": "schema",
        "description": dedent("""
        Export the TAXII schema to use in other tooling.
        """)
    }

    @property
    def tags(self):
        return [self.value['name']]

    @classmethod
    def all(cls):
        return [v.value for v in cls.__members__.values()]

from drf_spectacular.settings import spectacular_settings
spectacular_settings.apply_patches({'TAGS': OpenApiTags.all()})



class CustomAutoSchema(AutoSchema):
    global_params = [
        OpenApiParameter(
            name="Accept",
            type=dict(enum=[conf.taxii_type]),
            location=OpenApiParameter.HEADER,
            required=True,
        ),
        OpenApiParameter(
            name="Content-Type",
            location=OpenApiParameter.HEADER,
            response=True,
            required=True,
            default=conf.taxii_type
        ),
    ]
    url_path_params = {
        'collection_id': OpenApiParameter('collection_id', type=str, location=OpenApiParameter.PATH, description="The identifier of the Collection being requested."),
        'api_root': OpenApiParameter('api_root', type=str, location=OpenApiParameter.PATH, description="The API Root name. Do not include the full URL."),
        'object_id': OpenApiParameter('object_id', type=str, location=OpenApiParameter.PATH, description="The STIX ID of the object being requested."),
        'status_id': OpenApiParameter('status_id', type=OpenApiTypes.UUID, location=OpenApiParameter.PATH, description="The ID of the object being requested"),
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
        return False
                

class ArangoServerAuthenticationScheme(OpenApiAuthenticationExtension):
    target_class = ArangoServerAuthentication
    name = "ArangoBasicAuth"
    priority = -1

    def get_security_definition(self, auto_schema):
        return {
            "type": "http",
            "scheme": "basic",
        }
