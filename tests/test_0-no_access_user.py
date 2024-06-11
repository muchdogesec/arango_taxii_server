import unittest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8000"
AUTH = HTTPBasicAuth('no_access_user', 'testing123')
HEADERS = {'Accept': 'application/taxii+json;version=2.1'}

EXPECTED_RESPONSE_BODY_1 = {
    "title": "Arango TAXII Server",
    "description": "https://github.com/muchdogesec/arango_taxii_server/",
    "contact": "noreply@dogesec.com",
    "api_roots": []
}
EXPECTED_RESPONSE_BODY_2 = {
    "title": "remote error: 1228 - database not found",
    "http_status": 404,
    "details": {
        "content": None
    }
}
EXPECTED_CONTENT_TYPE = "application/taxii+json;version=2.1"

class TestTaxiiEndpoint(unittest.TestCase):

    def setUp(self):
        self.auth = AUTH
        self.headers = HEADERS
        self.expected_content_type = EXPECTED_CONTENT_TYPE

    def tearDown(self):
        pass

    def test_taxii_root_endpoint(self):
        url = f"{BASE_URL}/api/taxii2/"
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

        # Print response body and headers for debugging purposes
        print("Response Body:", response_json)
        print("Response Headers:", response.headers)

    def test_taxii_collections_endpoint(self):
        url = f"{BASE_URL}/api/taxii2/arango_taxii_server_tests_database/collections/"
        try:
            response = requests.get(url, auth=self.auth, headers=self.headers)
        except requests.RequestException as e:
            self.fail(f"Request to {url} failed with exception {e}")

        # Assert that the request was unsuccessful (404 Not Found)
        self.assertEqual(response.status_code, 404, f"Expected status code 404, but got {response.status_code}")

        # Assert that the Content-Type header is correct
        self.assertIn('content-type', response.headers, "Response headers missing 'content-type'")
        self.assertEqual(response.headers['content-type'], self.expected_content_type, f"Expected Content-Type {self.expected_content_type}, but got {response.headers['content-type']}")

        # Assert that the response body matches the expected structure
        response_json = response.json()
        self.assertEqual(response_json, EXPECTED_RESPONSE_BODY_2, f"Expected response body {EXPECTED_RESPONSE_BODY_2}, but got {response_json}")

        # Print response body and headers for debugging purposes
        print("Response Body:", response_json)
        print("Response Headers:", response.headers)

if __name__ == "__main__":
    unittest.main()
