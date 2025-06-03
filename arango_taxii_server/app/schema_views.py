
import textwrap
from .settings import arango_taxii_server_settings
from drf_spectacular.generators import SchemaGenerator
from drf_spectacular.views import SpectacularAPIView
from drf_spectacular.settings import spectacular_settings
from rest_framework.response import Response
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView


class AtsSchemaGenerator(SchemaGenerator):
    def _get_paths_and_endpoints(self):
        endpoints = []
        for endpoint in  super()._get_paths_and_endpoints():
            _, _, _, view = endpoint
            if not getattr(view, 'is_arango_taxii_server_view', None):
                continue
            view.schema_exclude = False
            endpoints.append(endpoint)
        return endpoints

class SchemaView(SpectacularAPIView):
    custom_settings = {
        "VERSION": arango_taxii_server_settings.VERSION,
        "DESCRIPTION": arango_taxii_server_settings.SERVER_DESCRIPTION,
        "TITLE": arango_taxii_server_settings.SERVER_TITLE,
        'CONTACT': {
            'email': arango_taxii_server_settings.CONTACT_EMAIL,
            'url': arango_taxii_server_settings.CONTACT_URL,
        },
        "TAGS": [
            {
                "name": "Taxii API - Server Information",
                "description": textwrap.dedent(
                    """
                Information about this TAXII Server, the available API Roots, and to retrieve the status of requests.
                """
                ),
            },
            {
                "name": "Taxii API - Collections",
                "description": textwrap.dedent(
                    """
                Collections are hosted in the context of an API Root. Each API Root MAY have zero or more Collections. As with other TAXII Endpoints, the ability of TAXII Clients to read from and write to Collections can be restricted depending on their permissions level.
                """
                ),
            },
        ],
        **arango_taxii_server_settings.SPECTACULAR_KWARGS,
    }
    generator_class = AtsSchemaGenerator
    if arango_taxii_server_settings.AUTHENTICATION_CLASSES != None:
        authentication_classes = arango_taxii_server_settings.AUTHENTICATION_CLASSES

    _schema = None
    
    def _get_schema_response(self, request):
        version = self.api_version or request.version or self._get_version_parameter(request)
        if not self.__class__._schema:
            generator = self.generator_class(urlconf=self.urlconf, api_version=version, patterns=self.patterns)
            self.__class__._schema = generator.get_schema(request=request, public=self.serve_public)
        return Response(
            data=self.__class__._schema,
            headers={"Content-Disposition": f'inline; filename="{self._get_filename(request, version)}"'}
        )
    
class SwaggerUIView(SpectacularSwaggerView):
    title = arango_taxii_server_settings.SERVER_TITLE