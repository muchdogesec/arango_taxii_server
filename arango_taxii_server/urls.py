from django.urls import include, path, re_path
from rest_framework import routers
from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from arango_taxii_server.app import views


router = routers.SimpleRouter(trailing_slash=True)
router.register(r'collections', views.CollectionView, basename="collection-view")
router.register(r'collections/(?P<collection_id>\w+)/objects', views.ObjectView, basename="objects-view")
router.register(r'', views.ApiRootView, "api-root-view")
router.register(r'status', views.StatusView, "api-root-status-view")

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('api/taxii2/', views.ServerInfoView.as_view()),
    re_path('api/taxii2/(?P<api_root>\w+)/', include(router.urls), name="api-root"),
    # <>
    # SWAGGER
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    # Optional UI:
    path('api/schema/swagger-ui/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/schema/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]