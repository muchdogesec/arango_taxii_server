import glob
import json
import os
from pathlib import Path
from urllib.parse import urljoin
import pytest
import requests


base_url = os.environ["SERVICE_BASE_URL"]

def get_session():
    s = requests.Session()
    s.headers = {
        "Content-Type": "application/taxii+json;version=2.1",
        "Accept": "application/taxii+json;version=2.1",
    }
    return s


@pytest.fixture
def unathorized_client():
    s = get_session()
    s.auth = ('user_none', 'user_none')
    return s



@pytest.fixture
def read_write_client():
    s = get_session()
    s.auth = ('user_rw', 'user_rw')
    return s

@pytest.fixture
def read_only_client():
    s = get_session()
    s.auth = ('user_rw', 'user_rw')
    return s


def validate_envelope(data: dict, object_key='objects'):
    assert isinstance(data, dict), "envelope must be a dict type"
    assert 'more' in data, 'envelope must have key `more`'
    assert 'next' in data, 'envelope must have key `next`'
    assert object_key in data, 'envelope must have key `objects`'
    assert type(data[object_key]) == list, 'envelope.objects must be a list'
