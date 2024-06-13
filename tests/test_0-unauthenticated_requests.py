import unittest
import sys
import os

# Ensure the 'tests' directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.base_test import BaseTest, BASE_URL, API_ROOT, TAXII_ENDPOINTS, LIST_OF_COLLECTION_IDS, VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_OBJECT_IDS, VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_RELATIONSHIP_IDS, VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_EMBEDDED_RELATIONSHIP_IDS, EXPECTED_RESPONSES

def create_test_method(endpoint, method, url, expected_response):
    def test_method(self):
        print(f"Hitting endpoint: {url} with method: {method}")
        self.check_response(method, url, expected_response)
    return test_method

class UnauthenticatedRequestsTest(BaseTest):
    pass

expected_response = EXPECTED_RESPONSES["401"]
random_expected_response = EXPECTED_RESPONSES["401"]

# Add a random endpoint that should return 401
random_endpoint = {"endpoint": f"/api/taxii2/{API_ROOT}/does_not_exist", "method": "GET"}
endpoints_to_test = TAXII_ENDPOINTS

test_index = 0
for endpoint_data in endpoints_to_test:
    method = endpoint_data["method"]
    endpoint = endpoint_data["endpoint"]

    # Skip the status endpoint for unauthenticated tests
    if "status" in endpoint:
        continue

    for collection_id in LIST_OF_COLLECTION_IDS:
        formatted_endpoint = endpoint.replace("{COLLECTION_ID}", collection_id)

        object_ids = (VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_OBJECT_IDS +
                      VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_RELATIONSHIP_IDS +
                      VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_EMBEDDED_RELATIONSHIP_IDS)

        for obj in object_ids:
            final_endpoint = formatted_endpoint.replace("{OBJECT_ID}", obj["id"])
            url = f"{BASE_URL}{final_endpoint}"

            test_method = create_test_method(endpoint, method, url, expected_response)
            test_method.__name__ = f"test_{test_index}_{method}_{final_endpoint.replace('/', '_')}"
            setattr(UnauthenticatedRequestsTest, test_method.__name__, test_method)
            test_index += 1

# Also add the random endpoint separately
url = f"{BASE_URL}{random_endpoint['endpoint']}"
test_method = create_test_method(random_endpoint['endpoint'], random_endpoint['method'], url, random_expected_response)
test_method.__name__ = f"test_{test_index}_random_endpoint_{random_endpoint['method']}"
setattr(UnauthenticatedRequestsTest, test_method.__name__, test_method)

if __name__ == "__main__":
    unittest.main()
