from typing import Any, Dict

from django.conf import settings
from rest_framework.settings import APISettings, perform_import, api_settings
from django.core.signals import setting_changed


ARANGO_TAXII_DEFAULTS: dict[str, any] = {
    'APIROOT_BASE_URL': None,
    'SERVER_TITLE': "Arango Taxii Server",
    'SERVER_DESCRIPTION': "Arango TAXII Server is a production ready implementation of a TAXII 2.1 Server designed to work with ArangoDB.",
    'CONTACT_URL': '',
    'CONTACT_EMAIL': '',
    'VERSION': None,
    'MAX_CONTENT_LENGTH': 10*1024*1024, #10 MiB
    'DEFAULT_PAGINATION_LIMIT': 50,
    'MAX_PAGINATION_LIMIT': 200,
    'SUPPORT_WRITE_OPERATIONS': True,
    'ARANGODB_HOST_URL': None,
    'AUTHENTICATION_CLASSES': ["arango_taxii_server.app.authentication.ArangoServerAuthentication",],
    'PERMISSION_CLASSES': ['arango_taxii_server.app.views.APIRootAuthentication'],
    # 'COLLECTION_PERMISSION_CLASSES': ['arango_taxii_server.app.views.APIRootAuthentication', 'arango_taxii_server.app.views.CollectionAuthentication'],
    'FILTER_COLLECTIONS': 'arango_taxii_server.app.views.noop_filter',
    'FILTER_API_ROOTS': 'arango_taxii_server.app.views.noop_filter',
    'ARANGO_AUTH_FUNCTION': None,
    'SPECTACULAR_KWARGS': {},
}

IMPORT_STRINGS = [
    'AUTHENTICATION_CLASSES',
    'PERMISSION_CLASSES',
    # 'COLLECTION_PERMISSION_CLASSES',
    'FILTER_COLLECTIONS',
    'FILTER_API_ROOTS',
    'ARANGO_AUTH_FUNCTION',
]

SETTINGS_NAME = 'ARANGO_TAXII_SETTINGS'
class ArangoTaxiiServerSettings(APISettings):
    @property
    def user_settings(self):
        if not hasattr(self, '_user_settings'):
            self._user_settings = getattr(settings, SETTINGS_NAME, {})
        return self._user_settings

arango_taxii_server_settings = ArangoTaxiiServerSettings(
    defaults=ARANGO_TAXII_DEFAULTS,  # type: ignore
    import_strings=IMPORT_STRINGS,
)



def reload_api_settings(*args, **kwargs):
    setting = kwargs['setting']
    if setting == SETTINGS_NAME:
        arango_taxii_server_settings.reload()


setting_changed.connect(reload_api_settings)