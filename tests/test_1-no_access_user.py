# python3 -m unittest tests/test_1-no_access_user.py

import unittest
import requests
from requests.auth import HTTPBasicAuth  # Add this import
from .base_test import BaseTest, API_ROOT, BAD_API_ROOT, EXPECTED_404_ERROR_RESPONSE, users

EXPECTED_RESPONSE_BODY_1 = {
    "title": "Arango TAXII Server",
    "description": "https://github.com/muchdogesec/arango_taxii_server/",
    "contact": "noreply@dogesec.com",
    "api_roots": []
}

class TestTaxiiEndpoint(BaseTest):

    def setUp(self):
        super().setUp()
        self.auth = HTTPBasicAuth('no_access_user', self.users['no_access_user'])

    # this test should return an empty response EXPECTED_RESPONSE_BODY_1 because this user has no access to any collections
    def test_taxii_root_endpoint(self):
        url = f"{self.base_url}/api/taxii2/"
        try:
            response = requests.get(url, auth=self.auth, headers=self.headers)
        except requests.RequestException as e:
            self.fail(f"Request to {url} failed with exception {e}")

        # Assert that the request was successful
        self.assertEqual(response.status_code, 200, f"Expected status code 200, but got {response.status_code}")

        # Assert that the Content-Type header is correct
        self.assertIn('content-type', response.headers, "Response headers missing 'content-type'")
        self.assertEqual(response.headers['content-type'], self.expected_RESPONSE_HEADER_content_type, f"Expected Content-Type {self.expected_RESPONSE_HEADER_content_type}, but got {response.headers['content-type']}")

        # Assert that the response body matches the expected structure
        response_json = response.json()
        self.assertEqual(response_json, EXPECTED_RESPONSE_BODY_1, f"Expected response body {EXPECTED_RESPONSE_BODY_1}, but got {response_json}")

    # this test should return a 404 EXPECTED_404_ERROR_RESPONSE because although this API_ROOT exists this user cannot see any collections
    def test_cti_database_endpoint(self):
        url = f"{self.base_url}/api/taxii2/{API_ROOT}/"
        try:
            response = requests.get(url, auth=self.auth, headers=self.headers)
        except requests.RequestException as e:
            self.fail(f"Request to {url} failed with exception {e}")

        # Assert that the request resulted in a 404 status code
        self.assertEqual(response.status_code, 404, f"Expected status code 404, but got {response.status_code}")

        # Assert that the response body matches the expected error structure
        response_json = response.json()
        self.assertEqual(response_json, EXPECTED_404_ERROR_RESPONSE, f"Expected response body {EXPECTED_404_ERROR_RESPONSE}, but got {response_json}")

    # this test should return a 404 EXPECTED_404_ERROR_RESPONSE because this collection does not exist on the server
    def test_cti_bad_api_root_endpoint(self):
        url = f"{self.base_url}/api/taxii2/{BAD_API_ROOT}/"
        try:
            response = requests.get(url, auth=self.auth, headers=self.headers)
        except requests.RequestException as e:
            self.fail(f"Request to {url} failed with exception {e}")

        # Assert that the request resulted in a 404 status code
        self.assertEqual(response.status_code, 404, f"Expected status code 404, but got {response.status_code}")

        # Assert that the response body matches the expected error structure
        response_json = response.json()
        self.assertEqual(response_json, EXPECTED_404_ERROR_RESPONSE, f"Expected response body {EXPECTED_404_ERROR_RESPONSE}, but got {response_json}")

    # this test should return a 404 EXPECTED_404_ERROR_RESPONSE because this collection does not exist on the server
    def test_arango_taxii_server_tests_collections_endpoint(self):
        url = f"{self.base_url}/api/taxii2/{API_ROOT}/collections/"
        try:
            response = requests.get(url, auth=self.auth, headers=self.headers)
        except requests.RequestException as e:
            self.fail(f"Request to {url} failed with exception {e}")

        # Assert that the request resulted in a 404 status code
        self.assertEqual(response.status_code, 404, f"Expected status code 404, but got {response.status_code}")

        # Assert that the response body matches the expected error structure
        response_json = response.json()
        self.assertEqual(response_json, EXPECTED_404_ERROR_RESPONSE, f"Expected response body {EXPECTED_404_ERROR_RESPONSE}, but got {response_json}")

if __name__ == "__main__":
    unittest.main()
