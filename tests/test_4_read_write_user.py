import unittest
import requests
from tests.test_variables import *
import base64

class TestReadWriteUser(unittest.TestCase):

    def setUp(self):
        self.headers = REQUEST_HEADERS.copy()
        user_pass = f"read_write_user:{USERS['read_write_user']}"
        encoded_credentials = base64.b64encode(user_pass.encode()).decode('utf-8')
        self.headers['Authorization'] = f"Basic {encoded_credentials}"
        self.root_headers = REQUEST_HEADERS.copy()
        root_user_pass = f"root:{USERS['root']}"
        encoded_root_credentials = base64.b64encode(root_user_pass.encode()).decode('utf-8')
        self.root_headers['Authorization'] = f"Basic {encoded_root_credentials}"
        self.test_number = 0
        self.status_id = None

    def log_response(self, test_num, url, headers, response, auth=None):
        print(f"Test Number: {test_num}")
        print(f"Request URL: {url}")
        print(f"Request Headers: {headers}")
        if auth:
            print(f"Request Authentication Values: {auth}")
        print(f"Response HTTP Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Body: {response.text}")

    def check_response_headers(self, response):
        for key, value in RESPONSE_HEADERS.items():
            self.assertIn(key, response.headers)
            self.assertEqual(response.headers[key], value)

    def test_post_collection_objects(self):
        for api_root in API_ROOT:
            for collection_id in LIST_OF_COLLECTION_IDS:
                self.test_number += 1
                url = URL_COLLECTION_OBJECTS.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id)
                data = {
                    "objects": [DUMMY_OBJECT]
                }
                response = requests.post(url, headers=self.headers, json=data)
                self.log_response(self.test_number, url, self.headers, response, auth="read_write_user")
                self.check_response_headers(response)
                self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

                # Check the total_count and pending_count
                response_json = response.json()
                self.assertEqual(response_json["total_count"], 1, f"Expected total_count to be 1, got {response_json['total_count']}")
                self.assertEqual(response_json["pending_count"], 1, f"Expected pending_count to be 1, got {response_json['pending_count']}")

                # Store status_id for later use
                self.status_id = response_json["id"]

                # Verify that the object was added
                verification_url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", DUMMY_OBJECT_ID)
                verification_response = requests.get(verification_url, headers=self.root_headers)
                self.log_response(self.test_number, verification_url, self.root_headers, verification_response, auth="root")
                self.assertEqual(verification_response.status_code, 200, f"Expected 200, got {verification_response.status_code}")
                verification_response_json = verification_response.json()
                self.assertEqual(len(verification_response_json.get('objects', [])), 1, "Expected exactly 1 object")
                self.assertEqual(verification_response_json["objects"][0]["id"], DUMMY_OBJECT_ID, f"Expected object ID {DUMMY_OBJECT_ID}")

    def test_get_status(self):
        if self.status_id is None:
            self.skipTest("No status ID available from test_post_collection_objects")

        for api_root in API_ROOT:
            self.test_number += 1
            url = URL_STATUS.replace("{API_ROOT}", api_root).replace("{STATUS_ID}", self.status_id)
            response = requests.get(url, headers=self.headers)
            self.log_response(self.test_number, url, self.headers, response, auth="read_write_user")
            self.check_response_headers(response)
            self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

    # should delete all objects for id, because no filter applied
    def test_delete_object(self):
        for api_root in API_ROOT:
            for collection_id in LIST_OF_COLLECTION_IDS:
                self.test_number += 1
                url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", DUMMY_OBJECT_ID)
                response = requests.delete(url, headers=self.headers)
                self.log_response(self.test_number, url, self.headers, response, auth="read_write_user")
                self.check_response_headers(response)
                self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

                # Verify that the object was deleted
                verification_response = requests.get(url, headers=self.root_headers)
                self.log_response(self.test_number, url, self.root_headers, verification_response, auth="root")
                self.assertEqual(verification_response.status_code, 200, f"Expected 200, got {verification_response.status_code}")
                expected_verification_body = {
                    "more": False,
                    "next": None,
                    "objects": []
                }
                self.assertEqual(verification_response.json(), expected_verification_body, f"Expected {expected_verification_body}, got {verification_response.json()}")

if __name__ == "__main__":
    unittest.main()
