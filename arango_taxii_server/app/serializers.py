

import json
from drf_spectacular.utils import (OpenApiExample, extend_schema_field,
                                   extend_schema_serializer, inline_serializer)
from rest_framework import serializers

from .. import conf
from .open_api_schemas import EnvelopeObjectsObject
from . import models


class SerializerBase(serializers.Serializer):
    @property
    def _serializer_fields(self):
        for field, field_obj in self.fields.items():
            if isinstance(field_obj, serializers.ListSerializer) or isinstance(field_obj, serializers.Serializer):
                yield field, field_obj
    def run_validation(self, data):
        s = self.__class__(data=data, many=isinstance(self, serializers.ListSerializer))
        for field, field_obj in self._serializer_fields:
            field_obj.initial_data = data[field]
            field_obj.is_valid()
            data[field] = field_obj.data
        return super().run_validation(data)

class NoManySerializer(serializers.Serializer):
    def __init__(self, instance=None, data=..., **kwargs):
        kwargs.pop("many", None)
        super().__init__(instance, data, **kwargs)

class ServerInfoSerializer(serializers.Serializer):
    title = serializers.CharField(default=conf.server_title)
    description = serializers.CharField(default=conf.server_description)
    contact = serializers.EmailField(default=conf.server_contact_email)
    api_roots = serializers.ListField(child=serializers.CharField())

class APIRootSerializer(serializers.Serializer):
    max_content_length = serializers.IntegerField(default=conf.server_max_content_length)
    title = serializers.CharField(required=True)
    versions = serializers.ListField(child=serializers.CharField(), default=[conf.media_type])

class SingleCollectionSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField()
    can_read = serializers.BooleanField(default=False)
    can_write = serializers.BooleanField(default=False)
    media_types = serializers.ListField(child=serializers.CharField(), default=[conf.media_type])

class MultiCollectionSerializer(SerializerBase):
    collections = SingleCollectionSerializer(many=True)


@extend_schema_field(EnvelopeObjectsObject, component_name="objects_object")
class StixObjectField(serializers.DictField):
    pass



class TaxiiEnvelopeSerializer(serializers.Serializer):
    more = serializers.BooleanField(default=False)
    next = serializers.IntegerField(required=False)
    objects = serializers.ListField(child=StixObjectField())


@extend_schema_serializer(examples=[OpenApiExample('example', value={
  "more": True,
  "next": 34617997,
  "objects": [
    {
      "date_added": "2020-10-16T00:00:00.000Z",
      "id": "relationship--da230f89-3019-5016-8b40-695f343988ea",
      "media_type": "application/stix+json;version=2.1",
      "version": "2023-02-28T00:00:00.000Z"
    },
    {
      "date_added": "2023-02-28T00:00:00.000Z",
      "id": "relationship--d99e8a09-00d6-5e64-bad8-e9a75879f63c",
      "media_type": "application/stix+json;version=2.1",
      "version": "2023-02-28T00:00:00.000Z"
    }]})])
class ManifestSerializer(TaxiiEnvelopeSerializer):
    objects =  inline_serializer("object_manifest", dict(
        date_added=serializers.CharField(),
        id=serializers.CharField(),
        media_type=serializers.CharField(default=conf.media_type, read_only=True),
        version=serializers.CharField())
    , many=True, required=True)


@extend_schema_serializer(examples=[OpenApiExample('example', value={"objects":[
        {
            "type": "threat-actor",
            "spec_version": "2.1",
            "id": "threat-actor--dfaa8d77-07e2-4e28-b2c8-92e9f7b04428",
            "created": "2014-11-19T23:39:03.893Z",
            "modified": "2014-11-19T23:39:03.893Z",
            "name": "Disco Team Threat Actor Group",
            "description": "This organized threat actor group operates to create profit from all types of crime.",
            "threat_actor_types": [
                "crime-syndicate"
            ],
            "aliases": [
                "Equipo del Discoteca"
            ],
            "roles": [
                "agent"
            ],
            "goals": [
                "Steal Credit Card Information"
            ],
            "sophistication": "expert",
            "resource_level": "organization",
            "primary_motivation": "personal-gain"
        },
        {
            "type": "identity",
            "spec_version": "2.1",
            "id": "identity--733c5838-34d9-4fbf-949c-62aba761184c",
            "created": "2016-08-23T18:05:49.307Z",
            "modified": "2016-08-23T18:05:49.307Z",
            "name": "Disco Team",
            "description": "Disco Team is the name of an organized threat actor crime-syndicate.",
            "identity_class": "organization",
            "contact_information": "disco-team@stealthemail.com"
        },
        {
            "type": "relationship",
            "spec_version": "2.1",
            "id": "relationship--a2e3efb5-351d-4d46-97a0-6897ee7c77a0",
            "created": "2020-02-29T18:01:28.577Z",
            "modified": "2020-02-29T18:01:28.577Z",
            "relationship_type": "attributed-to",
            "source_ref": "threat-actor--dfaa8d77-07e2-4e28-b2c8-92e9f7b04428",
            "target_ref": "identity--733c5838-34d9-4fbf-949c-62aba761184c"
        }
]})])
class ObjectSerializer(TaxiiEnvelopeSerializer):
    objects = serializers.ListField(child=StixObjectField())

class VersionsSerializer(TaxiiEnvelopeSerializer):
    objects = None
    versions = serializers.ListField(child=serializers.DateTimeField())


class TaxxiiStatusObjectField(serializers.ModelSerializer):
    id = serializers.CharField(source="stix_id")
    version = serializers.CharField(source='get_version', read_only=True)
    stix_data_json = serializers.CharField(write_only=True)
    class Meta:
        model = models.ObjectStatus
        fields = ("message", "version", "id", "stix_data_json")

    def run_validation(self, data=...):
        if isinstance(data, dict):
            data["stix_data_json"] = json.dumps(data)
        return super().run_validation(data)


class TaxiiStatusSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="get_status", required=False)
    total_count = serializers.IntegerField(source='get_total_count', required=False)
    success_count = serializers.IntegerField(source='get_success_count', required=False)
    successes = serializers.ListField(child=TaxxiiStatusObjectField(), required=False, source="get_successes")
    failure_count = serializers.IntegerField(source='get_failure_count', required=False)
    failures = serializers.ListField(child=TaxxiiStatusObjectField(), required=False, source="get_failures")
    pending_count = serializers.IntegerField(source='get_pending_count', required=False)
    pendings = serializers.ListField(child=TaxxiiStatusObjectField(), required=False, source="get_pendings")
    username = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False)
    db = serializers.CharField(write_only=True, required=False)
    collection = serializers.CharField(write_only=True, required=False)
    class Meta:
        model = models.UploadTask
        fields = '__all__'

def error_examples():
    TAXII_ERROR_MAPPING = {
        400: "The server did not understand the request or filter parameters",
        401: "The client needs to authenticate",
        403: "The client does not have access to this manifest resource",
        404: "The API Root or Collection ID are not found, or the client does not have access to the manifest resource",
        406: "The media type provided in the Accept header is invalid",
        413: "The POSTed payload exceeds the max_content_length of the API Root",
        415: "The client attempted to POST a payload with a content type the server does not support",
        422: "The object type or version is not supported or could not be processed.",
    }
    examples = []
    for status_code, title in TAXII_ERROR_MAPPING.items():
        examples.append(
            OpenApiExample(
                f"example-{status_code}",
                status_codes=[status_code],
                value=dict(
                    title=title,
                    http_status=str(status_code)
                )
            ),
        )
    return examples

@extend_schema_serializer(examples=error_examples())
class TaxiiErrorSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    error_id = serializers.CharField(required=False)
    error_code = serializers.CharField(required=False)
    http_status = serializers.CharField(required=False)

    @classmethod
    def error_responses(cls, *status_codes):
        status_codes = status_codes or [400, 401, 403, 404, 406]
        retval = {}
        for code in status_codes:
            retval[code] = cls
        return retval
