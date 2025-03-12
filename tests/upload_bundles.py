import glob
import os
from pathlib import Path
import time
from types import SimpleNamespace
from urllib.parse import urljoin

from tests.utils import get_session

base_url = os.environ["SERVICE_BASE_URL"]
import requests
from tests.create_accounts_and_databases import COLL_1_1, COLL_1_2, COLL_2_1


def wait_for_job(api_root, status_id):
    s = get_session()
    s.auth = ('user_rw', 'user_rw')
    retries = 0
    while retries < 10:
        retries += 1
        resp = s.get(urljoin(base_url, f'/api/taxii2/{api_root}/status/{status_id}/'))
        data = resp.json()
        print(data, resp.url)
        if data['status'] == 'complete':
            return
        time.sleep(5)
    raise Exception(f"upload ({status_id =}, {api_root =}) failed")

API_ROOT = 'test1_database'
status_ids = []
if __name__ == '__main__':
    for bundle in glob.glob('tests/bundles/*.json'):
        body = Path(bundle).read_text()
        resp = requests.post(urljoin(base_url, f'api/taxii2/{API_ROOT}/collections/{COLL_1_2}/objects/'), data=body, headers={'Content-Type': 'application/taxii+json;version=2.1', 'Accept': 'application/taxii+json;version=2.1'}, auth=('user_rw', 'user_rw'))
        data = resp.json()
        status_ids.append(data['id'])
        wait_for_job(API_ROOT, data['id'])

    with open('/tmp/ats_status_ids', 'w') as f:
        for status_id in status_ids:
            print(status_id, file=f)
