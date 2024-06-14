import unittest
import requests
import logging

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

USERS = {
    "read_write_user": "testing123",
    "read_user": "testing123",
    "no_access_user": "testing123",
    "bad_permission_user": "testing123",
    "root": ""
}

BASE_URL = "http://127.0.0.1:8000"
REQUEST_HEADERS = {'Accept': 'application/taxii+json;version=2.1'}
EXPECTED_RESPONSE_HEADER_CONTENT_TYPE = "application/taxii+json;version=2.1"

API_ROOT = "arango_taxii_server_tests_database"

LIST_OF_COLLECTION_IDS = [
    "mitre_attack_enterprise",
    "mitre_attack_ics",
    "mitre_attack_mobile"
]

VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_OBJECT_IDS = [
    { 
        "id": "attack-pattern--2bce5b30-7014-4a5d-ade7-12913fe6ac36",
        "versions": ["2020-03-29T21:23:51.886Z"]
    },
    { 
        "id": "attack-pattern--67720091-eee3-4d2d-ae16-8264567f6f5b",
        "versions": ["2023-10-02T00:47:11.369Z", "2024-04-15T20:52:09.908Z"]
    },
    {
        "id": "tool--30489451-5886-4c46-90c9-0dff9adc5252",
        "versions": ["2023-07-25T19:24:08.305Z"]
    }
]

VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_RELATIONSHIP_IDS = [
    { 
        "id": "relationship--00038d0e-7fc7-41c3-9055-edb4d87ea912",
        "versions": ["2021-04-27T01:56:35.810Z"]
    },
    {
        "id": "relationship--00192a5f-9dc0-445a-b010-d77bd08aac93",
        "versions": ["2021-06-08T13:29:06.838Z"]
    }
]

VALID_MITRE_ATTACK_ENTERPRISE_COLLECTION_EMBEDDED_RELATIONSHIP_IDS = [
    { 
        "id": "relationship--cf2fdad6-76ad-5521-b6a0-3671ad1892b7",
        "versions": ["2023-11-14T14:00:00.188Z", "2024-04-23T14:00:00.188Z", "2024-05-02T14:00:00.188Z"]
    },
    {
        "id": "relationship--a0a48703-e7e8-55d5-bcf3-f524b9ada4e9",
        "versions": ["2023-03-30T21:01:39.967Z"]
    }
]

VALID_STIX_OBJECTS_FOR_POST = [
    {
        "objects": [
            {
                "type": "indicator",
                "spec_version": "2.1",
                "id": "indicator--adb149cb-dac4-5e81-b6c3-f7354477a1df",
                "created_by_ref": "identity--562918ee-d5da-5579-b6a1-fae50cc6bad3",
                "created": "2002-07-23T04:00:00.000Z",
                "modified": "2008-09-05T20:28:38.523Z",
                "name": "CVE-2002-0672",
                "description": "Pingtel xpressa SIP-based voice-over-IP phone 1.2.5 through 1.2.7.4 allows attackers with physical access to restore the phone to factory defaults without authentication via a menu option, which sets the administrator password to null.",
                "indicator_types": [
                    "compromised"
                ],
                "pattern": "([(software:cpe='cpe:2.3:h:pingtel:xpressa:1.2.5:*:*:*:*:*:*:*') OR (software:cpe='cpe:2.3:h:pingtel:xpressa:1.2.7.4:*:*:*:*:*:*:*')])",
                "pattern_type": "stix",
                "pattern_version": "2.1",
                "valid_from": "2002-07-23T04:00:00Z",
                "external_references": [
                    {
                        "source_name": "cve",
                        "url": "https://nvd.nist.gov/vuln/detail/CVE-2002-0672",
                        "external_id": "CVE-2002-0672"
                    }
                ],
                "object_marking_refs": [
                    "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
                    "marking-definition--562918ee-d5da-5579-b6a1-fae50cc6bad3"
                ]
            },
            {
                "type": "indicator",
                "spec_version": "2.1",
                "id": "indicator--522d3b88-5a0f-5155-a9fa-f4eb81f245ed",
                "created_by_ref": "identity--562918ee-d5da-5579-b6a1-fae50cc6bad3",
                "created": "1999-12-01T05:00:00.000Z",
                "modified": "2008-09-09T12:36:03.397Z",
                "name": "CVE-1999-0857",
                "description": "FreeBSD gdc program allows local users to modify files via a symlink attack.",
                "indicator_types": [
                    "compromised"
                ],
                "pattern": "([(software:cpe='cpe:2.3:o:freebsd:freebsd:3.3:*:*:*:*:*:*:*' OR software:cpe='cpe:2.3:o:freebsd:freebsd:3.3:-:*:*:*:*:*:*' OR software:cpe='cpe:2.3:o:freebsd:freebsd:3.3:rc:*:*:*:*:*:*')])",
                "pattern_type": "stix",
                "pattern_version": "2.1",
                "valid_from": "1999-12-01T05:00:00Z",
                "external_references": [
                    {
                        "source_name": "cve",
                        "url": "https://nvd.nist.gov/vuln/detail/CVE-1999-0857",
                        "external_id": "CVE-1999-0857"
                    }
                ],
                "object_marking_refs": [
                    "marking-definition--94868c89-83c2-464b-929b-a1a8aa3c8487",
                    "marking-definition--562918ee-d5da-5579-b6a1-fae50cc6bad3"
                ]
            }
        ]
    }
]

# Expected error responses
EXPECTED_RESPONSES = {
    "200": {"http_status": 200},
    "400": {"http_status": 400}, # The server did not understand the request
    "401": {"http_status": 401}, # The client needs to authenticate
    "403": {"http_status": 403}, # The client does not have access to this resource
    "404": {"http_status": 404}, # not found, or the client does not have access to the resource
    "406": {"http_status": 406}, # The media type provided in the Accept header is invalid
    "413": {"http_status": 413}, # The POSTed payload exceeds the max_content_length of the API Root
    "415": {"http_status": 415}, # The client attempted to POST a payload with a content type the server does not support
    "422": {"http_status": 422}, # The object type or version is not supported or could not be processed. This can happen, for example, when sending a version of STIX that this TAXII Server does not support and cannot process, when sending a malformed body, or other unprocessable content
}

TAXII_ENDPOINTS = [
    {"endpoint": "/api/taxii2/", "method": "GET"},
    {"endpoint": f"/api/taxii2/{API_ROOT}/", "method": "GET"},
    {"endpoint": f"/api/taxii2/{API_ROOT}/collections/", "method": "GET"},
    {"endpoint": f"/api/taxii2/{API_ROOT}/collections/{{COLLECTION_ID}}/", "method": "GET"},
    {"endpoint": f"/api/taxii2/{API_ROOT}/collections/{{COLLECTION_ID}}/manifest/", "method": "GET"},
    {"endpoint": f"/api/taxii2/{API_ROOT}/collections/{{COLLECTION_ID}}/objects/", "method": "GET"},
    {"endpoint": f"/api/taxii2/{API_ROOT}/collections/{{COLLECTION_ID}}/objects/", "method": "POST"},
    {"endpoint": f"/api/taxii2/{API_ROOT}/collections/{{COLLECTION_ID}}/objects/{{OBJECT_ID}}/", "method": "GET"},
    {"endpoint": f"/api/taxii2/{API_ROOT}/collections/{{COLLECTION_ID}}/objects/{{OBJECT_ID}}/", "method": "DELETE"},
    {"endpoint": f"/api/taxii2/{API_ROOT}/collections/{{COLLECTION_ID}}/objects/{{OBJECT_ID}}/versions/", "method": "GET"},
    {"endpoint": f"/api/taxii2/{API_ROOT}/status/{{STATUS_ID}}/", "method": "GET"},
]

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.base_url = BASE_URL
        self.headers = REQUEST_HEADERS

    def check_response(self, method, url, expected_status, json=None, auth=None, test_number=None):
        logger.info(f"===TEST {test_number}===")
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
        response_json = response.json()
        self.assertEqual(response.status_code, expected_status["http_status"])
        self.assertIn("title", response_json, "The response JSON should contain a 'title' field.")

    def check_get_response(self, method, url, expected_status, expected_body, auth=None, test_number=None):
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
        if objects:
            expected_id = expected_body["objects"][0]["id"]
            self.assertTrue(any(obj["id"] == expected_id for obj in objects), f"Expected id: {expected_id} not found in response")
        else:
            self.assertEqual(objects, expected_body["objects"], "Expected empty objects list in response")
