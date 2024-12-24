from django.urls import include, path

urlpatterns = [
    path('api/', include('arango_taxii_server.app.urls')),
]