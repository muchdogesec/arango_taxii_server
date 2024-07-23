from datetime import datetime
import logging
from arango import ArangoClient
from arango.database import StandardDatabase

"""


Indexes are needed for Arango Taxii Server (ATS) to work correctly, ATS makes use of subqueries which will be very slow if run on bare server, this is why this script exists

stix2arango starting from v0.0.1b1 automatically adds indexes to the collections, but if you have manually created some collections or you're migrating from an older s2a verion, you need to run this script before using ATS


# pip install python-arango && python create_indexes_for_existing_db.py
"""

ARANGO_HOST = "http://localhost:8529/"
ROOT_USERNAME = "root"
ROOT_PASSWORD = ""



def create_indexes(db: StandardDatabase):
    print("========================================")
    print("========================================")
    print("========================================")
    print(f"creating indexes for database {db.name}")
    for collection in db.collections():
        if collection.get('system'):
            continue
        name = collection['name']
        collection = db.collection(name)
        print(f">>> creating indexes for {name}")
        time = int(datetime.now().timestamp())
        collection.add_persistent_index(["id"], storedValues=["modified", "created", "type", "_record_modified", "spec_version", "_record_md5_hash"], in_background=True, name=f"by_stix_id_{time}")
        collection.add_persistent_index(["modified", "created"], storedValues=["type", "_record_modified", "id", "spec_version", "_record_md5_hash"], in_background=True, name=f"by_stix_version_{time}")
        collection.add_persistent_index(["type"], storedValues=["modified", "created", "_record_modified", "id", "spec_version", "_record_md5_hash"], in_background=True, name=f"by_stix_type_{time}")
        collection.add_persistent_index(["_record_modified", "_record_created"], storedValues=["modified","created", "type", "id", "spec_version", "_record_md5_hash"], in_background=True, name=f"by_insertion_time_{time}")

def create_indexes_for_all_databases(client: ArangoClient, sys_db: StandardDatabase):
    for db in sys_db.databases():
        if not db.endswith("_database") or db[0] == "_":
            continue
        create_indexes(client.db(name=db, username=ROOT_USERNAME, password=ROOT_PASSWORD))

if __name__ == '__main__':
    client = ArangoClient(ARANGO_HOST)
    sys_db = client.db(username=ROOT_USERNAME, password=ROOT_PASSWORD)
    create_indexes_for_all_databases(client, sys_db)