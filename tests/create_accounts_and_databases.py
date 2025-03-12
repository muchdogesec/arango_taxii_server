import os
from urllib.parse import urljoin
import arango
from arango import ArangoClient

import requests

USERS = {
    "user_rw",
    "user_ro",
    "user_none"
}
COLL_1_1 = "kraz"
COLL_1_2 = "mazov"
COLL_2_1 = "innocence"
DATABASES = {
    "test1_database": [COLL_1_1, COLL_1_2],
    "test2_database": [COLL_2_1],
}


arango_db_url = os.getenv('ARANGODB_HOST_URL')
arango_db_auth = (os.getenv('ARANGODB_USERNAME'), os.getenv('ARANGODB_PASSWORD'))
client = ArangoClient(
    hosts=os.getenv('ARANGODB_HOST_URL')
)
sys_db = client.db(
    username=arango_db_auth[0],
    password=arango_db_auth[1],
)

def create_user(username):
    sys_db.create_user(username=username, password=username)


def create_database(db_name, collections):
    sys_db.create_database(db_name)
    db = client.db(db_name, username=arango_db_auth[0], password=arango_db_auth[1])

    for username in USERS:
        db.update_permission(username, permission=username.split('_')[-1], database=db_name)
        
    for collection_name in collections:
        db.create_collection(collection_name+"_vertex_collection")
        db.create_collection(collection_name+"_edge_collection")
        for username in USERS:
            db.update_permission(username, permission=username.split('_')[-1], database=db_name, collection=collection_name+"_vertex_collection")
            db.update_permission(username, permission=username.split('_')[-1], database=db_name, collection=collection_name+"_edge_collection")

if __name__ == '__main__':
    for username in USERS:
        create_user(username)

    for db_name, collections in DATABASES.items():
        create_database(db_name, collections)