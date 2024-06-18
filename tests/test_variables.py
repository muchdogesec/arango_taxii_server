# test_variables.py

BASE_URL = "http://127.0.0.1:8000"

# Users
USERS = {
    "read_write_user": "testing123", # this user has read/write permissions to collections in database arango_taxii_server_tests_database
    "read_user": "testing123", # this user has read permissions to collections in database arango_taxii_server_tests_database
    "no_access_user": "testing123", # this is a valid Arango account, but user has no permissions
    "bad_credentials_user": "blah", # this is not a valid Arango account
    "root": "" # this user has read/write permissions to all databases / collections
}

# Common headers
HEADERS = {
    "Content-Type": "application/taxii+json;version=2.1"
}

# API roots to use
API_ROOT = [
    "arango_taxii_server_tests_database"
]

# Collection IDs to use
LIST_OF_COLLECTION_IDS = [
    "mitre_attack_enterprise",
    "mitre_attack_ics",
    "mitre_attack_mobile"
]

# Dummy ID for unauthorized tests
DUMMY_STATUS_ID = "test_status_id"
DUMMY_OBJECT_ID = "dummy--b41e15b1-1595-4e4a-bb03-e6f48f7edafb"
DUMMY_OBJECT = {
    "type": "indicator",
    "spec_version": "2.1",
    "id": "dummy--b41e15b1-1595-4e4a-bb03-e6f48f7edafb",
    "created_by_ref": "identity--562918ee-d5da-5579-b6a1-fae50cc6bad3",
    "created": "2000-01-01T00:00:00.000Z",
    "modified": "2000-01-01T00:00:00.000Z",
    "name": "DUMMY OBJECT"
}

# URL endpoints
URL_SCHEMA = f"{BASE_URL}/api/schema/"
URL_DISCOVER = f"{BASE_URL}/api/taxii2/"
URL_API_ROOT = f"{BASE_URL}/api/taxii2/{{API_ROOT}}/"
URL_COLLECTIONS_LIST = f"{BASE_URL}/api/taxii2/{{API_ROOT}}/collections/"
URL_COLLECTION = f"{BASE_URL}/api/taxii2/{{API_ROOT}}/collections/{{COLLECTION_ID}}/"
URL_COLLECTION_MANIFEST = f"{BASE_URL}/api/taxii2/{{API_ROOT}}/collections/{{COLLECTION_ID}}/manifest/"
URL_COLLECTION_OBJECTS = f"{BASE_URL}/api/taxii2/{{API_ROOT}}/collections/{{COLLECTION_ID}}/objects/"
URL_OBJECT = f"{BASE_URL}/api/taxii2/{{API_ROOT}}/collections/{{COLLECTION_ID}}/objects/{{OBJECT_ID}}/"
URL_OBJECT_VERSIONS = f"{BASE_URL}/api/taxii2/{{API_ROOT}}/collections/{{COLLECTION_ID}}/objects/{{OBJECT_ID}}/versions/"
URL_STATUS = f"{BASE_URL}/api/taxii2/{{API_ROOT}}/status/{{STATUS_ID}}/"
