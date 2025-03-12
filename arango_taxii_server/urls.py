from django.urls import include, path
from arango_taxii_server.app.urls import handler404, handler500

urlpatterns = [
    path('api/', include('arango_taxii_server.app.urls')),
]