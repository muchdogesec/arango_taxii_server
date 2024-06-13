import unittest
import sys
import os

# Ensure the 'tests' directory is in the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from tests.base_test import BaseTest, TAXII_ENDPOINTS, LIST_OF_COLLECTION_IDS, VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_OBJECT_IDS, VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_RELATIONSHIP_IDS, VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_EMBEDDED_RELATIONSHIP_IDS, EXPECTED_RESPONSES

class UnauthenticatedRequestsTest(BaseTest):

    def test_endpoints_without_authentication(self):
        expected_response = EXPECTED_RESPONSES["401"]
        for endpoint_data in TAXII_ENDPOINTS:
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
                    url = f"{self.base_url}{final_endpoint}"

                    with self.subTest(method=method, url=url):
                        self.check_response(method, url, expected_response)

if __name__ == "__main__":
    unittest.main()
