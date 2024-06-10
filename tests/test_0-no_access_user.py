# python3 -m unittest tests/test_0-no_access_user.py

import pytest
import requests
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8000"
AUTH = HTTPBasicAuth('no_access_user', 'testing123')
