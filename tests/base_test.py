import unittest
import requests
from requests.auth import HTTPBasicAuth

# generic logic

BASE_URL = "http://127.0.0.1:8000"
REQUEST_HEADERS = {'Accept': 'application/taxii+json;version=2.1'}
REQUEST_BAD_HEADER = {'Accept': 'application/json'}
EXPECTED_RESPONSE_HEADER_CONTENT_TYPE = "application/taxii+json;version=2.1"

API_ROOT = "cti_database"
BAD_API_ROOT = "xyz"

# list of collections includes both edge and vertex
LIST_OF_COLLECTIONS = [
    "mitre_attack_enterprise",
    "mitre_attack_ics",
    "mitre_attack_mobile"
]

# The server did not understand the request
EXPECTED_400_ERROR_RESPONSE = {
    "http_status": 400
}

# The client needs to authenticate
EXPECTED_401_ERROR_RESPONSE = {
    "http_status": 401
}

# The client does not have access to this resource
EXPECTED_403_ERROR_RESPONSE = {
    "http_status": 403
}

# not found, or the client does not have access to the resource
EXPECTED_404_ERROR_RESPONSE = {
    "http_status": 404
}

# The media type provided in the Accept header is invalid
EXPECTED_406_ERROR_RESPONSE = {
    "http_status": 406
}

# The POSTed payload exceeds the max_content_length of the API Root
EXPECTED_413_ERROR_RESPONSE = {
    "http_status": 413
}

# The client attempted to POST a payload with a content type the server does not support
EXPECTED_415_ERROR_RESPONSE = {
    "http_status": 415
}

# The object type or version is not supported or could not be processed. This can happen, for example, when sending a version of STIX that this TAXII Server does not support and cannot process, when sending a malformed body, or other unprocessable content
EXPECTED_422_ERROR_RESPONSE = {
    "http_status": 422
}

# User credentials dictionary
users = {
    "read_write_user": "testing123",
    "read_user": "testing123",
    "no_access_user": "testing123",
    "bad_permission_user": "testing123",
}

class BaseTest(unittest.TestCase):

    def setUp(self):
        self.users = users
        self.auth = HTTPBasicAuth('no_access_user', self.users['no_access_user'])
        self.headers = REQUEST_HEADERS
        self.bad_headers = REQUEST_BAD_HEADER
        self.expected_RESPONSE_HEADER_content_type = EXPECTED_RESPONSE_HEADER_CONTENT_TYPE
        self.base_url = BASE_URL

    def tearDown(self):
        pass
