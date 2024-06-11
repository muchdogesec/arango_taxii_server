import unittest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8000"
AUTH = HTTPBasicAuth('no_access_user', 'testing123')
REQUEST_HEADERS = {'Accept': 'application/taxii+json;version=2.1'}
REQUEST_BAD_HEADER = {'Accept': 'application/json'}
EXPECTED_CONTENT_TYPE = "application/taxii+json;version=2.1"

EXPECTED_RESPONSE_BODY_1 = {
    "title": "Arango TAXII Server",
    "description": "https://github.com/muchdogesec/arango_taxii_server/",
    "contact": "noreply@dogesec.com",
    "api_roots": []
}

class TestTaxiiEndpoint(unittest.TestCase):

    def setUp(self):
        self.auth = AUTH
        self.headers = REQUEST_HEADERS
        self.bad_headers = REQUEST_BAD_HEADER
        self.expected_content_type = EXPECTED_CONTENT_TYPE
        self.base_url = BASE_URL

    def tearDown(self):
        pass

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
        self.assertEqual(response.headers['content-type'], self.expected_content_type, f"Expected Content-Type {self.expected_content_type}, but got {response.headers['content-type']}")

        # Assert that the response body matches the expected structure
        response_json = response.json()
        self.assertEqual(response_json, EXPECTED_RESPONSE_BODY_1, f"Expected response body {EXPECTED_RESPONSE_BODY_1}, but got {response_json}")

    def test_invalid_headers(self):
        url = f"{self.base_url}/api/taxii2/"
        try:
            response = requests.get(url, auth=self.auth, headers=self.bad_headers)
        except requests.RequestException as e:
            self.fail(f"Request to {url} failed with exception {e}")

        # Assert that the request fails with the wrong headers
        self.assertNotEqual(response.status_code, 200, f"Expected non-200 status code, but got {response.status_code}")

    def test_authentication_failure(self):
        invalid_auth = HTTPBasicAuth('invalid_user', 'invalid_pass')
        url = f"{self.base_url}/api/taxii2/"
        try:
            response = requests.get(url, auth=invalid_auth, headers=self.headers)
        except requests.RequestException as e:
            self.fail(f"Request to {url} failed with exception {e}")

        # Assert that the request fails with invalid authentication
        self.assertEqual(response.status_code, 401, f"Expected status code 401, but got {response.status_code}")

    def test_endpoint_not_found(self):
        url = f"{self.base_url}/api/taxii2/non_existing_endpoint"
        try:
            response = requests.get(url, auth=self.auth, headers=self.headers)
        except requests.RequestException as e:
            self.fail(f"Request to {url} failed with exception {e}")

        # Assert that the request returns a 404 status for a non-existing endpoint
        self.assertEqual(response.status_code, 404, f"Expected status code 404, but got {response.status_code}")

if __name__ == "__main__":
    unittest.main()

