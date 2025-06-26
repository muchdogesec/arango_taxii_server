import pytest

from tests.create_accounts_and_databases import create_db_and_users
from tests.full.utils import get_session
from tests.upload_bundles import upload_bundles

@pytest.fixture(autouse=True)
def setup_database(transactional_db):
    from arango_taxii_server.celery import app
    app.conf.task_always_eager = True
    app.conf.broker_url = 'redis://goog.ls:1235/0/1/'

    create_db_and_users()
    upload_bundles()
    yield
    app.conf.task_always_eager = False




@pytest.fixture
def unathorized_client():
    s = get_session(auth=("user_none", "user_none"))
    return s


@pytest.fixture
def read_write_client():
    s = get_session(auth=("user_rw", "user_rw"))
    return s


@pytest.fixture
def read_only_client():
    s = get_session(auth=("user_rw", "user_rw"))
    return s
