
# Create your views here.
import logging
from urllib.parse import urljoin
import uuid

import django.core.exceptions
from drf_spectacular.utils import extend_schema, extend_schema_serializer
from rest_framework import decorators, generics, permissions, views, viewsets, exceptions
from rest_framework.request import Request
# from rest_framework.response import Response
from rest_framework import renderers, parsers

from .utils import ErrorResp, Response, TaxiiEnvelope

from . import task_helpers
from .. import conf
from . import arango_helper, open_api_schemas, serializers, models
from .serializers import ServerInfoSerializer
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
    
def get_added_date_headers(object_dict):
    return {"X-TAXII-Date-Added-First": object_dict.get("added_first"), "X-TAXII-Date-Added-Last": object_dict.get("added_last")}

def get_status(id):
    try:
        # status = get_object_or_404(models.UploadTask, pk=id)
        status = models.UploadTask.objects.get(pk=id)
        s = serializers.TaxiiStatusSerializer(status)
        return Response(s.data)
    except (models.UploadTask.DoesNotExist, django.core.exceptions.ValidationError) as e:
        return ErrorResp(404, f"status object with status-id `{id}` does not exist")

class ArangoView(views.APIView):
    permission_classes = [permissions.IsAuthenticated]
    renderer_classes = [TaxiiJSONRenderer]
    def handle_exception(self, exc):
        if isinstance(exc, arango_helper.ArangoError):
            return ErrorResp(exc.http_code, exc.message)
        elif isinstance (exc, exceptions.APIException):
            return ErrorResp(exc.status_code, exc.default_detail, exc.get_full_details())
        elif isinstance(exc, django.core.exceptions.ValidationError):
            return ErrorResp(400, "The server did not understand the request or filter parameters", details=exc.error_list)
        else:
            logging.exception(exc, exc_info=True)
            return ErrorResp(500, "Server ran into an error while processing request")



class ServerInfoView(generics.GenericAPIView, ArangoView):
    @extend_schema_serializer(many=False)
    @extend_schema(responses={200:ServerInfoSerializer, **serializers.TaxiiErrorSerializer.error_responses(401, 403, 404, 406)}, operation_id='discover', tags=open_api_schemas.OpenApiTags.API_ROOT.tags, summary="Get information about the TAXII Server and available API Roots", description=textwrap.dedent("""
        This Endpoint provides general information about a TAXII Server, including the advertised API Roots. It's a common entry point for TAXII Clients into the data and services provided by a TAXII Server. For example, clients auto-discovering TAXII Servers via the DNS SRV record will be able to automatically retrieve a discovery response for that server by requesting the `/taxii2/` path on that domain.\n\n
        If your request fails authentication then you will get a HTTP 401 (Unauthorized) error. Assuming your authentication details are correct, you will see a HTTP 200 (Success) response. If the API Roots list is empty, it means your user has no access to any API Roots on this server.
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
        This Endpoint provides general information about an API Root, which can be used to help users and clients decide whether and how they want to interact with it. Multiple API Roots may be hosted on a single TAXII Server. Often, an API Root represents a single trust group.\n\n
        If your request fails authentication then you will get a HTTP 401 (Unauthorized) error. If you are not authorized to view this API Root and/or `status_id`, or if either does not exist you will get a HTTP 404 (Not Found) error.
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
        This Endpoint provides information about the status of a previous request. In TAXII 2.1, the only request that can be monitored is one to add objects to a Collection. It is typically used by TAXII Clients to monitor a POST request that they made in order to take action when it is complete.\n\n
        If your request fails authentication then you will get a HTTP 401 (Unauthorized) error. If you are not authorized to view this API Root, or it does not exist you will get a HTTP 404 (Not Found) error.
        """))
    def retrieve(self, request, status_id=None, api_root=None):
        return get_status(status_id)

class CollectionView(ArangoView, viewsets.ViewSet):
    lookup_url_kwarg = "collection_id"
    serializer_class = serializers.MultiCollectionSerializer

    @property
    def pagination_class(self):
        if self.action == 'manifest':
            return TaxiiEnvelope('objects')

    @extend_schema("taxii2_collections_list", tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Get information about all collections", responses={200: serializers.MultiCollectionSerializer, **serializers.TaxiiErrorSerializer.error_responses()}, description=textwrap.dedent("""
        This Endpoint provides information about the Collections hosted under this API Root. This is similar to the response to get a Collection, but rather than providing information about one Collection it provides information about all of the Collections. Most importantly, it provides the Collection's id, which is used to request objects or manifest entries from the Collection.\n\n
        If your request fails authentication then you will get a HTTP 401 (Unauthorized) error. If you are not authorized to view this API Root, or it does not exist you will get a HTTP 404 (Not Found) error.
        """))
    def list(self, request: Request, api_root=""):
        db: arango_helper.ArangoSession =  request.user.arango_session
        collections = db.get_collections(api_root)
        s = self.serializer_class(data={"collections": collections})
        s.is_valid()
        return Response(s.data)

    @extend_schema(responses={200:serializers.SingleCollectionSerializer, **serializers.TaxiiErrorSerializer.error_responses()}, tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Get information about a specific collection", description=textwrap.dedent("""
        This Endpoint provides general information about a Collection, which can be used to help users and clients decide whether and how they want to interact with it. For example, it will tell clients what it's called and what permissions they have to it.\n\n
        If your request fails authentication then you will get a HTTP 401 (Unauthorized) error. If you are not authorized to view this API Root, or either the API Root and/or Collection does not exist you will get a HTTP 404 (Not Found) error.
        """))
    def retrieve(self, request: Request, api_root="", collection_id=""):
        db: arango_helper.ArangoSession =  request.user.arango_session
        collection = db.get_collection(api_root, collection_id)
        s = serializers.SingleCollectionSerializer(data=collection)
        s.is_valid()
        return Response(s.data)

    @extend_schema(responses={200:serializers.ManifestObjectSerializer(many=True), **serializers.TaxiiErrorSerializer.error_responses()}, parameters=open_api_schemas.ObjectsQueryParams, tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Get manifest information about the object in a collection.",  description=textwrap.dedent("""
        This Endpoint retrieves a manifest about the objects in a Collection. It supports filtering identical to the get objects Endpoint but rather than returning the object itself it returns metadata about the object. It can be used to retrieve metadata to decide whether it's worth retrieving the actual objects.\n\n
        If your request fails authentication then you will get a HTTP 401 (Unauthorized) error. If you are not authorized to view this API Root, or either the API Root and/or Collection does not exist you will get a HTTP 404 (Not Found) error. If the Collection you are trying to access specifies `can_read` as `false` for your authenticated user you will get a HTTP 403 (Forbidden) error.
        """))
    @decorators.action(methods=['GET'], detail=True)
    def manifest(self, request, api_root="", collection_id=""):
        db: arango_helper.ArangoSession =  request.user.arango_session
        manifest = db.get_objects_all(api_root, collection_id, request.query_params, 'manifest')
        for r in manifest.result:
            r["media_type"] = conf.media_type
        return self.pagination_class.get_paginated_response(manifest.result, manifest)

class ObjectView(ArangoView, viewsets.ViewSet):
    lookup_url_kwarg = "object_id"
    parser_classes = [TaxiiJSONParser]

    @property
    def pagination_class(self):
        if self.action == 'versions':
            return TaxiiEnvelope("versions")
        return TaxiiEnvelope("objects")
    
    def get_serializer_class(self):
        if self.action == 'create':
            return serializers.ObjectsSerializer
        return serializers.StixObjectField

    @extend_schema(tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, responses={200:serializers.TaxiiStatusSerializer, **serializers.TaxiiErrorSerializer.error_responses(400, 401, 403, 404, 406, 413, 415, 422)}, request=serializers.ObjectsSerializer, summary="Add a new object to a specific collection", description=textwrap.dedent("""
        This Endpoint adds objects to a Collection. Successful responses to this Endpoint will contain a status resource describing the status of the request. The status resource contains an id, which can be used to make requests to the get status Endpoint, a status flag to indicate whether the request is completed or still being processed, and information about the status of the particular objects in the request.\n\n
        If your request fails authentication then you will get a HTTP 401 (Unauthorized) error. If you are not authorized to view this API Root, or either the API Root and/or Collection does not exist you will get a HTTP 404 (Not Found) error. If the Collection you are trying to add an object to specifies `can_write` as `false` for your authenticated user you will get a HTTP 403 (Forbidden) error.
        """))
    def create(self, request: Request, api_root="", collection_id="", more_queries={}):
        db: arango_helper.ArangoSession =  request.user.arango_session
        if (
                conf.server_max_content_length and 
                int(request.META.get("CONTENT_LENGTH") or 0) > conf.server_max_content_length
            ):
                return ErrorResp(413, f"Request Entity Too Large. Request's Content-Length must not be higher than api_root.max_content_length.")

        serializer = self.get_serializer_class()(data=request.data)
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
        This Endpoint retrieves objects from a Collection. Clients can search for objects in the Collection, retrieve all objects in a Collection, or paginate through objects in the Collection. Pagination is supported by the `limit` URL query parameter and the `more` property of the envelope.\n\n
        If your request fails authentication then you will get a HTTP 401 (Unauthorized) error. If you are not authorized to view this API Root, or either the API Root and/or Collection does not exist you will get a HTTP 404 (Not Found) error. If the Collection you are trying to access specifies `can_read` as `false` for your authenticated user you will get a HTTP 403 (Forbidden) error.
        """), responses={200: open_api_schemas.StixObject, **serializers.TaxiiErrorSerializer.error_responses()})
    def list(self, request: Request, api_root="", collection_id="", more_queries={}):
        db: arango_helper.ArangoSession =  request.user.arango_session
        objects = db.get_objects_all(api_root, collection_id, {**request.query_params.dict(), **more_queries}, "objects")
        return self.pagination_class.get_paginated_response(objects.result, objects)

    @extend_schema("taxii2_collections_objects_retrieve_envelope", tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Get a specific object from a collection", parameters=open_api_schemas.SingleObjectQueryParams, responses={200: open_api_schemas.StixObject, **serializers.TaxiiErrorSerializer.error_responses()}, description=textwrap.dedent("""
        This Endpoint gets an object from a Collection by its id. It can be thought of as a search where the `match[id]` parameter is set to the `object_id` in the path. The `object_id` MUST be the STIX id.\n\n
        If your request fails authentication then you will get a HTTP 401 (Unauthorized) error. If you are not authorized to view this API Root, or either the API Root and/or Collection does not exist you will get a HTTP 404 (Not Found) error. If the Collection you are trying to access specifies `can_read` as `false` for your authenticated user you will get a HTTP 403 (Forbidden) error.
        """))
    def retrieve(self, request:Request, api_root="", collection_id="", object_id=""):
        return self.list(request, api_root, collection_id, more_queries={"match[id]": object_id})

    @extend_schema(parameters=open_api_schemas.VersionsQueryParams, responses={200: open_api_schemas.OpenApiTypes.DATETIME, **serializers.TaxiiErrorSerializer.error_responses()}, tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Get a list of object versions from a collection", description=textwrap.dedent("""
        This Endpoint retrieves a list of one or more versions of an object in a Collection. This list can be used to decide whether it's worth retrieving the actual objects, or if new versions have been added. If a STIX object is not versioned (and therefore does not have a `modified` timestamp), the server uses the stix2atango `_record_modified` timestamp.\n\n
        If your request fails authentication then you will get a HTTP 401 (Unauthorized) error. If you are not authorized to view this API Root, or either the API Root and/or Collection does not exist you will get a HTTP 404 (Not Found) error. If the Collection you are trying to access specifies `can_read` as `false` for your authenticated user you will get a HTTP 403 (Forbidden) error.
        """))
    @decorators.action(methods=['GET'], detail=True)
    def versions(self, request:Request, api_root="", collection_id="", object_id=""):
        db: arango_helper.ArangoSession =  request.user.arango_session
        objects = db.get_objects_all(api_root, collection_id, {"match[version]": "all", **request.query_params.dict(), "match[id]": object_id}, "versions")
        return self.pagination_class.get_paginated_response([x["version"] for x in objects.result], objects)

    @extend_schema(parameters=open_api_schemas.ObjectDeleteParams, tags=open_api_schemas.OpenApiTags.COLLECTIONS.tags, summary="Delete a specific object from a collection", responses={(200, TaxiiJSONRenderer.media_type):open_api_schemas.OpenApiTypes.NONE, **serializers.TaxiiErrorSerializer.error_responses()}, description=textwrap.dedent("""
        This Endpoint deletes an object from a Collection by its id. The `object_id` MUST be the STIX id. To support removing a particular version of an object, this Endpoint supports filtering. The only valid match parameter is `version`. If no filters are applied, all versions of the object will be deleted.\n\n
        If your request fails authentication then you will get a HTTP 401 (Unauthorized) error. If you are not authorized to view this API Root, or either the API Root and/or Collection does not exist you will get a HTTP 404 (Not Found) error. If the Collection you are trying to add an object to specifies `can_write` as `false` for your authenticated user you will get a HTTP 403 (Forbidden) error.
        """))
    def destroy(self, request:Request, api_root="", collection_id="", object_id=""):
        db: arango_helper.ArangoSession =  request.user.arango_session
        db.remove_object(api_root, collection_id, object_id, match_version=request.query_params.get('match[version]'))
        return Response()
