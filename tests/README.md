## Setup a test Arango Instance

### Create test environment outside of Docker

```shell
python3 -m venv arango_taxii_server-venv
source arango_taxii_server-venv/bin/activate
# install requirements
pip3 install -r requirements.txt
```

### set environment variables

For it to work correctly and test everything, you need to set the following env variables

```env
ARANGODB_HOST_URL=http://localhost:8529
ARANGODB_USERNAME=USERNAME
ARANGODB_PASSWORD=PASSWORD
SCHEMATHESIS_HOOKS=tests.st_hooks.links
DJANGO_DEBUG=False
```

## run the test

```shell
st run --checks all http://127.0.0.1:8009/api/schema/ --generation-allow-x00 false --contrib-openapi-formats-uuid  --show-trace --exclude-tag schema
```