import unittest
import requests
from tests.test_variables import *
import base64

class BadCredentialsUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.global_test_counter = 1

    def setUp(self):
        self.headers = REQUEST_HEADERS.copy()
        user_pass = f"bad_credentials_user:{USERS['bad_credentials_user']}"
        encoded_credentials = base64.b64encode(user_pass.encode()).decode('utf-8')
        self.headers['Authorization'] = f"Basic {encoded_credentials}"
        self.root_headers = REQUEST_HEADERS.copy()
        root_user_pass = f"root:{USERS['root']}"
        encoded_root_credentials = base64.b64encode(root_user_pass.encode()).decode('utf-8')
        self.root_headers['Authorization'] = f"Basic {encoded_root_credentials}"

    def log_response(self, url, headers, response, auth=None, request_body=None):
        print(f"============Test Number: {self.__class__.global_test_counter}============")
        print(f"Request Method: {response.request.method}")
        print(f"Request URL: {url}")
        print(f"Request Headers: {headers}")
        if request_body:
            print(f"Request Body: {request_body}")
        if auth:
            print(f"Request Authentication Values: {auth}")
        print(f"Response HTTP Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Body: {response.text}")
        self.__class__.global_test_counter += 1

    def check_response_headers(self, response):
        for key, value in RESPONSE_HEADERS.items():
            self.assertIn(key, response.headers)
            self.assertEqual(response.headers[key], value)

    def test_01_get_schema(self):
        url = URL_SCHEMA
        response = requests.get(url, headers=REQUEST_SCHEMA_HEADERS)
        self.log_response(url, REQUEST_SCHEMA_HEADERS, response, auth="bad_credentials_user")
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

    def test_02_get_discover(self):
        url = URL_DISCOVER
        response = requests.get(url, headers=self.headers)
        self.log_response(url, self.headers, response, auth="bad_credentials_user")
        self.check_response_headers(response)
        self.assertEqual(response.status_code, 401, f"Expected 401, got {response.status_code}")

    def test_03_get_api_root(self):
        for api_root in API_ROOT:
            url = URL_API_ROOT.replace("{API_ROOT}", api_root)
            response = requests.get(url, headers=self.headers)
            self.log_response(url, self.headers, response, auth="bad_credentials_user")
            self.check_response_headers(response)
            self.assertEqual(response.status_code, 401, f"Expected 401, got {response.status_code}")

    def test_04_get_collections_list(self):
        for api_root in API_ROOT:
            url = URL_COLLECTIONS_LIST.replace("{API_ROOT}", api_root)
            response = requests.get(url, headers=self.headers)
            self.log_response(url, self.headers, response, auth="bad_credentials_user")
            self.check_response_headers(response)
            self.assertEqual(response.status_code, 404, f"Expected 401, got {response.status_code}")

    def test_05_get_collection(self):
        for api_root in API_ROOT:
            for collection_id in LIST_OF_COLLECTION_IDS:
                url = URL_COLLECTION.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id)
                response = requests.get(url, headers=self.headers)
                self.log_response(url, self.headers, response, auth="bad_credentials_user")
                self.check_response_headers(response)
                self.assertEqual(response.status_code, 404, f"Expected 404, got {response.status_code}")

    def test_06_get_collection_manifest(self):
        for api_root in API_ROOT:
            for collection_id in LIST_OF_COLLECTION_IDS:
                url = URL_COLLECTION_MANIFEST.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id)
                response = requests.get(url, headers=REQUEST_HEADERS_MANIFEST)
                self.log_response(url, REQUEST_HEADERS_MANIFEST, response, auth="bad_credentials_user")
                self.check_response_headers(response)
                self.assertEqual(response.status_code, 401, f"Expected 401, got {response.status_code}")

    def test_07_get_collection_objects(self):
        for api_root in API_ROOT:
            for collection_id in LIST_OF_COLLECTION_IDS:
                url = URL_COLLECTION_OBJECTS.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id)
                response = requests.get(url, headers=self.headers)
                self.log_response(url, self.headers, response, auth="bad_credentials_user")
                self.check_response_headers(response)
                self.assertEqual(response.status_code, 404, f"Expected 404, got {response.status_code}")

    def test_08_post_collection_objects(self):
        api_root = "arango_taxii_server_tests_database"
        url = URL_COLLECTION_OBJECTS.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", "mitre_attack_enterprise")
        data = {
            "objects": [DUMMY_OBJECT]
        }
        response = requests.post(url, headers={**self.headers, **POST_REQUEST_HEADERS}, json=data)
        self.log_response(url, self.headers, response, auth="bad_credentials_user", request_body=data)
        self.check_response_headers(response)
        self.assertEqual(response.status_code, 401, f"Expected 401, got {response.status_code}")

    def test_09_verify_post_collection_objects(self):
        api_root = "arango_taxii_server_tests_database"
        verification_url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", "mitre_attack_enterprise").replace("{OBJECT_ID}", DUMMY_OBJECT_ID)
        verification_response = requests.get(verification_url, headers=self.root_headers)
        self.log_response(verification_url, self.root_headers, verification_response, auth="root")
        expected_verification_body = {
            "more": False,
            "next": None,
            "objects": []
        }
        self.assertEqual(verification_response.status_code, 200, f"Expected 200, got {verification_response.status_code}")
        self.assertEqual(verification_response.json(), expected_verification_body, f"Expected {expected_verification_body}, got {verification_response.json()}")

    def test_10_get_object(self):
        api_root = "arango_taxii_server_tests_database"
        object_ids = {
            "mitre_attack_enterprise": "attack-pattern--1126cab1-c700-412f-a510-61f4937bb096",
            "mitre_attack_ics": "attack-pattern--1c5cf58c-a34a-40d7-82f4-f987cdfc2b91",
            "mitre_attack_mobile": "attack-pattern--00290ac5-551e-44aa-bbd8-c4b913488a6d"
        }
        for collection_id, object_id in object_ids.items():
            url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_id)
            response = requests.get(url, headers=self.headers)
            self.log_response(url, self.headers, response, auth="bad_credentials_user")
            self.check_response_headers(response)
            self.assertEqual(response.status_code, 404, f"Expected 404, got {response.status_code}")

    def test_11_delete_object(self):
        api_root = "arango_taxii_server_tests_database"
        object_ids = {
            "mitre_attack_enterprise": "attack-pattern--1126cab1-c700-412f-a510-61f4937bb096",
            "mitre_attack_ics": "attack-pattern--1c5cf58c-a34a-40d7-82f4-f987cdfc2b91",
            "mitre_attack_mobile": "attack-pattern--00290ac5-551e-44aa-bbd8-c4b913488a6d"
        }
        for collection_id, object_id in object_ids.items():
            url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_id)
            response = requests.delete(url, headers=self.headers)
            self.log_response(url, self.headers, response, auth="bad_credentials_user")
            self.check_response_headers(response)
            self.assertEqual(response.status_code, 404, f"Expected 404, got {response.status_code}")

    def test_12_verify_delete_object(self):
        api_root = "arango_taxii_server_tests_database"
        object_ids = {
            "mitre_attack_enterprise": "attack-pattern--1126cab1-c700-412f-a510-61f4937bb096",
            "mitre_attack_ics": "attack-pattern--1c5cf58c-a34a-40d7-82f4-f987cdfc2b91",
            "mitre_attack_mobile": "attack-pattern--00290ac5-551e-44aa-bbd8-c4b913488a6d"
        }
        for collection_id, object_id in object_ids.items():
            verification_url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_id)
            verification_response = requests.get(verification_url, headers=self.root_headers)
            self.log_response(verification_url, self.root_headers, verification_response, auth="root")
            self.assertEqual(verification_response.status_code, 200, f"Expected 200, got {verification_response.status_code}")
            response_json = verification_response.json()
            self.assertFalse(response_json.get('more'), "Expected 'more' to be false")
            self.assertGreater(len(response_json.get('objects', [])), 0, "Expected more than 1 object in the response")

    def test_13_get_object_versions(self):
        api_root = "arango_taxii_server_tests_database"
        object_ids = {
            "mitre_attack_enterprise": "attack-pattern--1126cab1-c700-412f-a510-61f4937bb096",
            "mitre_attack_ics": "attack-pattern--1c5cf58c-a34a-40d7-82f4-f987cdfc2b91",
            "mitre_attack_mobile": "attack-pattern--00290ac5-551e-44aa-bbd8-c4b913488a6d"
        }
        for collection_id, object_id in object_ids.items():
            url = URL_OBJECT_VERSIONS.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_id)
            response = requests.get(url, headers=self.headers)
            self.log_response(url, self.headers, response, auth="bad_credentials_user")
            self.check_response_headers(response)
            self.assertEqual(response.status_code, 404, f"Expected 404, got {response.status_code}")

    def test_14_get_status(self):
        for api_root in API_ROOT:
            url = URL_STATUS.replace("{API_ROOT}", api_root).replace("{STATUS_ID}", DUMMY_STATUS_ID)
            response = requests.get(url, headers=self.headers)
            self.log_response(url, self.headers, response, auth="bad_credentials_user")
            self.check_response_headers(response)
            self.assertEqual(response.status_code, 401, f"Expected 401, got {response.status_code}")

if __name__ == "__main__":
    unittest.main()
