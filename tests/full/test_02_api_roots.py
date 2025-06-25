import glob
import os
from pathlib import Path
import time
from types import SimpleNamespace
from urllib.parse import urljoin
import pytest
from .utils import get_session


@pytest.mark.parametrize(
    ["username", "api_root_name", 'extra_headers', "expected_status", "expected_body"],
    [
        pytest.param(
            "user_rw",
            "test2_database",
            None,
            200,
            {
                "max_content_length": 10485760,
                "title": "test2_database",
                "versions": ["application/stix+json;version=2.1"],
            },
            id="good 1",
        ),
        pytest.param(
            "user_rw",
            "test2_database",
            {"accept": "application/json"},
            406,
            None,
            id="bad accept",
        ),
        pytest.param(
            "user_rw",
            "test2_database",
            {"accept": "text/html"},
            406,
            None,
            id="bad accept",
        ),
        pytest.param(
            "user_ro",
            "test2_database",
            None,
            200,
            {
                "max_content_length": 10485760,
                "title": "test2_database",
                "versions": ["application/stix+json;version=2.1"],
            },
            id="good 2",
        ),
        pytest.param(
            "user_rw",
            "test1_database",
            None,
            200,
            {
                "max_content_length": 10485760,
                "title": "test1_database",
                "versions": ["application/stix+json;version=2.1"],
            },
            id="good 3",
        ),
        pytest.param(
            "user_none",
            "test1_database",
            None,
            403,
            {},
            id="bad 1",
        ),
    ],
)
def test_api_root(username, api_root_name, extra_headers, expected_status, expected_body):
    s = get_session(auth=(username, username))
    resp = s.get(
        f"/api/taxii2/{api_root_name}/", headers=extra_headers
    )
    assert resp.status_code == expected_status
    assert (
        resp.headers["Content-Type"] == "application/taxii+json;version=2.1"
    ), "response `header['content-type']` must always be `application/taxii+json;version=2.1`"
    if expected_status != 200:
        return
    data = resp.json()
    assert data == expected_body
