
# Create your views here.
import json
import tempfile
from urllib.parse import urljoin
import uuid

from drf_spectacular.utils import extend_schema, extend_schema_serializer
from rest_framework import decorators, generics, permissions, views, viewsets, response, exceptions
from rest_framework.request import Request
# from rest_framework.response import Response
from datetime import datetime as dt
from rest_framework import renderers, parsers

from . import task_helpers
from .. import conf
from . import arango_helper, open_api_schemas, serializers, models
from .serializers import ServerInfoSerializer
from enum import StrEnum
from django.shortcuts import get_object_or_404
import textwrap


class TaxiiJSONParser(parsers.JSONParser):
    media_type = conf.taxii_type

class TaxiiJSONRenderer(renderers.JSONRenderer):
    media_type = conf.taxii_type
    format = 'taxii2-json'


def date_cmp(iterable, max=True):
    value = None
    for v in iterable:
        if not v:
            continue
        elif not value:
            value = v
        elif max and v > value:
            value = v
        elif not max and v < value:
            value = v
    return value
    
def get_added_date_headers(objects, first_key='created', last_key='modified'):
    if not objects:
        return {"X-TAXII-Date-Added-First": None, "X-TAXII-Date-Added-Last": None}
    
    first_min = date_cmp(map(lambda obj: obj if first_key is None else obj.get(first_key), objects), max=False)
    last_max = date_cmp(map(lambda obj: obj if last_key is None else obj.get(last_key), objects), max=True)
    return {"X-TAXII-Date-Added-First": first_min, "X-TAXII-Date-Added-Last": last_max}

def get_status(id):
    try:
        # status = get_object_or_404(models.UploadTask, pk=id)
        status = models.UploadTask.objects.get(pk=id)
        s = serializers.TaxiiStatusSerializer(status)
        return Response(s.data)
    except models.UploadTask.DoesNotExist as e:
        return ErrorResp(404, f"status object with status-id `{id}` does not exist")


class Response(response.Response):
    DEFAULT_HEADERS = {
        'Access-Control-Allow-Origin': '*',
    }
    def __init__(self, data=None, status=None, template_name=None, headers=None, exception=False, content_type=conf.taxii_type):
        headers = headers or {}
        headers.update(self.DEFAULT_HEADERS)
        super().__init__(data, status, template_name, headers, exception, content_type)

class ErrorResp(Response):
    def __init__(self, status, title, details=None):
        super().__init__({"title": title, "http_status": status, "details": dict(content=details)}, status=status)

class ArangoView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TaxiiJSONRenderer]
    def handle_exception(self, exc):
        if isinstance(exc, arango_helper.ArangoError):
            return ErrorResp(exc.http_code, exc.message)
        if isinstance (exc, exceptions.APIException):
            return ErrorResp(exc.status_code, exc.default_detail, exc.get_full_details())
        return super().handle_exception(exc)



class ServerInfoView(generics.GenericAPIView, ArangoView):
    @extend_schema_serializer(many=False)
    @extend_schema(responses={200:ServerInfoSerializer, **serializers.TaxiiErrorSerializer.error_responses(401, 403, 404, 406)}, operation_id='discover', tags=open_api_schemas.OpenApiTags.API_ROOT.tags, summary="Get information about the TAXII Server and available API Roots", description=textwrap.dedent("""
        This Endpoint provides general information about a TAXII Server, including the advertised API Roots. It's a common entry point for TAXII Clients into the data and services provided by a TAXII Server. For example, clients auto-discovering TAXII Servers via the DNS SRV record will be able to automatically retrieve a discovery response for that server by requesting the `/taxii2/` path on that domain.
        """))
    def get(self, request: Request):
        base_url = urljoin(conf.server_host_path, request._request.get_full_path(False))
        db: arango_helper.ArangoSession =  request.user.arango_session
        api_roots = [urljoin(base_url, collection+"/") for collection in db.get_databases()]
        serializer = ServerInfoSerializer(data={
            "api_roots": api_roots,
        })
        serializer.is_valid()
        return Response(serializer.data)

class ApiRootView(ArangoView, viewsets.ViewSet):
    lookup_url_kwarg = "api_root"
    @extend_schema(responses={200: serializers.APIRootSerializer(many=False), **serializers.TaxiiErrorSerializer.error_responses(401, 403, 404, 406)}, operation_id='api_root_retrieve', tags=open_api_schemas.OpenApiTags.API_ROOT.tags, summary="Get information about a specific API Root", description=textwrap.dedent("""
        This Endpoint provides general information about an API Root, which can be used to help users and clients decide whether and how they want to interact with it. Multiple API Roots may be hosted on a single TAXII Server. Often, an API Root represents a single trust group.
        """))
    def list(self, request:Request, api_root=None):
        db: arango_helper.ArangoSession =  request.user.arango_session
        read, write = db.get_database(api_root)
        s = serializers.APIRootSerializer(data={"title":api_root, "can_read": read, "can_write": write})
        s.is_valid()
        return Response(s.data)
        
class StatusView(ArangoView, viewsets.ViewSet):
    lookup_url_kwarg = 'status_id'
    @extend_schema(tags=open_api_schemas.OpenApiTags.API_ROOT.tags, responses={200: serializers.TaxiiStatusSerializer, **serializers.TaxiiErrorSerializer.error_responses(401, 403, 404, 406)}, summary="Get the status of a job by API root", description=textwrap.dedent("""
        This Endpoint provides information about the status of a previous request. In TAXII 2.1, the only request that can be monitored is one to add objects to a Collection. It is typically used by TAXII Clients to monitor a POST request that they made in order to take action when it is complete.
        """))
    def retrieve(self, request, status_id=None, api_root=None):
        return get_status(status_id)

class CollectionView(ArangoView, viewsets.ViewSet):
    lookup_url_kwarg = "collection_id"
    serializer_class = serializers.MultiCollectionSerializer

    @extend_schema("taxii2_collections_list", tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Get information about all collections", responses={200: serializers.MultiCollectionSerializer, **serializers.TaxiiErrorSerializer.error_responses()}, description=textwrap.dedent("""
        This Endpoint provides information about the Collections hosted under this API Root. This is similar to the response to get a Collection, but rather than providing information about one Collection it provides information about all of the Collections. Most importantly, it provides the Collection's id, which is used to request objects or manifest entries from the Collection.
        """))
    def list(self, request: Request, api_root=""):
        db: arango_helper.ArangoSession =  request.user.arango_session
        collections = db.get_collections(api_root)
        s = self.serializer_class(data={"collections": collections})
        s.is_valid()
        return Response(s.data)

    @extend_schema(responses={200:serializers.SingleCollectionSerializer, **serializers.TaxiiErrorSerializer.error_responses()}, tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Get information about a specific collection", description=textwrap.dedent("""
        This Endpoint provides general information about a Collection, which can be used to help users and clients decide whether and how they want to interact with it. For example, it will tell clients what it's called and what permissions they have to it.
        """))
    def retrieve(self, request: Request, api_root="", collection_id=""):
        db: arango_helper.ArangoSession =  request.user.arango_session
        collection = db.get_collection(api_root, collection_id)
        s = serializers.SingleCollectionSerializer(data=collection)
        s.is_valid()
        return Response(s.data)

    @extend_schema(responses={200:serializers.ManifestSerializer, **serializers.TaxiiErrorSerializer.error_responses()}, parameters=open_api_schemas.ObjectsQueryParams, tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Get manifest information about the object in a collection.",  description=textwrap.dedent("""
        This Endpoint retrieves a manifest about the objects in a Collection. It supports filtering identical to the get objects Endpoint but rather than returning the object itself it returns metadata about the object. It can be used to retrieve metadata to decide whether it's worth retrieving the actual objects.
        """))
    @decorators.action(methods=['GET'], detail=True)
    def manifest(self, request, api_root="", collection_id=""):
        db: arango_helper.ArangoSession =  request.user.arango_session
        manifest = db.get_objects_all(api_root, collection_id, request.query_params, 'manifest')
        s = serializers.ManifestSerializer(data={"objects": manifest.result, "more": manifest.dict["hasMore"], "next": manifest.dict.get("next")})
        s.is_valid()
        return Response(s.data, headers=get_added_date_headers(manifest.result, first_key='date_added', last_key='version'))

class ObjectView(ArangoView, viewsets.ViewSet):
    serializer_class = serializers.ObjectSerializer
    lookup_url_kwarg = "object_id"
    parser_classes = [TaxiiJSONParser]

    @extend_schema(tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, responses={200:serializers.TaxiiStatusSerializer, **serializers.TaxiiErrorSerializer.error_responses(400, 401, 403, 404, 406, 413, 415, 422)}, request=serializers.ObjectSerializer, summary="Add a new object to a specific collection", description=textwrap.dedent("""
        This Endpoint adds objects to a Collection. Successful responses to this Endpoint will contain a status resource describing the status of the request. The status resource contains an id, which can be used to make requests to the get status Endpoint, a status flag to indicate whether the request is completed or still being processed, and information about the status of the particular objects in the request.
        """))
    def create(self, request: Request, api_root="", collection_id="", more_queries={}):
        db: arango_helper.ArangoSession =  request.user.arango_session
        if (
                conf.server_max_content_length and 
                int(request.META.get("CONTENT_LENGTH") or 0) > conf.server_max_content_length
            ):
                return ErrorResp(413, f"Request Entity Too Large. Request's Content-Length must not be higher than api_root.max_content_length.")

        print(request.body)
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid()
        status_id = uuid.uuid4()
        serializer1 = serializers.TaxiiStatusSerializer(data=dict(id=status_id, username=db.user, password=db.password, db=api_root, collection=collection_id))
        serializer1.is_valid(raise_exception=True)
        task = serializer1.save()
        objects = serializer.data['objects']
        serializer2 = serializers.TaxxiiStatusObjectField(data=objects, many=True)
        serializer2.is_valid(raise_exception=True)
        serializer2.save(task=task)
        task_helpers.start_task.delay(task.pk)
        return get_status(task.pk)

    @extend_schema("taxii2_collections_objects_list", parameters=open_api_schemas.ObjectsQueryParams, tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Get all objects from a collection", description=textwrap.dedent("""
        This Endpoint retrieves objects from a Collection. Clients can search for objects in the Collection, retrieve all objects in a Collection, or paginate through objects in the Collection. Pagination is supported by the `limit` URL query parameter and the `more` property of the envelope.
        """), responses={200: serializer_class, **serializers.TaxiiErrorSerializer.error_responses()})
    def list(self, request: Request, api_root="", collection_id="", more_queries={}):
        db: arango_helper.ArangoSession =  request.user.arango_session
        objects = db.get_objects_all(api_root, collection_id, {**request.query_params.dict(), **more_queries}, "objects")
        s = serializers.ObjectSerializer(data={"objects": objects.result, "more": objects.dict["hasMore"], "next": objects.dict.get("next")})
        s.is_valid()
        return Response(s.data, headers=get_added_date_headers(objects.result))

    @extend_schema(tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Get a specific object from a collection", parameters=open_api_schemas.SingleObjectQueryParams, responses={200: serializer_class, **serializers.TaxiiErrorSerializer.error_responses()}, description=textwrap.dedent("""
        This Endpoint gets an object from a Collection by its id. It can be thought of as a search where the `match[id]` parameter is set to the `{object-id}` in the path. The `{object-id}` MUST be the STIX id.
        """))
    def retrieve(self, request:Request, api_root="", collection_id="", object_id=""):
        return self.list(request, api_root, collection_id, more_queries={"match[id]": object_id})

    @extend_schema(parameters=open_api_schemas.VersionsQueryParams, responses={200: serializers.VersionsSerializer, **serializers.TaxiiErrorSerializer.error_responses()}, tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Get a list of object versions from a collection", description=textwrap.dedent("""
        This Endpoint retrieves a list of one or more versions of an object in a Collection. This list can be used to decide whether it's worth retrieving the actual objects, or if new versions have been added. If a STIX object is not versioned (and therefore does not have a `modified` timestamp), the server uses the stix2atango `_record_modified` timestamp.
        """))
    @decorators.action(methods=['GET'], detail=True)
    def versions(self, request:Request, api_root="", collection_id="", object_id=""):
        db: arango_helper.ArangoSession =  request.user.arango_session
        objects = db.get_objects_all(api_root, collection_id, {"match[version]": "all", **request.query_params.dict(), "match[id]": object_id}, "versions")
        s = serializers.VersionsSerializer(data={"versions": objects.result, "more": objects.dict["hasMore"], "next": objects.dict.get("next")})
        s.is_valid()
        return Response(s.data, headers=get_added_date_headers(objects.result, first_key=None, last_key=None))

    @extend_schema(tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Delete a specific object from a collection", responses={200:{}, **serializers.TaxiiErrorSerializer.error_responses()}, description=textwrap.dedent("""
        This Endpoint deletes an object from a Collection by its id. The `{object-id}` MUST be the STIX id. To support removing a particular version of an object, this Endpoint supports filtering. The only valid match parameter is `version`. If no filters are applied, all versions of the object will be deleted.
        """))
    def destroy(self, request:Request, api_root="", collection_id="", object_id=""):
        db: arango_helper.ArangoSession =  request.user.arango_session
        db.remove_object(api_root, collection_id, object_id)
        return Response()
