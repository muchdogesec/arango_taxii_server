import unittest
import sys
import os

# Ensure the 'tests' directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.base_test import BaseTest
from tests.test_variables import (BASE_URL, API_ROOT, TAXII_ENDPOINTS, LIST_OF_COLLECTION_IDS, 
                                  VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_OBJECT_IDS, 
                                  VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_RELATIONSHIP_IDS, 
                                  VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_EMBEDDED_RELATIONSHIP_IDS, 
                                  VALID_STIX_OBJECTS_FOR_POST, EXPECTED_RESPONSES, USERS)
from requests.auth import HTTPBasicAuth

def create_test_method(endpoint, method, url, expected_response, json=None, auth=None, test_number=None, test_label=None):
    def test_method(self):
        print(f"Hitting endpoint: {url} with method: {method}")
        self.check_response(method, url, expected_response, json=json, auth=auth, test_number=test_number, test_label=test_label)
    return test_method

def create_get_test_method(endpoint, method, url, expected_response, expected_body=None, auth=None, test_number=None, test_label=None):
    def test_method(self):
        print(f"Hitting endpoint: {url} with method: {method}")
        if expected_body:
            self.check_get_response(method, url, expected_response, expected_body, auth=auth, test_number=test_number, test_label=test_label)
        else:
            self.check_get_response_with_dynamic_body(method, url, expected_response, expected_body, auth=auth, test_number=test_number, test_label=test_label)
    return test_method

class ReadUserRequestsTest(BaseTest):
    pass

expected_response_200 = EXPECTED_RESPONSES["200"]
expected_response_404 = EXPECTED_RESPONSES["404"]
random_expected_response = EXPECTED_RESPONSES["404"]
auth = HTTPBasicAuth('read_user', USERS['read_user'])

# Specific expected body for the /api/taxii2/ endpoint
expected_body_taxii2 = {
    "title": "Arango TAXII Server",
    "description": "https://github.com/muchdogesec/arango_taxii_server/",
    "contact": "noreply@dogesec.com",
    "api_roots": [
        f"{BASE_URL}/api/taxii2/{API_ROOT}/"
    ]
}

# Specific expected body for the /api/taxii2/arango_taxii_server_tests_database/ endpoint
expected_body_api_root = {
    "max_content_length": 10485760,
    "title": "arango_taxii_server_tests_database",
    "versions": [
        "application/stix+json;version=2.1"
    ]
}

# Specific expected body for the /api/taxii2/arango_taxii_server_tests_database/collections/ endpoint
expected_body_collections = {
    "collections": [
        {
            "id": "mitre_attack_mobile",
            "title": "mitre_attack_mobile",
            "description": "vertex+edge",
            "can_read": True,
            "can_write": False,
            "media_types": [
                "application/stix+json;version=2.1"
            ]
        },
        {
            "id": "mitre_attack_enterprise",
            "title": "mitre_attack_enterprise",
            "description": "vertex+edge",
            "can_read": True,
            "can_write": False,
            "media_types": [
                "application/stix+json;version=2.1"
            ]
        },
        {
            "id": "mitre_attack_ics",
            "title": "mitre_attack_ics",
            "description": "vertex+edge",
            "can_read": True,
            "can_write": False,
            "media_types": [
                "application/stix+json;version=2.1"
            ]
        }
    ]
}

# Specific expected body for the /api/taxii2/arango_taxii_server_tests_database/collections/mitre_attack_enterprise/ endpoint
expected_body_collection = {
    "id": "mitre_attack_enterprise",
    "title": "mitre_attack_enterprise",
    "description": None,
    "can_read": True,
    "can_write": False
}

# Expected body for dynamic responses
expected_body_objects = {
    "more": True,
    "next": "<STRING>",
    "objects": []
}

# Add a random endpoint that should return 404
random_endpoint = {"endpoint": f"/api/taxii2/{API_ROOT}/does_not_exist/", "method": "GET"}
endpoints_to_test = TAXII_ENDPOINTS

test_index = 1
for endpoint_data in endpoints_to_test:
    method = endpoint_data["method"]
    endpoint = endpoint_data["endpoint"]

    # Skip the status endpoint for read user tests
    if "status" in endpoint:
        continue

    if endpoint == "/api/taxii2/" and method == "GET":
        url = f"{BASE_URL}{endpoint}"
        test_method = create_get_test_method(endpoint, method, url, expected_response_200, expected_body_taxii2, auth=auth, test_number=test_index, test_label="GET /api/taxii2/")
        test_method.__name__ = f"test_{test_index}_{method}_{endpoint.replace('/', '_')}"
        setattr(ReadUserRequestsTest, test_method.__name__, test_method)
        test_index += 1
        continue

    if endpoint == f"/api/taxii2/{API_ROOT}/" and method == "GET":
        url = f"{BASE_URL}{endpoint}"
        test_method = create_get_test_method(endpoint, method, url, expected_response_200, expected_body_api_root, auth=auth, test_number=test_index, test_label=f"GET {API_ROOT}")
        test_method.__name__ = f"test_{test_index}_{method}_{endpoint.replace('/', '_')}"
        setattr(ReadUserRequestsTest, test_method.__name__, test_method)
        test_index += 1
        continue

    if endpoint == f"/api/taxii2/{API_ROOT}/collections/" and method == "GET":
        url = f"{BASE_URL}{endpoint}"
        test_method = create_get_test_method(endpoint, method, url, expected_response_200, expected_body_collections, auth=auth, test_number=test_index, test_label="GET collections")
        test_method.__name__ = f"test_{test_index}_{method}_{endpoint.replace('/', '_')}"
        setattr(ReadUserRequestsTest, test_method.__name__, test_method)
        test_index += 1
        continue

    if endpoint == f"/api/taxii2/{API_ROOT}/collections/mitre_attack_enterprise/" and method == "GET":
        url = f"{BASE_URL}{endpoint}"
        test_method = create_get_test_method(endpoint, method, url, expected_response_200, expected_body_collection, auth=auth, test_number=test_index, test_label="GET mitre_attack_enterprise")
        test_method.__name__ = f"test_{test_index}_{method}_{endpoint.replace('/', '_')}"
        setattr(ReadUserRequestsTest, test_method.__name__, test_method)
        test_index += 1
        continue

    if (endpoint == f"/api/taxii2/{API_ROOT}/collections/mitre_attack_enterprise/objects/" and method == "GET") or (endpoint == f"/api/taxii2/{API_ROOT}/collections/mitre_attack_enterprise/manifest/" and method == "GET"):
        url = f"{BASE_URL}{endpoint}"
        test_method = create_get_test_method(endpoint, method, url, expected_response_200, expected_body_objects, auth=auth, test_number=test_index, test_label="GET objects or manifest")
        test_method.__name__ = f"test_{test_index}_{method}_{endpoint.replace('/', '_')}"
        setattr(ReadUserRequestsTest, test_method.__name__, test_method)
        test_index += 1
        continue

    for collection_id in LIST_OF_COLLECTION_IDS:
        formatted_endpoint = endpoint.replace("{COLLECTION_ID}", collection_id)

        if endpoint == f"/api/taxii2/{API_ROOT}/collections/{{COLLECTION_ID}}/objects/{{OBJECT_ID}}/" and method == "GET":
            object_ids = (VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_OBJECT_IDS +
                          VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_RELATIONSHIP_IDS +
                          VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_EMBEDDED_RELATIONSHIP_IDS)

            for obj in object_ids:
                final_endpoint = formatted_endpoint.replace("{OBJECT_ID}", obj["id"])
                url = f"{BASE_URL}{final_endpoint}"
                expected_body = {"id": obj["id"]}

                test_method = create_get_test_method(endpoint, method, url, expected_response_200, expected_body, auth=auth, test_number=test_index, test_label="GET specific object")
                test_method.__name__ = f"test_{test_index}_{method}_{final_endpoint.replace('/', '_')}"
                setattr(ReadUserRequestsTest, test_method.__name__, test_method)
                test_index += 1
            continue

# Also add the random endpoint separately
url = f"{BASE_URL}{random_endpoint['endpoint']}"
test_method = create_test_method(random_endpoint['endpoint'], random_endpoint['method'], url, random_expected_response, auth=auth, test_number=test_index, test_label="Random endpoint")
test_method.__name__ = f"test_{test_index}_random_endpoint_{random_endpoint['method']}"
setattr(ReadUserRequestsTest, test_method.__name__, test_method)

if __name__ == "__main__":
    unittest.main()
