import unittest
import requests
import time
from tests.test_variables import *
import base64

class TestReadWriteUser(unittest.TestCase):

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
        self.status_id = None
        self.status_check_passed = True

    def log_response(self, url, headers, response, auth=None, request_body=None, method=None):
        print(f"============Test Number: {self.__class__.global_test_counter}============")
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
        self.__class__.global_test_counter += 1

    def check_response_headers(self, response):
        for key, value in RESPONSE_HEADERS.items():
            self.assertIn(key, response.headers)
            self.assertEqual(response.headers[key], value)

    def test_01_post_collection_objects(self):
        for api_root in API_ROOT:
            collection_id = "dummy_post"
            url = URL_COLLECTION_OBJECTS.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id)
            data = {
                "objects": [DUMMY_OBJECT, DUMMY_OBJECT_2, DUMMY_OBJECT_3]
            }
            response = requests.post(url, headers=self.headers, json=data)
            self.log_response(url, self.headers, response, auth="read_write_user", request_body=data, method="POST")
            self.check_response_headers(response)
            self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

            # Check the total_count and pending_count
            response_json = response.json()
            self.assertEqual(response_json["total_count"], 3, f"Expected total_count to be 3, got {response_json['total_count']}")
            self.assertEqual(response_json["pending_count"], 3, f"Expected pending_count to be 3, got {response_json['pending_count']}")

            # Store status_id for later use
            self.status_id = response_json["id"]

            # Wait for 5 seconds before verifying
            time.sleep(5)

            # Verify that the objects were added
            verification_url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", DUMMY_OBJECT_ID) + "?match[version]=all"
            verification_response = requests.get(verification_url, headers=self.root_headers)
            self.log_response(verification_url, self.root_headers, verification_response, auth="root", method="GET")
            self.assertEqual(verification_response.status_code, 200, f"Expected 200, got {verification_response.status_code}")
            verification_response_json = verification_response.json()
            self.assertEqual(len(verification_response_json.get('objects', [])), 3, "Expected exactly 3 objects")
            for obj in verification_response_json["objects"]:
                self.assertEqual(obj["id"], DUMMY_OBJECT_ID, f"Expected object ID {DUMMY_OBJECT_ID}")

    def test_02_get_status(self):
        if self.status_id is None:
            self.skipTest("No status ID available from test_post_collection_objects")

        time.sleep(5)  # Wait for 5 seconds before checking status

        for api_root in API_ROOT:
            url = URL_STATUS.replace("{API_ROOT}", api_root).replace("{STATUS_ID}", self.status_id)
            response = requests.get(url, headers=self.headers)
            self.log_response(url, self.headers, response, auth="read_write_user", method="GET")
            self.check_response_headers(response)
            self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

            response_json = response.json()
            if response_json.get("pending_count") != 0 or response_json.get("success_count") != 3:
                self.status_check_passed = False
                self.fail(f"Expected pending_count = 0 and success_count = 3, got {response_json}")

    def test_03_delete_object_by_version(self):
        if not self.status_check_passed:
            self.skipTest("Skipping test_delete_object due to failed status check in test_get_status")

        for api_root in API_ROOT:
            collection_id = "dummy_post"
            # Delete object with version filter
            url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", DUMMY_OBJECT_ID) + "?match[version]=2002-01-01T00:00:00.000Z"
            response = requests.delete(url, headers=self.headers)
            self.log_response(url, self.headers, response, auth="read_write_user", method="DELETE")
            self.check_response_headers(response)
            self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

    def test_04_verify_delete_object_by_version(self):
        if not self.status_check_passed:
            self.skipTest("Skipping test_verify_delete_object_by_version due to failed status check in test_get_status")

        for api_root in API_ROOT:
            collection_id = "dummy_post"
            # Verify that 2 objects remain
            verification_url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", DUMMY_OBJECT_ID) + "?match[version]=all"
            verification_response = requests.get(verification_url, headers=self.root_headers)
            self.log_response(verification_url, self.root_headers, verification_response, auth="root", method="GET")
            self.assertEqual(verification_response.status_code, 200, f"Expected 200, got {verification_response.status_code}")
            verification_response_json = verification_response.json()
            remaining_objects = [obj for obj in verification_response_json.get('objects', []) if obj["id"] == DUMMY_OBJECT_ID]
            self.assertEqual(len(remaining_objects), 2, "Expected exactly 2 objects")
            if len(remaining_objects) != 2:
                self.status_check_passed = False
                self.fail(f"Expected exactly 2 objects, got {len(remaining_objects)}")

    def test_05_delete_all_objects(self):
        if not self.status_check_passed:
            self.skipTest("Skipping test_delete_all_objects due to failed status check in test_verify_delete_object_by_version")

        for api_root in API_ROOT:
            collection_id = "dummy_post"
            # Delete all versions of the object
            url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", DUMMY_OBJECT_ID)
            response = requests.delete(url, headers=self.headers)
            self.log_response(url, self.headers, response, auth="read_write_user", method="DELETE")
            self.check_response_headers(response)
            self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

    def test_06_verify_delete_all_objects(self):
        if not self.status_check_passed:
            self.skipTest("Skipping test_verify_delete_all_objects due to failed status check in test_verify_delete_object_by_version")

        for api_root in API_ROOT:
            collection_id = "dummy_post"
            # Verify that no objects remain
            url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", DUMMY_OBJECT_ID)
            verification_response = requests.get(url + "?match[version]=all", headers=self.root_headers)
            self.log_response(url, self.root_headers, verification_response, auth="root", method="GET")
            self.assertEqual(verification_response.status_code, 200, f"Expected 200, got {verification_response.status_code}")
            expected_verification_body = {
                "more": False,
                "next": None,
                "objects": []
            }
            self.assertEqual(verification_response.json(), expected_verification_body, f"Expected {expected_verification_body}, got {verification_response.json()}")

    def test_07_post_collection_objects_again(self):
        self.test_01_post_collection_objects()

    def test_08_get_status_again(self):
        self.test_02_get_status()

    def test_09_delete_object_by_spec_version_invalid(self):
        if not self.status_check_passed:
            self.skipTest("Skipping test_delete_object_by_spec_version_invalid due to failed status check in test_get_status")

        for api_root in API_ROOT:
            collection_id = "dummy_post"
            # Delete object with spec_version filter (invalid version)
            url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", DUMMY_OBJECT_ID) + "?match[spec_version]=2.0"
            response = requests.delete(url, headers=self.headers)
            self.log_response(url, self.headers, response, auth="read_write_user", method="DELETE")
            self.check_response_headers(response)
            self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")

    def test_10_verify_delete_object_by_spec_version_invalid(self):
        if not self.status_check_passed:
            self.skipTest("Skipping test_verify_delete_object_by_spec_version_invalid due to failed status check in test_get_status")

        for api_root in API_ROOT:
            collection_id = "dummy_post"
            # Verify that 3 objects remain
            verification_url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", DUMMY_OBJECT_ID) + "?match[version]=all"
            verification_response = requests.get(verification_url, headers=self.root_headers)
            self.log_response(verification_url, self.root_headers, verification_response, auth="root", method="GET")
            self.assertEqual(verification_response.status_code, 200, f"Expected 200, got {verification_response.status_code}")
            verification_response_json = verification_response.json()
            remaining_objects = [obj for obj in verification_response_json.get('objects', []) if obj["id"] == DUMMY_OBJECT_ID]
            self.assertEqual(len(remaining_objects), 3, "Expected exactly 3 objects")
            if len(remaining_objects) != 3:
                self.status_check_passed = False
                self.fail(f"Expected exactly 3 objects, got {len(remaining_objects)}")

    def test_11_delete_object_by_spec_version_valid(self):
        if not self.status_check_passed:
            self.skipTest("Skipping test_delete_object_by_spec_version_valid due to failed status check in test_get_status")

        for api_root in API_ROOT:
            collection_id = "dummy_post"
            # Delete object with spec_version filter (valid version)
            url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", DUMMY_OBJECT_ID) + "?match[spec_version]=2.1"
            response = requests.delete(url, headers=self.headers)
            self.log_response(url, self.headers, response, auth="read_write_user", method="DELETE")
            self.check_response_headers(response)
            self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

    def test_12_verify_delete_object_by_spec_version_valid(self):
        if not self.status_check_passed:
            self.skipTest("Skipping test_verify_delete_object_by_spec_version_valid due to failed status check in test_get_status")

        for api_root in API_ROOT:
            collection_id = "dummy_post"
            # Verify that no objects remain
            url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", DUMMY_OBJECT_ID)
            verification_response = requests.get(url + "?match[version]=all", headers=self.root_headers)
            self.log_response(url, self.root_headers, verification_response, auth="root", method="GET")
            self.assertEqual(verification_response.status_code, 200, f"Expected 200, got {verification_response.status_code}")
            expected_verification_body = {
                "more": False,
                "next": None,
                "objects": []
            }
            self.assertEqual(verification_response.json(), expected_verification_body, f"Expected {expected_verification_body}, got {verification_response.json()}")

if __name__ == "__main__":
    unittest.main()
