import unittest
import requests
from tests.test_variables import *
import base64

class TestReadUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.global_test_counter = 1

    def setUp(self):
        self.headers = REQUEST_HEADERS.copy()
        user_pass = f"read_write_user:{USERS['read_write_user']}"
        encoded_credentials = base64.b64encode(user_pass.encode()).decode('utf-8')
        self.headers['Authorization'] = f"Basic {encoded_credentials}"
        self.root_headers = REQUEST_HEADERS.copy()
        root_user_pass = f"root:{USERS['root']}"
        encoded_root_credentials = base64.b64encode(root_user_pass.encode()).decode('utf-8')
        self.root_headers['Authorization'] = f"Basic {encoded_root_credentials}"

    def log_response(self, test_num, url, headers, response, auth=None, request_body=None, method=None):
        print(f"============Test Number: {test_num}============")
        print(f"Request Method: {method}")
        print(f"Request URL: {url}")
        print(f"Request Headers: {headers}")
        if request_body:
            print(f"Request Body: {request_body}")
        if auth:
            print(f"Request Authentication Values: {auth}")
        print(f"Response HTTP Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Body: {response.text}")

    def check_response_headers(self, response):
        for key, value in RESPONSE_HEADERS.items():
            self.assertIn(key, response.headers)
            self.assertEqual(response.headers[key], value)

    def test_01_get_discover(self):
        url = URL_DISCOVER
        response = requests.get(url, headers=self.headers)
        self.log_response(self.global_test_counter, url, self.headers, response, auth="read_write_user", method="GET")
        self.check_response_headers(response)
        expected_body = {
            "title": "Arango TAXII Server",
            "description": "https://github.com/muchdogesec/arango_taxii_server/",
            "contact": "noreply@dogesec.com",
            "api_roots": [
                f"{BASE_URL}/api/taxii2/arango_taxii_server_tests_database/"
            ]
        }
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
        self.assertEqual(response.json(), expected_body, f"Expected {expected_body}, got {response.json()}")
        self.global_test_counter += 1

    def test_02_get_api_root(self):
        for api_root in API_ROOT:
            url = URL_API_ROOT.replace("{API_ROOT}", api_root)
            response = requests.get(url, headers=self.headers)
            self.log_response(self.global_test_counter, url, self.headers, response, auth="read_write_user", method="GET")
            self.check_response_headers(response)
            expected_body = {
                "max_content_length": 10485760,
                "title": "arango_taxii_server_tests_database",
                "versions": [
                    "application/stix+json;version=2.1"
                ]
            }
            self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
            self.assertEqual(response.json(), expected_body, f"Expected {expected_body}, got {response.json()}")
            self.global_test_counter += 1

    def test_03_get_collections_list(self):
        for api_root in API_ROOT:
            url = URL_COLLECTIONS_LIST.replace("{API_ROOT}", api_root)
            response = requests.get(url, headers=self.headers)
            self.log_response(self.global_test_counter, url, self.headers, response, auth="read_write_user", method="GET")
            self.check_response_headers(response)
            expected_body = {
                "collections": [
                    {
                        "id": "mitre_attack_enterprise",
                        "title": "mitre_attack_enterprise",
                        "description": "vertex+edge",
                        "can_read": True,
                        "can_write": True,
                        "media_types": [
                            "application/stix+json;version=2.1"
                        ]
                    },
                    {
                        "id": "mitre_attack_mobile",
                        "title": "mitre_attack_mobile",
                        "description": "vertex+edge",
                        "can_read": True,
                        "can_write": True,
                        "media_types": [
                            "application/stix+json;version=2.1"
                        ]
                    },
                    {
                        "id": "mitre_attack_ics",
                        "title": "mitre_attack_ics",
                        "description": "vertex+edge",
                        "can_read": True,
                        "can_write": True,
                        "media_types": [
                            "application/stix+json;version=2.1"
                        ]
                    }
                ]
            }
            self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
            self.assertEqual(response.json(), expected_body, f"Expected {expected_body}, got {response.json()}")
            self.global_test_counter += 1

    def test_04_get_collection(self):
        for api_root in API_ROOT:
            for collection_id in LIST_OF_COLLECTION_IDS:
                url = URL_COLLECTION.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id)
                response = requests.get(url, headers=self.headers)
                self.log_response(self.global_test_counter, url, self.headers, response, auth="read_write_user", method="GET")
                self.check_response_headers(response)
                expected_body = {
                    "id": collection_id,
                    "title": collection_id,
                    "description": "vertex+edge",
                    "can_read": True,
                    "can_write": True,
                        "media_types": [
                            "application/stix+json;version=2.1"
                        ]
                }
                self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
                self.assertEqual(response.json(), expected_body, f"Expected {expected_body}, got {response.json()}")
                self.global_test_counter += 1

    def test_05_get_collection_manifest(self):
        for api_root in API_ROOT:
            for collection_id in LIST_OF_COLLECTION_IDS:
                url = URL_COLLECTION_MANIFEST.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id)
                response = requests.get(url, headers=self.headers)
                self.log_response(self.global_test_counter, url, self.headers, response, auth="read_write_user", method="GET")
                self.check_response_headers(response)
                expected_body = response.json()
                self.assertTrue(expected_body.get('more'), "Expected 'more' to be true")
                self.assertEqual(len(expected_body.get('objects', [])), 50, "Expected exactly 50 objects")
                self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
                self.global_test_counter += 1

    def test_06_get_collection_objects(self):
        for api_root in API_ROOT:
            for collection_id in LIST_OF_COLLECTION_IDS:
                url = URL_COLLECTION_OBJECTS.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id)
                response = requests.get(url, headers=self.headers)
                self.log_response(self.global_test_counter, url, self.headers, response, auth="read_write_user", method="GET")
                self.check_response_headers(response)
                expected_body = response.json()
                self.assertTrue(expected_body.get('more'), "Expected 'more' to be true")
                self.assertEqual(len(expected_body.get('objects', [])), 50, "Expected exactly 50 objects")
                self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
                self.global_test_counter += 1

    def test_08_get_object(self):
        for api_root in API_ROOT:
            for object_info in VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_OBJECT_IDS:
                collection_id = "mitre_attack_enterprise"
                url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_info["id"])
                response = requests.get(url, headers=self.headers)
                self.log_response(self.global_test_counter, url, self.headers, response, auth="read_write_user", method="GET")
                self.check_response_headers(response)
                self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
                response_json = response.json()
                self.assertFalse(response_json.get('more'), "Expected 'more' to be false")
                self.assertEqual(len(response_json.get('objects', [])), 1, "Expected exactly 1 object")
                self.assertEqual(response_json["objects"][0]["id"], object_info["id"], f"Expected object ID {object_info['id']}")
                self.global_test_counter += 1

            for object_info in VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_RELATIONSHIP_IDS:
                collection_id = "mitre_attack_enterprise"
                url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_info["id"])
                response = requests.get(url, headers=self.headers)
                self.log_response(self.global_test_counter, url, self.headers, response, auth="read_write_user", method="GET")
                self.check_response_headers(response)
                self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
                response_json = response.json()
                self.assertFalse(response_json.get('more'), "Expected 'more' to be false")
                self.assertEqual(len(response_json.get('objects', [])), 1, "Expected exactly 1 object")
                self.assertEqual(response_json["objects"][0]["id"], object_info["id"], f"Expected object ID {object_info['id']}")
                self.global_test_counter += 1

            for object_info in VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_EMBEDDED_RELATIONSHIP_IDS:
                collection_id = "mitre_attack_enterprise"
                url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_info["id"])
                response = requests.get(url, headers=self.headers)
                self.log_response(self.global_test_counter, url, self.headers, response, auth="read_write_user", method="GET")
                self.check_response_headers(response)
                self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
                response_json = response.json()
                self.assertFalse(response_json.get('more'), "Expected 'more' to be false")
                self.assertEqual(len(response_json.get('objects', [])), 1, "Expected exactly 1 object")
                self.assertEqual(response_json["objects"][0]["id"], object_info["id"], f"Expected object ID {object_info['id']}")
                self.global_test_counter += 1

    def test_10_get_object_versions(self):
        for api_root in API_ROOT:
            for object_info in VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_OBJECT_IDS:
                collection_id = "mitre_attack_enterprise"
                url = URL_OBJECT_VERSIONS.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_info["id"])
                response = requests.get(url, headers=self.headers)
                self.log_response(self.global_test_counter, url, self.headers, response, auth="read_write_user", method="GET")
                self.check_response_headers(response)
                self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
                response_json = response.json()
                self.assertFalse(response_json.get('more'), "Expected 'more' to be false")
                self.assertEqual(response_json.get('versions', []), object_info["versions"], f"Expected versions {object_info['versions']}")
                self.global_test_counter += 1

            for object_info in VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_RELATIONSHIP_IDS:
                collection_id = "mitre_attack_enterprise"
                url = URL_OBJECT_VERSIONS.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_info["id"])
                response = requests.get(url, headers=self.headers)
                self.log_response(self.global_test_counter, url, self.headers, response, auth="read_write_user", method="GET")
                self.check_response_headers(response)
                self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
                response_json = response.json()
                self.assertFalse(response_json.get('more'), "Expected 'more' to be false")
                self.assertEqual(response_json.get('versions', []), object_info["versions"], f"Expected versions {object_info['versions']}")
                self.global_test_counter += 1

            for object_info in VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_EMBEDDED_RELATIONSHIP_IDS:
                collection_id = "mitre_attack_enterprise"
                url = URL_OBJECT_VERSIONS.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_info["id"])
                response = requests.get(url, headers=self.headers)
                self.log_response(self.global_test_counter, url, self.headers, response, auth="read_write_user", method="GET")
                self.check_response_headers(response)
                self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
                response_json = response.json()
                self.assertFalse(response_json.get('more'), "Expected 'more' to be false")
                self.assertEqual(response_json.get('versions', []), object_info["versions"], f"Expected versions {object_info['versions']}")
                self.global_test_counter += 1

    def test_11_get_status(self):
        for api_root in API_ROOT:
            url = URL_STATUS.replace("{API_ROOT}", api_root).replace("{STATUS_ID}", DUMMY_STATUS_ID)
            response = requests.get(url, headers=self.headers)
            self.log_response(self.global_test_counter, url, self.headers, response, auth="read_write_user", method="GET")
            self.check_response_headers(response)
            self.assertEqual(response.status_code, 404, f"Expected 404, got {response.status_code}")
            self.global_test_counter += 1

if __name__ == "__main__":
    unittest.main()
