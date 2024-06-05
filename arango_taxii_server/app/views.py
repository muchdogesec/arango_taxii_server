
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

from . import task_helpers
from .. import conf
from . import arango_helper, open_api_schemas, serializers, models
from .serializers import ServerInfoSerializer
from enum import StrEnum
from django.shortcuts import get_object_or_404
    
def get_added_date_headers(objects, key='created'):
    if not objects:
        return {"X-TAXII-Date-Added-First": None, "X-TAXII-Date-Added-Last": None}
    first, last = objects[0], objects[-1]
    if key:
        first = first.get(key)
        last  = last.get(key)
    return {"X-TAXII-Date-Added-First": first, "X-TAXII-Date-Added-Last": last}

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
    def handle_exception(self, exc):
        if isinstance(exc, arango_helper.ArangoError):
            return ErrorResp(exc.http_code, exc.message)
        if isinstance (exc, exceptions.APIException):
            return ErrorResp(exc.status_code, exc.default_detail, exc.get_full_details())
        return super().handle_exception(exc)



class ServerInfoView(generics.GenericAPIView, ArangoView):
    @extend_schema_serializer(many=False)
    @extend_schema(responses={200:ServerInfoSerializer, **serializers.TaxiiErrorSerializer.error_responses(401, 403, 404, 406)}, operation_id='discover', tags=open_api_schemas.OpenApiTags.API_ROOT.tags, summary="Get information about the TAXII Server and any advertised API Roots")
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
    @extend_schema(responses={200: serializers.APIRootSerializer(many=False), **serializers.TaxiiErrorSerializer.error_responses(401, 403, 404, 406)}, operation_id='api_root_retrieve', tags=open_api_schemas.OpenApiTags.API_ROOT.tags, summary="Get information about a specific API Root")
    def list(self, request:Request, api_root=None):
        db: arango_helper.ArangoSession =  request.user.arango_session
        read, write = db.get_database(api_root)
        s = serializers.APIRootSerializer(data={"title":api_root, "can_read": read, "can_write": write})
        s.is_valid()
        return Response(s.data)
        
class StatusView(ArangoView, viewsets.ViewSet):
    lookup_url_kwarg = 'status_id'
    @extend_schema(tags=open_api_schemas.OpenApiTags.API_ROOT.tags, responses={200: serializers.TaxiiStatusSerializer, **serializers.TaxiiErrorSerializer.error_responses(401, 403, 404, 406)})
    def retrieve(self, request, status_id=None, api_root=None):
        return get_status(status_id)

class CollectionView(ArangoView, viewsets.ViewSet):
    lookup_url_kwarg = "collection_id"
    serializer_class = serializers.MultiCollectionSerializer

    @extend_schema("taxii2_collections_list", tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Get information about all collections", responses={200: serializers.MultiCollectionSerializer, **serializers.TaxiiErrorSerializer.error_responses()})
    def list(self, request: Request, api_root=""):
        db: arango_helper.ArangoSession =  request.user.arango_session
        collections = db.get_collections(api_root)
        s = self.serializer_class(data={"collections": collections})
        s.is_valid()
        return Response(s.data)

    @extend_schema(responses={200:serializers.SingleCollectionSerializer, **serializers.TaxiiErrorSerializer.error_responses()}, tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Get information about a specific collection")
    def retrieve(self, request: Request, api_root="", collection_id=""):
        db: arango_helper.ArangoSession =  request.user.arango_session
        collection = db.get_collection(api_root, collection_id)
        s = serializers.SingleCollectionSerializer(data=collection)
        s.is_valid()
        return Response(s.data)

    @extend_schema(responses={200:serializers.ManifestSerializer, **serializers.TaxiiErrorSerializer.error_responses()}, parameters=open_api_schemas.ObjectsQueryParams, tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Get manifest information about the contents of a specific collection.")
    @decorators.action(methods=['GET'], detail=True)
    def manifest(self, request, api_root="", collection_id=""):
        db: arango_helper.ArangoSession =  request.user.arango_session
        manifest = db.get_objects_all(api_root, collection_id, request.query_params, 'manifest')
        s = serializers.ManifestSerializer(data={"objects": manifest.result, "more": manifest.dict["hasMore"], "next": manifest.dict.get("id")})
        s.is_valid()
        return Response(s.data, headers=get_added_date_headers(manifest.result, key='date_added'))

class ObjectView(ArangoView, viewsets.ViewSet):
    serializer_class = serializers.ObjectSerializer
    lookup_url_kwarg = "object_id"

    @extend_schema(tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, responses={200:serializers.TaxiiStatusSerializer, **serializers.TaxiiErrorSerializer.error_responses(400, 401, 403, 404, 406, 413, 415, 422)}, request=serializers.ObjectSerializer, summary="Add a new object to a specific collection")
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

    @extend_schema("taxii2_collections_objects_list", parameters=open_api_schemas.ObjectsQueryParams, tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Get all objects from a collection", responses={200: serializer_class, **serializers.TaxiiErrorSerializer.error_responses()})
    def list(self, request: Request, api_root="", collection_id="", more_queries={}):
        db: arango_helper.ArangoSession =  request.user.arango_session
        objects = db.get_objects_all(api_root, collection_id, {**request.query_params.dict(), **more_queries}, "objects")
        s = serializers.ObjectSerializer(data={"objects": objects.result, "more": objects.dict["hasMore"], "next": objects.dict.get("id")})
        s.is_valid()
        return Response(s.data, headers=get_added_date_headers(objects.result))

    @extend_schema(tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Get a specific object from a collection", parameters=open_api_schemas.SingleObjectQueryParams, responses={200: serializer_class, **serializers.TaxiiErrorSerializer.error_responses()})
    def retrieve(self, request:Request, api_root="", collection_id="", object_id=""):
        return self.list(request, api_root, collection_id, more_queries={"match[id]": object_id})

    @extend_schema(parameters=open_api_schemas.VersionsQueryParams, responses={200: serializers.VersionsSerializer, **serializers.TaxiiErrorSerializer.error_responses()}, tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Get a list of object versions from a collection")
    @decorators.action(methods=['GET'], detail=True)
    def versions(self, request:Request, api_root="", collection_id="", object_id=""):
        db: arango_helper.ArangoSession =  request.user.arango_session
        objects = db.get_objects_all(api_root, collection_id, {"match[version]": "all", **request.query_params.dict(), "match[id]": object_id}, "versions")
        s = serializers.VersionsSerializer(data={"versions": objects.result, "more": objects.dict["hasMore"], "next": objects.dict.get("id")})
        s.is_valid()
        return Response(s.data, headers=get_added_date_headers(objects.result, key=None))

    @extend_schema(tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Delete a specific object from a collection", responses={200:{}, **serializers.TaxiiErrorSerializer.error_responses()})
    def destroy(self, request:Request, api_root="", collection_id="", object_id=""):
        db: arango_helper.ArangoSession =  request.user.arango_session
        db.remove_object(api_root, collection_id, object_id)
        return Response()
