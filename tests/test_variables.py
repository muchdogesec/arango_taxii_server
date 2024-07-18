# test_variables.py
import os


BASE_URL = "http://127.0.0.1:8000"

# Users
USERS = {
    "read_write_user": "testing123",  # this user has read/write permissions to collections in database arango_taxii_server_tests_database
    "read_user": "testing123",  # this user has read permissions to collections in database arango_taxii_server_tests_database
    "no_access_user": "testing123",  # this is a valid Arango account, but user has no permissions
    "bad_credentials_user": "blah",  # this is not a valid Arango account
    "root": "",  # this user has read/write permissions to all databases / collections
}

# Common headers
REQUEST_HEADERS = {"Accept": "application/taxii+json;version=2.1"}

POST_REQUEST_HEADERS = {
    "Content-Type": "application/taxii+json;version=2.1",
}

REQUEST_HEADERS_MANIFEST = {
    "Accept": "application/taxii+json;version=2.1,application/stix+json;version=2.1"
}

REQUEST_SCHEMA_HEADERS = {"accept": "application/vnd.oai.openapi"}

RESPONSE_HEADERS = {"Content-Type": "application/taxii+json;version=2.1"}

# API roots to use
API_ROOT = ["arango_taxii_server_tests_database"]

# Collection IDs to use
LIST_OF_COLLECTION_IDS = [
    "mitre_attack_enterprise",
    "mitre_attack_ics",
    "mitre_attack_mobile",
]

ENTERPRISE_OBJECT_ID = "attack-pattern--1126cab1-c700-412f-a510-61f4937bb096"
ICS_OBJECT_ID = "attack-pattern--1c5cf58c-a34a-40d7-82f4-f987cdfc2b91"
MOBILE_OBJECT_ID = "attack-pattern--00290ac5-551e-44aa-bbd8-c4b913488a6d"
# Objects

VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_OBJECT_IDS = [
    {
        "id": "attack-pattern--2bce5b30-7014-4a5d-ade7-12913fe6ac36",
        "versions": ["2021-04-29T14:49:39.188Z"],
    },
    {
        "id": "attack-pattern--67720091-eee3-4d2d-ae16-8264567f6f5b",
        "versions": ["2023-10-02T00:47:11.369Z", "2024-04-15T20:52:09.908Z"],
    },
    {
        "id": "tool--30489451-5886-4c46-90c9-0dff9adc5252",
        "versions": ["2023-07-25T19:24:08.305Z"],
    },
]

VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_RELATIONSHIP_IDS = [
    {
        "id": "relationship--00038d0e-7fc7-41c3-9055-edb4d87ea912",
        "versions": ["2021-04-27T01:56:35.810Z"],
    },
    {
        "id": "relationship--00192a5f-9dc0-445a-b010-d77bd08aac93",
        "versions": ["2021-06-08T13:29:06.838Z"],
    },
]

VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_EMBEDDED_RELATIONSHIP_IDS = [
    {
        "id": "relationship--cf2fdad6-76ad-5521-b6a0-3671ad1892b7",
        "versions": [
            "2023-11-14T14:00:00.188Z",
            "2024-04-23T14:00:00.188Z",
            "2024-05-02T14:00:00.188Z",
        ],
    },
    {
        "id": "relationship--a0a48703-e7e8-55d5-bcf3-f524b9ada4e9",
        "versions": ["2023-03-30T21:01:39.967Z"],
    },
]

# Dummy ID for unauthorized tests
DUMMY_STATUS_ID = "fake-id--a668e98c-84fa-4b76-b20a-4a880e20d62c"
DUMMY_OBJECT_ID = "dummy--b41e15b1-1595-4e4a-bb03-e6f48f7edafb"
DUMMY_OBJECT = {
    "type": "dummy",
    "spec_version": "2.1",
    "id": "dummy--b41e15b1-1595-4e4a-bb03-e6f48f7edafb",
    "created_by_ref": "identity--562918ee-d5da-5579-b6a1-fae50cc6bad3",
    "created": "2000-01-01T00:00:00.000Z",
    "modified": "2000-01-01T00:00:00.000Z",
    "name": "DUMMY OBJECT 1",
    "description": "Added first",
}
DUMMY_OBJECT_2 = {
    "type": "dummy",
    "spec_version": "2.1",
    "id": "dummy--b41e15b1-1595-4e4a-bb03-e6f48f7edafb",
    "created_by_ref": "identity--5edfebc9-331c-4264-a5bb-411a72089d41",
    "created": "2000-01-01T00:00:00.000Z",
    "modified": "2001-01-01T00:00:00.000Z",
    "name": "DUMMY OBJECT 2",
    "description": "Added second",
}
DUMMY_OBJECT_3 = {
    "type": "dummy",
    "spec_version": "2.1",
    "id": "dummy--b41e15b1-1595-4e4a-bb03-e6f48f7edafb",
    "created_by_ref": "identity--5edfebc9-331c-4264-a5bb-411a72089d41",
    "created": "2000-01-01T00:00:00.000Z",
    "modified": "2002-01-01T00:00:00.000Z",
    "name": "DUMMY OBJECT 3",
    "description": "Added third",
}

# URL endpoints
URL_SCHEMA = f"{BASE_URL}/api/schema/"
URL_DISCOVER = f"{BASE_URL}/api/taxii2/"
URL_API_ROOT = f"{BASE_URL}/api/taxii2/{{API_ROOT}}/"
URL_COLLECTIONS_LIST = f"{BASE_URL}/api/taxii2/{{API_ROOT}}/collections/"
URL_COLLECTION = f"{BASE_URL}/api/taxii2/{{API_ROOT}}/collections/{{COLLECTION_ID}}/"
URL_COLLECTION_MANIFEST = (
    f"{BASE_URL}/api/taxii2/{{API_ROOT}}/collections/{{COLLECTION_ID}}/manifest/"
)
URL_COLLECTION_OBJECTS = (
    f"{BASE_URL}/api/taxii2/{{API_ROOT}}/collections/{{COLLECTION_ID}}/objects/"
)
URL_OBJECT = f"{BASE_URL}/api/taxii2/{{API_ROOT}}/collections/{{COLLECTION_ID}}/objects/{{OBJECT_ID}}/"
URL_OBJECT_VERSIONS = f"{BASE_URL}/api/taxii2/{{API_ROOT}}/collections/{{COLLECTION_ID}}/objects/{{OBJECT_ID}}/versions/"
URL_STATUS = f"{BASE_URL}/api/taxii2/{{API_ROOT}}/status/{{STATUS_ID}}/"
