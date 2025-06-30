from functools import lru_cache
import glob
import json
import os
from pathlib import Path
import time
from types import SimpleNamespace
from urllib.parse import urljoin


from tests.create_accounts_and_databases import COLL_1_1, COLL_1_2, COLL_2_1
from tests.full.utils import get_headers, get_session

API_ROOT = 'test1_database'
status_ids = []
@lru_cache()
def upload_bundles():
    s = get_session(auth=('user_rw', 'user_rw'))
    for bundle in glob.glob('tests/bundles/*.json'):
        body = Path(bundle).read_text()
        resp = s.post(f"/api/taxii2/{API_ROOT}/collections/{COLL_1_2}/objects/", data=body, headers=get_headers(('user_rw', 'user_rw')), content_type='')
        assert resp.status_code == 200, resp.status_code
        data = resp.json()
        status_id = data['id']
        resp = s.get(f"/api/taxii2/{API_ROOT}/status/{status_id}/")
        assert resp.status_code == 200, resp.data
        assert resp.data['status'] == 'complete'
        assert resp.data['failure_count'] == 0, resp.content
