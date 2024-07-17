## Setup a test Arango Instance

### Create test environment outside of Docker

```shell
python3 -m venv arango_taxii_server-venv
source arango_taxii_server-venv/bin/activate
# install requirements
pip3 install -r requirements.txt
```

### Import required data

#### ATT&CK data

Download and setup a stix2arango install outside of arango_taxii_server (do not use the one that ships with this codebase).

Once done can then run...

##### setup database for testing automatically
   
```shell
sudo docker run -e ARANGO_ROOT_PASSWORD=root -p 8529:8529 arangodb/arangodb
python tests/setup_arango.py
```

##### OR setup database for testing manually

```shell
python3 utilities/arango_cti_processor/insert_archive_attack_enterprise.py --database arango_taxii_server_tests --versions 14_1,15_0,15_1 --ignore_embedded_relationships false && \
python3 utilities/arango_cti_processor/insert_archive_attack_ics.py --database arango_taxii_server_tests --versions 14_1,15_0,15_1 --ignore_embedded_relationships false && \
python3 utilities/arango_cti_processor/insert_archive_attack_mobile.py --database arango_taxii_server_tests --versions 14_1,15_0,15_1 --ignore_embedded_relationships false
```

This will install the MITRE ATT&CK versions 14.1, 15.0, 15.1 into ArangoDB into a database called `arango_taxii_server_tests_database` with each dataset in the following collections:

* `mitre_attack_enterprise_vertex_collection`/`mitre_attack_enterprise_edge_collection`
* `mitre_attack_ics_vertex_collection`/`mitre_attack_ics_edge_collection`
* `mitre_attack_mobile_vertex_collection`/`mitre_attack_mobile_edge_collection`

And then for the versioning tests

```shell
python3 utilities/arango_cti_processor/insert_archive_attack_enterprise.py --database arango_taxii_server_tests_versioning --ignore_embedded_relationships true &&
```

This will install all versions of MITRE ATT&CK Enterprise into the database `arango_taxii_server_tests_versioning` with each dataset in the following collections:

* `mitre_attack_enterprise_vertex_collection`/`mitre_attack_enterprise_edge_collection`

###### Dummy data

You should also manually create two collections in the `arango_taxii_server_tests_database`;

* `dummy_post_vertex_collection`: type = document
* `dummy_post_edge_collection`: type = edge

###### Configure Arango users for testing

To test permissions, setup 3 users in your local Arango instance (all with password `testing123`);

* `read_write_user` (permissions, read/write to all `mitre_attack_*_vertex_collection`/`mitre_attack_*_edge_collection` and `dummy_post_vertex_collection`/`dummy_post_edge_collection`)
* `read_user` (permissions, read to all `mitre_attack_*_vertex_collection`/`mitre_attack_*_edge_collection`)
* `no_access_user` (permissions, no access all `mitre_attack_*_vertex_collection`/`mitre_attack_*_edge_collection`)

You also need to ensure the default `root` user on your install with an empty password (the default). If you've changed this password, make sure to modify it in `base_test.py`.

To make it a bit clearer, here's an example of what `read_write_user` permissions should look like:

![](example_permissions.png)

### Set `.env` file for arango_taxii_server

```
# ARANGO
ARANGODB='http://host.docker.internal:8529/'
# CELERY
CELERY_BROKER_CONNECTION_RETRY_ON_STARTUP=1
# POSTGRES
POSTGRES_DB=postgres
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
# TAXII SERVER
SERVER_BASE_URL='http://127.0.0.1:8000/'
SERVER_TITLE='Arango TAXII Server'
SERVER_DESCRIPTION='https://github.com/muchdogesec/arango_taxii_server/'
SERVER_MAX_CONTENT_LENGTH=10485760
SERVER_EMAIL='noreply@dogesec.com'
SERVER_SUPPORT='https://community.dogesec.com/'
```

### Running tests

```shell
python3 -m unittest tests/TEST.py
```