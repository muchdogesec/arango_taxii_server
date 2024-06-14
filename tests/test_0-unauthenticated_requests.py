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
            self.check_get_response_with_body(method, url, expected_response, expected_body, auth=auth, test_number=test_number, test_label=test_label)
        else:
            self.check_get_response(method, url, expected_response, auth=auth, test_number=test_number, test_label=test_label)
    return test_method

class UnauthenticatedRequestsTest(BaseTest):
    pass

expected_response = EXPECTED_RESPONSES["401"]
random_expected_response = EXPECTED_RESPONSES["401"]

# Add a random endpoint that should return 401
random_endpoint = {"endpoint": f"/api/taxii2/{API_ROOT}/does_not_exist/", "method": "GET"}
endpoints_to_test = TAXII_ENDPOINTS

test_index = 1
for endpoint_data in endpoints_to_test:
    method = endpoint_data["method"]
    endpoint = endpoint_data["endpoint"]

    # Skip the status endpoint for unauthenticated tests
    if "status" in endpoint:
        continue

    for collection_id in LIST_OF_COLLECTION_IDS:
        formatted_endpoint = endpoint.replace("{COLLECTION_ID}", collection_id)

        if method == "POST" and collection_id == "mitre_attack_enterprise":
            url = f"{BASE_URL}{formatted_endpoint}"
            test_method = create_test_method(endpoint, method, url, expected_response, json=VALID_STIX_OBJECTS_FOR_POST, test_number=test_index, test_label="POST objects")
            test_method.__name__ = f"test_{test_index}_{method}_{formatted_endpoint.replace('/', '_')}"
            setattr(UnauthenticatedRequestsTest, test_method.__name__, test_method)
            test_index += 1

            # Add GET requests with root user to verify the objects were not created
            for obj in VALID_STIX_OBJECTS_FOR_POST[0]["objects"]:
                get_url = f"{BASE_URL}{formatted_endpoint}{obj['id']}/"
                get_auth = HTTPBasicAuth('root', USERS['root'])
                expected_body = {"more": False, "next": None, "objects": []}
                get_test_method = create_get_test_method(endpoint, "GET", get_url, EXPECTED_RESPONSES["200"], expected_body, auth=get_auth, test_number=test_index, test_label="Verify POST objects")
                get_test_method.__name__ = f"test_{test_index}_GET_{formatted_endpoint.replace('/', '_')}_{obj['id']}_verify"
                setattr(UnauthenticatedRequestsTest, get_test_method.__name__, get_test_method)
                test_index += 1

        elif method == "DELETE" and collection_id == "mitre_attack_enterprise":
            for obj in VALID_STIX_OBJECTS_FOR_POST[0]["objects"]:
                final_endpoint = formatted_endpoint.replace("{OBJECT_ID}", obj["id"])
                url = f"{BASE_URL}{final_endpoint}"

                delete_test_method = create_test_method(endpoint, method, url, expected_response, test_number=test_index, test_label="DELETE objects")
                delete_test_method.__name__ = f"test_{test_index}_{method}_{final_endpoint.replace('/', '_')}"
                setattr(UnauthenticatedRequestsTest, delete_test_method.__name__, delete_test_method)
                test_index += 1

                # Add a GET request with root user to verify the object was not deleted
                get_url = f"{BASE_URL}{final_endpoint}"
                get_auth = HTTPBasicAuth('root', USERS['root'])
                expected_body = {"more": False, "next": None, "objects": [{"id": obj["id"]}]}
                get_test_method = create_get_test_method(endpoint, "GET", get_url, EXPECTED_RESPONSES["200"], expected_body, auth=get_auth, test_number=test_index, test_label="Verify DELETE objects")
                get_test_method.__name__ = f"test_{test_index}_GET_{final_endpoint.replace('/', '_')}_verify"
                setattr(UnauthenticatedRequestsTest, get_test_method.__name__, get_test_method)
                test_index += 1
        else:
            object_ids = (VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_OBJECT_IDS +
                          VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_RELATIONSHIP_IDS +
                          VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_EMBEDDED_RELATIONSHIP_IDS)

            if collection_id == "mitre_attack_enterprise":
                for obj in object_ids:
                    final_endpoint = formatted_endpoint.replace("{OBJECT_ID}", obj["id"])
                    url = f"{BASE_URL}{final_endpoint}"

                    test_method = create_test_method(endpoint, method, url, expected_response, test_number=test_index, test_label="Generic GET/POST")
                    test_method.__name__ = f"test_{test_index}_{method}_{final_endpoint.replace('/', '_')}"
                    setattr(UnauthenticatedRequestsTest, test_method.__name__, test_method)
                    test_index += 1

# Also add the random endpoint separately
url = f"{BASE_URL}{random_endpoint['endpoint']}"
test_method = create_test_method(random_endpoint['endpoint'], random_endpoint['method'], url, random_expected_response, test_number=test_index, test_label="Random endpoint")
test_method.__name__ = f"test_{test_index}_random_endpoint_{random_endpoint['method']}"
setattr(UnauthenticatedRequestsTest, test_method.__name__, test_method)

if __name__ == "__main__":
    unittest.main()
