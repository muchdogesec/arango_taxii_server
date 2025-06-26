import glob
import os
from pathlib import Path
import time
from types import SimpleNamespace
from urllib.parse import urljoin
import pytest
from .utils import get_session, validate_envelope
from tests.create_accounts_and_databases import COLL_1_1, COLL_1_2, COLL_2_1

@pytest.mark.parametrize(
    ["headers", 'user', "api_root", "collection_id", "object_id", "filter_kwargs", "expected_status", "expected_versions"],
    [
        pytest.param({'Accept': "xml"}, 'user_rw', 'test1_database', COLL_1_2, 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', {}, 406, None, id="bad accept header 1"),
        pytest.param({'Accept': "application/json"}, 'user_rw', 'test1_database', COLL_1_2, 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', {}, 406, None, id="bad accept header 2"),
        pytest.param(None, 'user_ro', 'test1_database', "non-existent-collection", 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', {'match[version]': 'last'}, 404, [], id="nonexistent collection"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, 'missing-object--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', {'match[version]': 'last'}, 200, [], id="non-existent object"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', {'match[version]': 'last'}, 200, ['2023-06-29T00:00:00.000Z'], id="last"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', {'match[version]': 'first'}, 200, ['2023-04-27T00:00:00.000Z'], id="first"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', {'match[version]': '2023-04-27T00:00:00.000Z'}, 200, ['2023-04-27T00:00:00.000Z'], id="modified 1"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', {'match[version]': '2023-06-29T00:00:00.000Z'}, 200, ['2023-06-29T00:00:00.000Z'], id="modified 2"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', {'match[version]': '2023-04-27T00:00:00.000Z,2023-06-29T00:00:00.000Z'}, 200, ['2023-06-29T00:00:00.000Z', '2023-04-27T00:00:00.000Z'], id="modified 3"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', {'match[version]': 'all'}, 200, ['2023-06-29T00:00:00.000Z', '2023-04-27T00:00:00.000Z'], id="all"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', {'match[version]': 'all', 'match[spec_version]': '2.1'}, 200, ['2023-06-29T00:00:00.000Z', '2023-04-27T00:00:00.000Z'], id="all spec_version_2.1"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', {'match[version]': 'all', 'match[spec_version]': '2.0'}, 200, [], id="all spec_version_2.0"),
    ]
)
def test_object_retrieve(headers, user, api_root, collection_id, object_id, filter_kwargs, expected_status, expected_versions):
    s = get_session()
    s = get_session(auth=(user, user))
    resp = s.get(
        f"/api/taxii2/{api_root}/collections/{collection_id}/objects/{object_id}/",
        headers=headers,
        query_params=filter_kwargs
    )
    assert resp.status_code == expected_status
    assert (
        resp.headers["Content-Type"] == "application/taxii+json;version=2.1"
    ), "response `header['content-type']` must always be `application/taxii+json;version=2.1`"
    if expected_status != 200:
        return
    data = resp.json()
    validate_envelope(data)
    versions = {x['modified'] for x in data['objects']}
    assert versions == set(expected_versions)


@pytest.mark.parametrize(
    ['user', "api_root", "collection_id", "object_id", "expected_status", "expected_versions"],
    [
        pytest.param('user_ro', 'test1_database', "non-existent-collection", 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', 404, [], id="nonexistent collection"),
        pytest.param('user_none', 'test1_database', COLL_1_2, 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', 404, [], id="no permission at all"),
        pytest.param('bad user', 'test1_database', COLL_1_2, 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', 404, [], id="bad user"),
        pytest.param('user_ro', 'test1_database', COLL_1_2, 'missing-object--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', 200, [], id="non-existent obj"),
        ##
        pytest.param('user_rw', 'test1_database', COLL_1_2, 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', 200, ['2023-06-29T00:00:00.000Z', '2023-04-27T00:00:00.000Z'], id="good 1"),
        pytest.param('user_rw', 'test1_database', COLL_1_2, 'weakness--054fa434-776d-5b30-9566-809507993dd0', 200, ['2020-06-25T00:00:00.000Z', '2023-06-29T00:00:00.000Z']),
        pytest.param('user_rw', 'test1_database', COLL_1_2, 'weakness--0e3285cb-3cba-5d16-8f2a-9449a6242793', 200, ["2023-04-27T00:00:00.000Z", "2023-06-29T00:00:00.000Z"]),
    ]
)
def test_object_versions(user, api_root, collection_id, object_id, expected_status, expected_versions):
    s = get_session()
    s = get_session(auth=(user, user))
    resp = s.get(
        f"/api/taxii2/{api_root}/collections/{collection_id}/objects/{object_id}/versions/",
    )
    assert resp.status_code == expected_status
    assert (
        resp.headers["Content-Type"] == "application/taxii+json;version=2.1"
    ), "response `header['content-type']` must always be `application/taxii+json;version=2.1`"
    if expected_status != 200:
        return
    data = resp.json()
    validate_envelope(data, 'versions')
    versions = {version for version in data['versions']}
    assert versions == set(expected_versions)


@pytest.mark.parametrize(
    ['user', "api_root", "collection_id", "object_id", "filter_kwargs", "expected_status", "versions_after"],
    [
        pytest.param('user_ro', 'test1_database', "non-existent-collection", 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', {'match[version]': 'last'}, 404, [], id="nonexistent collection"),
        pytest.param('user_ro', 'test1_database', COLL_1_2, 'missing-object--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', None, 403, [], id="non-existent obj"),
        pytest.param('user_ro', 'test1_database', COLL_1_2, 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', {'match[version]': 'last'}, 403, [], id="no write permission"),
        pytest.param('user_none', 'test1_database', COLL_1_2, 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', {'match[version]': 'last'}, 404, [], id="no permission at all"),
        pytest.param('bad user', 'test1_database', COLL_1_2, 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', {'match[version]': 'last'}, 404, [], id="bad user"),
        ##
        pytest.param('user_rw', 'test1_database', COLL_1_2, 'weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', None, 200, [], id="deletes all"),
        pytest.param('user_rw', 'test1_database', COLL_1_2, 'weakness--054fa434-776d-5b30-9566-809507993dd0', {'match[version]': 'last'}, 200, ["2020-06-25T00:00:00.000Z"], id="deletes last"),
        pytest.param('user_rw', 'test1_database', COLL_1_2, 'weakness--054fa434-776d-5b30-9566-809507993dd0', {'match[version]': 'first'}, 200, [], id="deletes first"),
        pytest.param('user_rw', 'test1_database', COLL_1_2, 'weakness--0e3285cb-3cba-5d16-8f2a-9449a6242793', {'match[version]': '2023-06-29T00:00:00.000Z'}, 200, ["2023-04-27T00:00:00.000Z"], id="deletes modified"),
    ]
)
def test_object_delete(user, api_root, collection_id, object_id, filter_kwargs, expected_status, versions_after, subtests):
    s = get_session(auth=(user, user))
    url = f"/api/taxii2/{api_root}/collections/{collection_id}/objects/{object_id}/"
    resp = s.delete(
        url,
        query_params=filter_kwargs
    )
    assert resp.status_code == expected_status
    if expected_status != 200:
        return
    with subtests.test('check_versions_after_delete', delete_filters=filter_kwargs, object_url=url):
        test_object_retrieve(None, user, api_root, collection_id, object_id, {'match[version]': 'all'}, 200, versions_after)