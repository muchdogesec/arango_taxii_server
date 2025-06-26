import glob
import os
from pathlib import Path
import time
from types import SimpleNamespace
from urllib.parse import urljoin
import pytest

from tests.create_accounts_and_databases import COLL_1_1, COLL_1_2, COLL_2_1
from tests.full.test_04_collection import test_collection
from .utils import get_session

@pytest.mark.parametrize(
    ["username", "api_root_name", 'collection_names', 'extra_headers', "expected_status", "can_read", 'can_write'],
    [
        pytest.param(
            "user_rw",
            "test2_database",
            [COLL_2_1],
            None,
            200,
            True, True,
            id="good 1",
        ),
        pytest.param(
            "user_rw",
            "test2_database",
            [COLL_2_1],
            {"accept": "application/json"},
            406,
                        True, True,
            id="bad accept",
        ),
        pytest.param(
            "user_rw",
            "test2_database",
            [COLL_2_1],
            {"accept": "text/html"},
            406,
            True, True,
            id="bad accept",
        ),
        pytest.param(
            "user_ro",
            "test2_database",
            [COLL_2_1],
            None,
            200,
            True, False,

            id="good 2",
        ),
        pytest.param(
            "user_rw",
            "test1_database",
            [COLL_1_1, COLL_1_2],
            None,
            200,
            True, True,

            id="good 3",
        ),
        pytest.param(
            "user_none",
            "test1_database",
            [],
            None,
            404,
            False, False,
            id="bad 1",
        ),
        pytest.param(
            "user_that_does_not_exist",
            "test1_database",
            [],
            None,
            404,
            False, False,
            id="user does not exist",
        ),
        pytest.param(
            "user_rw",
            "bad_database",
            [],
            None,
            404,
            False, False,
            id="api root does not exist",
        ),
    ],
)
def test_collection_list(subtests, username, api_root_name, collection_names, extra_headers, expected_status, can_read, can_write):
    s = get_session(auth=(username, username))
    resp = s.get(
        f"/api/taxii2/{api_root_name}/collections/", headers=extra_headers
    )
    assert resp.status_code == expected_status
    assert (
        resp.headers["Content-Type"] == "application/taxii+json;version=2.1"
    ), "response `header['content-type']` must always be `application/taxii+json;version=2.1`"
    if expected_status != 200:
        return
    data = resp.json()
    assert isinstance(data['collections'], list), "response must be a list of collections"
    for d in data['collections']:
        assert d['title'] in collection_names
        assert d['can_read'] == can_read
        assert d['can_write'] == can_write
        assert d['media_types'] == ['application/stix+json;version=2.1']
        collection_name = d['title']

        with subtests.test('test_collections_item_matches_collection', api_root_name=api_root_name, collection_name=collection_name):
            test_collection(username, api_root_name, collection_name, None, 200, d)
