from arango_taxii_server.settings import *


DEBUG = False
ARANGO_TAXII_SETTINGS = {
    'MAX_CONTENT_LENGTH': 10485760,
    'SERVER_TITLE': "Arango Taxii Server Title",
    'SERVER_DESCRIPTION': "Arango TAXII Server Description",
    'CONTACT_URL': 'https://github.com/muchdogesec/arango_taxii_server/issues/',
    'CONTACT_EMAIL': 'noreply@dogesec.com',
    'DEFAULT_PAGINATION_LIMIT': 45,
    'MAX_PAGINATION_LIMIT': 1000,
    'ARANGODB_HOST_URL': os.getenv('ARANGODB_HOST_URL'),
    'APIROOT_BASE_URL': os.getenv('APIROOT_BASE_URL'),
}