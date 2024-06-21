import unittest
import requests
from tests.test_variables import *
import base64

class TestObjectParameters(unittest.TestCase):

    def setUp(self):
        self.headers = REQUEST_HEADERS.copy()
        user_pass = f"read_write_user:{USERS['read_write_user']}"
        encoded_credentials = base64.b64encode(user_pass.encode()).decode('utf-8')
        self.headers['Authorization'] = f"Basic {encoded_credentials}"
        self.test_counter = 0

    def log_response(self, test_name, test_num, url, headers, response, auth=None, method=None):
        print(f"Test Name: {test_name} | Test Number: {test_num}")
        print(f"Request Method: {method}")
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

    def check_taxii_date_added_headers(self, response, objects):
        date_added_first = response.headers.get('X-TAXII-Date-Added-First')
        date_added_last = response.headers.get('X-TAXII-Date-Added-Last')

        self.assertIsNotNone(date_added_first, "X-TAXII-Date-Added-First header is missing")
        self.assertIsNotNone(date_added_last, "X-TAXII-Date-Added-Last header is missing")

        dates_added = [obj['date_added'] for obj in objects]
        versions = [obj['version'] for obj in objects]

        self.assertEqual(date_added_first, min(dates_added), f"Expected {min(dates_added)}, got {date_added_first}")
        self.assertEqual(date_added_last, max(versions), f"Expected {max(versions)}, got {date_added_last}")

    def test_get_object_limit_1(self):
        test_name = 'test_get_object_limit_1'
        self.test_counter += 1
        api_root = API_ROOT[0]  # Using the first API root from the list
        collection_id = "mitre_attack_enterprise"
        object_id = "attack-pattern--ad255bfe-a9e6-4b52-a258-8d3462abe842"
        url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_id)
        params = {"limit": 1}

        response = requests.get(url, headers=self.headers, params=params)
        self.log_response(test_name, self.test_counter, response.url, self.headers, response, auth="read_write_user", method="GET")
        self.check_response_headers(response)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

        response_json = response.json()
        self.assertIn('objects', response_json, "Expected 'objects' key in response")
        self.assertEqual(len(response_json['objects']), 1, f"Expected 1 object, got {len(response_json['objects'])}")
        self.assertTrue(response_json.get('more'), "Expected 'more' to be true")

        self.check_taxii_date_added_headers(response, response_json['objects'])

    def test_get_object_limit_100(self):
        test_name = 'test_get_object_limit_100'
        self.test_counter += 1
        api_root = API_ROOT[0]  # Using the first API root from the list
        collection_id = "mitre_attack_enterprise"
        object_id = "attack-pattern--ad255bfe-a9e6-4b52-a258-8d3462abe842"
        url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_id)
        params = {"limit": 100}

        response = requests.get(url, headers=self.headers, params=params)
        self.log_response(test_name, self.test_counter, response.url, self.headers, response, auth="read_write_user", method="GET")
        self.check_response_headers(response)
        self.assertEqual(response.status_code, 400, f"Expected 400, got {response.status_code}")

    def test_get_object_type(self):
        test_name = 'test_get_object_type'
        self.test_counter += 1
        api_root = API_ROOT[0]  # Using the first API root from the list
        collection_id = "mitre_attack_enterprise"
        object_id = "attack-pattern--ad255bfe-a9e6-4b52-a258-8d3462abe842"
        url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_id)
        params = {"match[type]": "attack-pattern"}

        response = requests.get(url, headers=self.headers, params=params)
        self.log_response(test_name, self.test_counter, response.url, self.headers, response, auth="read_write_user", method="GET")
        self.check_response_headers(response)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

        response_json = response.json()
        self.assertIn('objects', response_json, "Expected 'objects' key in response")
        self.assertEqual(len(response_json['objects']), 1, f"Expected 1 object, got {len(response_json['objects'])}")
        self.assertFalse(response_json.get('more'), "Expected 'more' to be false")

        self.check_taxii_date_added_headers(response, response_json['objects'])

        for obj in response_json['objects']:
            self.assertIn('id', obj, "Expected 'id' key in object")
            self.assertIn('date_added', obj, "Expected 'date_added' key in object")
            self.assertIn('version', obj, "Expected 'version' key in object")
            self.assertTrue(obj['id'].startswith("attack-pattern--"), f"Unexpected id format: {obj['id']}")

    def test_get_object_match_id_single(self):
        test_name = 'test_get_object_match_id_single'
        self.test_counter += 1
        api_root = API_ROOT[0]  # Using the first API root from the list
        collection_id = "mitre_attack_enterprise"
        object_id = "attack-pattern--ad255bfe-a9e6-4b52-a258-8d3462abe842"
        url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_id)
        params = {"match[id]": object_id}

        response = requests.get(url, headers=self.headers, params=params)
        self.log_response(test_name, self.test_counter, response.url, self.headers, response, auth="read_write_user", method="GET")
        self.check_response_headers(response)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

        response_json = response.json()
        expected_body = {
            "more": False,
            "next": None,
            "objects": [
                {
                    "id": object_id,
                    "date_added": "2017-05-31T21:30:18.931Z",
                    "version": "2024-02-02T19:04:35.389Z",
                    "media_type": "application/stix+json;version=2.1"
                }
            ]
        }
        self.assertEqual(response_json, expected_body, f"Expected {expected_body}, got {response_json}")

        self.check_taxii_date_added_headers(response, response_json['objects'])

    def test_get_object_match_id_multiple(self):
        test_name = 'test_get_object_match_id_multiple'
        self.test_counter += 1
        api_root = API_ROOT[0]  # Using the first API root from the list
        collection_id = "mitre_attack_enterprise"
        object_ids = "attack-pattern--ad255bfe-a9e6-4b52-a258-8d3462abe842,tool--afc079f3-c0ea-4096-b75d-3f05338b7f60"
        url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_ids)
        params = {"match[id]": object_ids}

        response = requests.get(url, headers=self.headers, params=params)
        self.log_response(test_name, self.test_counter, response.url, self.headers, response, auth="read_write_user", method="GET")
        self.check_response_headers(response)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

        response_json = response.json()
        expected_body = {
            "more": False,
            "next": None,
            "objects": [
                {
                    "id": "attack-pattern--ad255bfe-a9e6-4b52-a258-8d3462abe842",
                    "date_added": "2017-05-31T21:30:18.931Z",
                    "version": "2024-02-02T19:04:35.389Z",
                    "media_type": "application/stix+json;version=2.1"
                },
                {
                    "id": "tool--afc079f3-c0ea-4096-b75d-3f05338b7f60",
                    "date_added": "2017-05-31T21:32:11.544Z",
                    "version": "2024-02-09T21:31:30.227Z",
                    "media_type": "application/stix+json;version=2.1"
                }
            ]
        }
        self.assertEqual(response_json, expected_body, f"Expected {expected_body}, got {response_json}")

        self.check_taxii_date_added_headers(response, response_json['objects'])

    def test_get_object_match_version_first(self):
        test_name = 'test_get_object_match_version_first'
        self.test_counter += 1
        api_root = API_ROOT[0]
        collection_id = "mitre_attack_enterprise"
        object_id = "attack-pattern--67720091-eee3-4d2d-ae16-8264567f6f5b"
        url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_id)
        params = {"match[version]": "first"}

        response = requests.get(url, headers=self.headers, params=params)
        self.log_response(test_name, self.test_counter, response.url, self.headers, response, auth="read_write_user", method="GET")
        self.check_response_headers(response)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

        response_json = response.json()
        expected_body = {
            "more": False,
            "next": None,
            "objects": [
                {
                    "id": object_id,
                    "date_added": "2020-01-30T13:58:14.373Z",
                    "version": "2023-10-02T00:47:11.369Z",
                    "media_type": "application/stix+json;version=2.1"
                }
            ]
        }
        self.assertEqual(response_json, expected_body, f"Expected {expected_body}, got {response_json}")

        self.check_taxii_date_added_headers(response, response_json['objects'])

    def test_get_object_match_version_last(self):
        test_name = 'test_get_object_match_version_last'
        self.test_counter += 1
        api_root = API_ROOT[0]
        collection_id = "mitre_attack_enterprise"
        object_id = "attack-pattern--67720091-eee3-4d2d-ae16-8264567f6f5b"
        url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_id)
        params = {"match[version]": "last"}

        response = requests.get(url, headers=self.headers, params=params)
        self.log_response(test_name, self.test_counter, response.url, self.headers, response, auth="read_write_user", method="GET")
        self.check_response_headers(response)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

        response_json = response.json()
        expected_body = {
            "more": False,
            "next": None,
            "objects": [
                {
                    "id": object_id,
                    "date_added": "2020-01-30T13:58:14.373Z",
                    "version": "2024-02-02T19:04:35.389Z",
                    "media_type": "application/stix+json;version=2.1"
                }
            ]
        }
        self.assertEqual(response_json, expected_body, f"Expected {expected_body}, got {response_json}")

        self.check_taxii_date_added_headers(response, response_json['objects'])

    def test_get_object_match_version_first_last(self):
        test_name = 'test_get_object_match_version_first_last'
        self.test_counter += 1
        api_root = API_ROOT[0]
        collection_id = "mitre_attack_enterprise"
        object_id = "attack-pattern--67720091-eee3-4d2d-ae16-8264567f6f5b"
        url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_id)
        params = {"match[version]": "first,last"}

        response = requests.get(url, headers=self.headers, params=params)
        self.log_response(test_name, self.test_counter, response.url, self.headers, response, auth="read_write_user", method="GET")
        self.check_response_headers(response)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

        response_json = response.json()
        expected_body = {
            "more": False,
            "next": None,
            "objects": [
                {
                    "id": object_id,
                    "date_added": "2020-01-30T13:58:14.373Z",
                    "version": "2024-02-02T19:04:35.389Z",
                    "media_type": "application/stix+json;version=2.1"
                },
                {
                    "id": object_id,
                    "date_added": "2020-01-30T13:58:14.373Z",
                    "version": "2023-10-02T00:47:11.369Z",
                    "media_type": "application/stix+json;version=2.1"
                }
            ]
        }
        self.assertEqual(response_json, expected_body, f"Expected {expected_body}, got {response_json}")

        self.check_taxii_date_added_headers(response, response_json['objects'])

    def test_get_object_match_version_specific(self):
        test_name = 'test_get_object_match_version_specific'
        self.test_counter += 1
        api_root = API_ROOT[0]
        collection_id = "mitre_attack_enterprise"
        object_id = "attack-pattern--67720091-eee3-4d2d-ae16-8264567f6f5b"
        url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_id)
        params = {"match[version]": "2024-02-02T19:04:35.389Z"}

        response = requests.get(url, headers=self.headers, params=params)
        self.log_response(test_name, self.test_counter, response.url, self.headers, response, auth="read_write_user", method="GET")
        self.check_response_headers(response)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

        response_json = response.json()
        expected_body = {
            "more": False,
            "next": None,
            "objects": [
                {
                    "id": object_id,
                    "date_added": "2020-01-30T13:58:14.373Z",
                    "version": "2024-02-02T19:04:35.389Z",
                    "media_type": "application/stix+json;version=2.1"
                }
            ]
        }
        self.assertEqual(response_json, expected_body, f"Expected {expected_body}, got {response_json}")

        self.check_taxii_date_added_headers(response, response_json['objects'])

    def test_get_object_match_version_all(self):
        test_name = 'test_get_object_match_version_all'
        self.test_counter += 1
        api_root = API_ROOT[0]
        collection_id = "mitre_attack_enterprise"
        object_id = "attack-pattern--67720091-eee3-4d2d-ae16-8264567f6f5b"
        url = URL_OBJECT.replace("{API_ROOT}", api_root).replace("{COLLECTION_ID}", collection_id).replace("{OBJECT_ID}", object_id)
        params = {"match[version]": "all"}

        response = requests.get(url, headers=self.headers, params=params)
        self.log_response(test_name, self.test_counter, response.url, self.headers, response, auth="read_write_user", method="GET")
        self.check_response_headers(response)
        self.assertEqual(response.status_code, 200, f"Expected 200, got {response.status_code}")

        response_json = response.json()
        expected_body = {
            "more": False,
            "next": None,
            "objects": [
                {
                    "id": object_id,
                    "date_added": "2020-01-30T13:58:14.373Z",
                    "version": "2024-02-02T19:04:35.389Z",
                    "media_type": "application/stix+json;version=2.1"
                },
                {
                    "id": object_id,
                    "date_added": "2020-01-30T13:58:14.373Z",
                    "version": "2023-10-02T00:47:11.369Z",
                    "media_type": "application/stix+json;version=2.1"
                }
            ]
        }
        self.assertEqual(response_json, expected_body, f"Expected {expected_body}, got {response_json}")

        self.check_taxii_date_added_headers(response, response_json['objects'])

if __name__ == "__main__":
    unittest.main()
