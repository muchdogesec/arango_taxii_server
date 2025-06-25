import glob
import os
from pathlib import Path
import time
from types import SimpleNamespace
from urllib.parse import urljoin
import pytest
from .utils import get_session
from tests.create_accounts_and_databases import COLL_1_1, COLL_1_2, COLL_2_1

null, true, false = None, True, False


@pytest.mark.parametrize(
    [
        "username",
        "api_root_name",
        "collection_name",
        "extra_headers",
        "expected_status",
        "expected_body",
    ],
    [
        pytest.param(
            "user_rw",
            "test2_database",
            COLL_2_1,
            None,
            200,
            {
                "id": COLL_2_1,
                "title": COLL_2_1,
                "description": null,
                "can_read": true,
                "can_write": true,
                "media_types": ["application/stix+json;version=2.1"],
            },
            id="good 1",
        ),
        pytest.param(
            "user_rw",
            "test2_database",
            COLL_2_1,
            {"accept": "application/json"},
            406,
            None,
            id="bad accept",
        ),
        pytest.param(
            "user_rw",
            "test2_database",
            COLL_2_1,
            {"accept": "text/html"},
            406,
            None,
            id="bad accept",
        ),
        pytest.param(
            "user_ro",
            "test2_database",
            COLL_2_1,
            None,
            200,
            {
                "id": COLL_2_1,
                "title": COLL_2_1,
                "description": null,
                "can_read": true,
                "can_write": false,
                "media_types": ["application/stix+json;version=2.1"],
            },
            id="good 2",
        ),
        pytest.param(
            "user_rw",
            "test1_database",
            COLL_1_1,
            None,
            200,
            
            {
                "id": COLL_1_1,
                "title": COLL_1_1,
                "description": null,
                "can_read": true,
                "can_write": true,
                "media_types": ["application/stix+json;version=2.1"],
            },
            id="good 3",
        ),
        pytest.param(
            "user_none",
            "test1_database",
            COLL_1_1,
            None,
            404,
            {},
            id="user with no access",
        ),
        pytest.param(
            "user_rw",
            "test1_database",
            "bad_collection",
            None,
            404,
            {},
            id="invalid collection",
        ),
        pytest.param(
            "user_rw",
            "bad_apiroot",
            "bad_collection",
            None,
            404,
            {},
            id="invalid apiroot",
        ),
    ],
)
def test_collection(
    username,
    api_root_name,
    collection_name,
    extra_headers,
    expected_status,
    expected_body,
):
    s = get_session(auth=(username, username))
    resp = s.get(
        f"/api/taxii2/{api_root_name}/collections/{collection_name}/",
        headers=extra_headers,
    )
    assert resp.status_code == expected_status
    assert (
        resp.headers["Content-Type"] == "application/taxii+json;version=2.1"
    ), "response `header['content-type']` must always be `application/taxii+json;version=2.1`"
    if expected_status != 200:
        return
    data = resp.json()
    assert data == expected_body
