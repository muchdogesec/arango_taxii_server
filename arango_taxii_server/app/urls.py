from django.urls import include, path, re_path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from arango_taxii_server import conf
from arango_taxii_server.app import views

from arango_taxii_server.app import schema_views

from django.http import JsonResponse
def handler404(*args, **kwargs):
    return JsonResponse(dict(http_status=str(404), title='non-existent page'), status=404, content_type=conf.taxii_type)

def handler500(*args, **kwargs):
    return JsonResponse(dict(http_status=str(500), title='internal server error'), status=500, content_type=conf.taxii_type)


router = routers.SimpleRouter(trailing_slash=True, use_regex_path=False)
router.register(r'collections', views.CollectionView, basename="collection-view")
router.register(r'collections/<slug:collection_id>/objects', views.ObjectView, basename="objects-view")
router.register(r'', views.ApiRootView, "api-root-view")
router.register(r'status', views.StatusView, "api-root-status-view")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('taxii2/', views.ServerInfoView.as_view(), name='taxii-server-discovery'),
    path('taxii2/<slug:api_root>/', include(router.urls), name="taxii-server-api-root"),
    # <>
    # SWAGGER
    path('schema/', schema_views.SchemaView.as_view(), name='taxii-server-schema'),
    # Optional UI:
    path('schema/swagger-ui/', schema_views.SwaggerUIView.as_view(url_name='taxii-server-schema'), name='swagger-ui'),
    path('schema/redoc/', SpectacularRedocView.as_view(url_name='taxii-server-schema'), name='redoc'),
]