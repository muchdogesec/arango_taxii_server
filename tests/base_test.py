import unittest
import requests
import logging
from tests.test_variables import (USERS, BASE_URL, REQUEST_HEADERS, EXPECTED_RESPONSES)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.base_url = BASE_URL
        self.headers = REQUEST_HEADERS

    def check_response(self, method, url, expected_status, json=None, auth=None, test_number=None, test_label=None):
        logger.info(f"===TEST {test_number} ({test_label})===")
        if json:
            response = getattr(requests, method.lower())(url, headers=self.headers, json=json, auth=auth)
            logger.info(f"Request Body: {json}")
        else:
            response = getattr(requests, method.lower())(url, headers=self.headers, auth=auth)
        logger.info(f"URL: {url}")
        logger.info(f"Method: {method}")
        logger.info(f"User: {auth.username if auth else 'No credentials used'}")
        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")
        
        try:
            response_json = response.json()
            self.assertIn("title", response_json, "The response JSON should contain a 'title' field.")
        except requests.exceptions.JSONDecodeError:
            response_json = None

        self.assertEqual(response.status_code, expected_status["http_status"])

    def check_get_response(self, method, url, expected_status, auth=None, test_number=None, test_label=None):
        logger.info(f"===TEST {test_number}===")
        response = getattr(requests, method.lower())(url, headers=self.headers, auth=auth)
        logger.info(f"URL: {url}")
        logger.info(f"Method: {method}")
        logger.info(f"User: {auth.username if auth else 'No credentials used'}")
        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")
        self.assertEqual(response.status_code, expected_status["http_status"])
        response_json = response.json()
        objects = response_json.get("objects", [])
        logger.info(f"Objects: {objects}")
        self.assertEqual(objects, [], "Expected empty objects list in response")

    def check_get_response_with_body(self, method, url, expected_status, expected_body, auth=None, test_number=None, test_label=None):
        logger.info(f"===TEST {test_number}===")
        response = getattr(requests, method.lower())(url, headers=self.headers, auth=auth)
        logger.info(f"URL: {url}")
        logger.info(f"Method: {method}")
        logger.info(f"User: {auth.username if auth else 'No credentials used'}")
        logger.info(f"Status Code: {response.status_code}")
        logger.info(f"Response Body: {response.text}")
        self.assertEqual(response.status_code, expected_status["http_status"])
        response_json = response.json()
        self.assertEqual(response_json, expected_body, "Expected body does not match the response body")
