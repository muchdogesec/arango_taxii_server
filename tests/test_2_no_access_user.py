import unittest
import requests
from .test_variables import *
import base64

class TestNoAccessUser(unittest.TestCase):

    def setUp(self):
        self.headers = HEADERS.copy()
        user_pass = f"no_access_user:{USERS['no_access_user']}"
        encoded_credentials = base64.b64encode(user_pass.encode()).decode('utf-8')
        self.headers['Authorization'] = f"Basic {encoded_credentials}"
        self.test_counter = 1

    def log_response(self, url, headers, response, auth=None):
        print(f"Test Number: {self.test_counter}")
        print(f"Request URL: {url}")
        print(f"Request Headers: {headers}")
        if auth:
            print(f"Request Authentication Values: {auth}")
        print(f"Response HTTP Code: {response.status_code}")
        print(f"Response Headers: {response.headers}")
        print(f"Response Body: {response.text}")
        self.test_counter += 1

    def test_get_schema(self):
        url = URL_SCHEMA
        response = requests.get(url, headers=self.headers)
        self.log_response(url, self.headers, response, auth="no_access_user")
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

    def test_get_discover(self):
        url = URL_DISCOVER
        response = requests.get(url, headers=self.headers)
        self.log_response(url, self.headers, response, auth="no_access_user")
        expected_body = {
            "title": "Arango TAXII Server",
            "description": "https://github.com/muchdogesec/arango_taxii_server/",
            "contact": "noreply@dogesec.com",
            "api_roots": []
        }
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")
        self.assertEqual(response.json(), expected_body, f"Expected {expected_body}, got {response.json()}")

    def test_get_api_root(self):
        for api_root in API_ROOT:
            url = URL_API_ROOT.replace("{API_ROOT}", api_root)
            response = requests.get(url, headers=self.headers)
            self.log_response(url, self.headers, response, auth="no_access_user")
            self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")

    def test_get_collections_list(self):
        for api_root in API_ROOT:
            url = URL_COLLECTIONS_LIST.replace("{API_ROOT}", api_root)
            response = requests.get(url, headers=self.headers)
            self.log_response(url, self.headers, response, auth="no_access_user")
            self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")

    def test_get_collection(self):
        for api_root in API_ROOT:
            for collection_id in LIST_OF_COLLECTION_IDS:
                url = URL_COLLECTION.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id)
                response = requests.get(url, headers=self.headers)
                self.log_response(url, self.headers, response, auth="no_access_user")
                self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")

    def test_get_collection_manifest(self):
        for api_root in API_ROOT:
            for collection_id in LIST_OF_COLLECTION_IDS:
                url = URL_COLLECTION_MANIFEST.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id)
                response = requests.get(url, headers=self.headers)
                self.log_response(url, self.headers, response, auth="no_access_user")
                self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")

    def test_get_collection_objects(self):
        for api_root in API_ROOT:
            for collection_id in LIST_OF_COLLECTION_IDS:
                url = URL_COLLECTION_OBJECTS.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id)
                response = requests.get(url, headers=self.headers)
                self.log_response(url, self.headers, response, auth="no_access_user")
                self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")

    def test_post_collection_objects(self):
        for api_root in API_ROOT:
            for collection_id in LIST_OF_COLLECTION_IDS:
                url = URL_COLLECTION_OBJECTS.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id)
                data = {
                    "objects": [DUMMY_OBJECT]
                }
                response = requests.post(url, headers=self.headers, json=data)
                self.log_response(url, self.headers, response, auth="no_access_user")
                self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")

    def test_get_object(self):
        for api_root in API_ROOT:
            for collection_id in LIST_OF_COLLECTION_IDS:
                url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", DUMMY_OBJECT_ID)
                response = requests.get(url, headers=self.headers)
                self.log_response(url, self.headers, response, auth="no_access_user")
                self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")

    def test_delete_object(self):
        for api_root in API_ROOT:
            for collection_id in LIST_OF_COLLECTION_IDS:
                url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", DUMMY_OBJECT_ID)
                response = requests.delete(url, headers=self.headers)
                self.log_response(url, self.headers, response, auth="no_access_user")
                self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")

    def test_get_object_versions(self):
        for api_root in API_ROOT:
            for collection_id in LIST_OF_COLLECTION_IDS:
                url = URL_OBJECT_VERSIONS.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", DUMMY_OBJECT_ID)
                response = requests.get(url, headers=self.headers)
                self.log_response(url, self.headers, response, auth="no_access_user")
                self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")

    def test_get_status(self):
        for api_root in API_ROOT:
            url = URL_STATUS.replace("{API_ROOT}", api_root).replace("{STATUS_ID}", DUMMY_STATUS_ID)
            response = requests.get(url, headers=self.headers)
            self.log_response(url, self.headers, response, auth="no_access_user")
            self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")

if __name__ == "__main__":
    unittest.main()
