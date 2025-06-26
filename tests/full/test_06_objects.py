import glob
import os
from pathlib import Path
import time
from types import SimpleNamespace
from urllib.parse import urljoin
import pytest
from .utils import get_session, validate_envelope
from tests.create_accounts_and_databases import COLL_1_1, COLL_1_2, COLL_2_1

null, true, false = None, True, False

first_versions = [('attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298', '2022-04-25T14:00:00.188Z'), ('weakness--0e3285cb-3cba-5d16-8f2a-9449a6242793', '2023-04-27T00:00:00.000Z'), ('weakness--054fa434-776d-5b30-9566-809507993dd0', '2020-06-25T00:00:00.000Z'), ('weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', '2023-04-27T00:00:00.000Z'), ('attack-pattern--00dc0ed2-b16d-5f33-bad3-cc54fb7be6a9', '2024-03-13T00:00:00.000Z'), ('weakness--02ccafe3-fb87-5b5e-8639-117d6e87a2c7', '2020-02-24T00:00:00.000Z'), ('attack-pattern--00e4fd6f-7fcd-56d0-be21-5d61dc2c6a5a', '2024-11-22T00:00:00.000Z')]
last_versions  = [('attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298', '2022-04-25T14:00:00.188Z'), ('weakness--0e3285cb-3cba-5d16-8f2a-9449a6242793', '2023-06-29T00:00:00.000Z'), ('weakness--054fa434-776d-5b30-9566-809507993dd0', '2023-06-29T00:00:00.000Z'), ('weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', '2023-06-29T00:00:00.000Z'), ('attack-pattern--00dc0ed2-b16d-5f33-bad3-cc54fb7be6a9', '2024-08-02T00:00:00.000Z'), ('weakness--02ccafe3-fb87-5b5e-8639-117d6e87a2c7', '2020-02-24T00:00:00.000Z'), ('attack-pattern--00e4fd6f-7fcd-56d0-be21-5d61dc2c6a5a', '2024-11-22T00:00:00.000Z')]
all_versions   = [('attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298', '2022-04-25T14:00:00.188Z'), ('weakness--0e3285cb-3cba-5d16-8f2a-9449a6242793', '2023-06-29T00:00:00.000Z'), ('attack-pattern--00e4fd6f-7fcd-56d0-be21-5d61dc2c6a5a', '2024-11-22T00:00:00.000Z'), ('weakness--054fa434-776d-5b30-9566-809507993dd0', '2023-06-29T00:00:00.000Z'), ('attack-pattern--00dc0ed2-b16d-5f33-bad3-cc54fb7be6a9', '2024-03-13T00:00:00.000Z'), ('weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', '2023-04-27T00:00:00.000Z'), ('weakness--02ccafe3-fb87-5b5e-8639-117d6e87a2c7', '2020-02-24T00:00:00.000Z'), ('weakness--054fa434-776d-5b30-9566-809507993dd0', '2020-06-25T00:00:00.000Z'), ('weakness--0e3285cb-3cba-5d16-8f2a-9449a6242793', '2023-04-27T00:00:00.000Z'), ('attack-pattern--00dc0ed2-b16d-5f33-bad3-cc54fb7be6a9', '2024-08-02T00:00:00.000Z'), ('weakness--044d9bdf-3610-5bc2-8c72-bf5b86f91dd2', '2023-06-29T00:00:00.000Z')]
@pytest.mark.parametrize(
    ["headers", 'user', "api_root", "collection_id", "filter_kwargs", "expected_status", "expected_versions"],
    [
        pytest.param({'Accept': "xml"}, 'user_rw', 'test1_database', COLL_1_2, {}, 406, None, id="bad accept header 1"),
        pytest.param({'Accept': "application/json"}, 'user_rw', 'test1_database', COLL_1_2, {}, 406, None, id="bad accept header 2"),
        pytest.param(None, 'user_ro', 'test1_database', "non-existent-collection", {'match[version]': 'last'}, 404, [], id="nonexistent collection"),
        pytest.param(None, 'user_none', 'test1_database', "non-existent-collection", {'match[version]': 'last'}, 404, [], id="unauthorized user"),
        pytest.param(None, 'bad_user', 'test1_database', "non-existent-collection", {'match[version]': 'last'}, 404, [], id="bad user"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_1, {'match[version]': 'last'}, 200, [], id="empty collection"),
        pytest.param(None, 'user_rw', 'test1_database', COLL_1_2, {}, 200, last_versions, id="no filter (version defaults to last)"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, {'match[version]': 'last'}, 200, last_versions, id="version last"),
        pytest.param(None, 'user_rw', 'test1_database', COLL_1_2, {'match[version]': 'first'}, 200, first_versions, id="version first"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, {'match[version]': 'all'}, 200, all_versions, id="version all"),
        pytest.param(None, 'user_rw', 'test1_database', COLL_1_2, {'match[version]': 'first,last'}, 200, set(first_versions+last_versions), id="version first,last"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, {'match[version]': 'first,last,all'}, 200, all_versions, id="version first,last,all => all"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, {'match[version]': 'first,2024-08-02T00:00:00.000Z'}, 200, first_versions+[('attack-pattern--00dc0ed2-b16d-5f33-bad3-cc54fb7be6a9', '2024-08-02T00:00:00.000Z')], id="version first,modified"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, {'match[version]': '2024-08-02T00:00:00.000Z'}, 200, [('attack-pattern--00dc0ed2-b16d-5f33-bad3-cc54fb7be6a9', '2024-08-02T00:00:00.000Z')], id="version modified"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, {'match[spec_version]': '2.0'}, 200, [], id="spec_version 2.0"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, {'match[spec_version]': '2.1'}, 200, last_versions, id="spec_version 2.1"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, {'match[type]': 'attack-pattern'}, 200, [f for f in last_versions if f[0].startswith('attack-pattern')], id="match[type]=attack-pattern"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, {'match[type]': 'weakness'}, 200, [f for f in last_versions if f[0].startswith('weakness')], id="match[type]=weakness"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, {'match[type]': 'weakness,attack-pattern'}, 200, last_versions, id="match[type]=weakness,attack-pattern"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, {'match[type]': 'attack-pattern', 'match[version]': 'first'}, 200, [f for f in first_versions if f[0].startswith('attack-pattern')], id="match[type]=attack-pattern version first"),
        pytest.param(None, 'user_ro', 'test1_database', COLL_1_2, {'match[id]': 'attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298', 'match[version]': 'first'}, 200, [('attack-pattern--0042a9f5-f053-4769-b3ef-9ad018dfa298', '2022-04-25T14:00:00.188Z')], id="match[id] version first"),
    ]
)
def test_objects_list(headers, user, api_root, collection_id, filter_kwargs, expected_status, expected_versions):
    s = get_session(auth=(user, user))
    resp = s.get(
        f"/api/taxii2/{api_root}/collections/{collection_id}/objects/",
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
    versions = {(x['id'], x['modified']) for x in data['objects'] if not (x['id'].startswith('marking-definition') or x['id'].startswith('identity'))}
    assert len(versions) == len(expected_versions)
    assert versions == set(expected_versions)