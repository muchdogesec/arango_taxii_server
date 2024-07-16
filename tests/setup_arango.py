
import logging
from arango import ArangoClient
from arango.database import StandardDatabase
import os

logging.basicConfig()

ARANGO_HOST = "localhost"
ARANGO_PORT = "8529"
ROOT_USERNAME = "root"
ROOT_PASSWORD = "root"
S2A_DB_NAME = "arango_taxii_server_tests"
DB_NAME = S2A_DB_NAME+"_database"
DUMMY_COLLECTION_NAME = "dummy_post"
STIX2ARANGO_PATH = "../stix2arango"

USERS = [
    ("read_write_user", "testing123", "rw"),
    ("read_user", "testing123", "ro"),
    ("no_access_user", "testing123", "none"),
]

def create_user(sys_db: StandardDatabase, username, password, permissions):
    try:
        user = sys_db.create_user(username, password)
        sys_db.update_permission(username, permissions, database=DB_NAME)
    except Exception as e:
        logging.exception(e, exc_info=True)

def create_collections(client: ArangoClient, sys_db: StandardDatabase):
    try:
        sys_db.create_database(DB_NAME)
    except Exception as e:
        logging.exception(e, exc_info=True)

    test_db = client.db(username=ROOT_USERNAME, password=ROOT_PASSWORD, name=DB_NAME)
    try:
        test_db.create_collection(f"{DUMMY_COLLECTION_NAME}_vertex_collection")
        test_db.create_collection(f"{DUMMY_COLLECTION_NAME}_edge_collection", edge=True)
    except Exception as e:
        logging.exception(e, exc_info=True)

if __name__ == '__main__':
    client = ArangoClient(f"http://{ARANGO_HOST}:{ARANGO_PORT}/")
    sys_db = client.db(username=ROOT_USERNAME, password=ROOT_PASSWORD)

    create_collections(client, sys_db)
    for (username, passwd, perm) in USERS:
        create_user(sys_db, username, passwd, perm)

    os.chdir(STIX2ARANGO_PATH)
    os.environ.update(
        ARANGODB_HOST=ARANGO_HOST,
        ARANGODB_PORT=ARANGO_PORT,
        ARANGODB_USERNAME=ROOT_USERNAME,
        ARANGODB_PASSWORD=ROOT_PASSWORD,
        ARANGODB_DATABASE=S2A_DB_NAME,
        )
    os.system(f"python3 utilities/insert_archive_attack_enterprise.py --database {S2A_DB_NAME} --versions 14_1,15_0,15_1 --ignore_embedded_relationships false")
    os.system(f"python3 utilities/insert_archive_attack_ics.py --database {S2A_DB_NAME} --versions 14_1,15_0,15_1 --ignore_embedded_relationships false")
    os.system(f"python3 utilities/insert_archive_attack_mobile.py --database {S2A_DB_NAME} --versions 14_1,15_0,15_1 --ignore_embedded_relationships false")
