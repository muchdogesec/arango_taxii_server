# import pytest

# from tests.create_accounts_and_databases import create_db_and_users
# from tests.upload_bundles import upload_bundles

# @pytest.mark.django_db
# @pytest.fixture(autouse=True, scope='session')
# def setup_database(session_transaction):
#     from arango_taxii_server.celery import app
#     app.conf.task_always_eager = True
#     app.conf.broker_url = 'redis://goog.ls:1235/0/1/'

#     create_db_and_users()
#     upload_bundles()
#     yield
#     app.conf.task_always_eager = False

# @pytest.fixture(scope='session')
# def session_transaction(request, django_db_blocker, django_db_setup):
#     from django.db import connection, transaction

#     django_db_blocker.unblock()
#     # with transaction.atomic():
#     #     sid = transaction.savepoint()
#     #     yield get_atomic_rollback(request, vprint)
#     #     transaction.savepoint_rollback(sid)
#     yield
#     connection.close()