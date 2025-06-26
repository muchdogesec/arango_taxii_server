import time
from types import SimpleNamespace
from urllib.parse import urljoin
import pytest
from .utils import get_session
from arango_taxii_server.app.settings import arango_taxii_server_settings

@pytest.mark.parametrize(
    ["username", "extra_headers", "expected_status", "expected_roots"],
    [
        pytest.param("user_rw", None, 200, ["test1_database", "test2_database"], id="should show all"),
        pytest.param("user_ro", None, 200, ["test1_database", "test2_database"], id="should also show all"),
        pytest.param("user_none", None, 200, [], id="empty"),
        pytest.param("user_does_not_exist", None, 401, [], id="must fail"),
        pytest.param("user_rw", {'Accept': "application/json"}, 406, [], id="wrong accept header"),
    ]
)
def test_discovery(username, extra_headers, expected_status, expected_roots):
    s = get_session(auth=(username, username))
    resp = s.get(f"/api/taxii2/", headers=extra_headers)
    assert resp.status_code == expected_status
    assert resp.headers['Content-Type'] == "application/taxii+json;version=2.1", "response `header['content-type']` must always be `application/taxii+json;version=2.1`"
    if expected_status != 200:
        return
    data = resp.json()
    assert {root.split('/')[-2] for root in data['api_roots']} == set(expected_roots)
    assert data['title'] == "Arango Taxii Server Title"
    assert data['description'] == "Arango TAXII Server Description"