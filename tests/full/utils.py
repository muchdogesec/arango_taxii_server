import glob
import json
import os
from pathlib import Path
from urllib.parse import urljoin
from django.test import Client
import pytest
from base64 import b64encode


def get_headers(auth=None):
    h = {
        "Content-Type": "application/taxii+json;version=2.1",
        "Accept": "application/taxii+json;version=2.1",
    }
    if auth:
        h["Authorization"] = "Basic " + b64encode(":".join(auth).encode()).decode()
    return h


def get_session(auth=None):
    s = Client(headers=get_headers(auth=auth))
    return s

def validate_envelope(data: dict, object_key="objects"):
    assert isinstance(data, dict), "envelope must be a dict type"
    assert "more" in data, "envelope must have key `more`"
    assert "next" in data, "envelope must have key `next`"
    assert object_key in data, "envelope must have key `objects`"
    assert type(data[object_key]) == list, "envelope.objects must be a list"
