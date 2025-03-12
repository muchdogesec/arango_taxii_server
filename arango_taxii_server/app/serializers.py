import json
from drf_spectacular.utils import (
    extend_schema_field,
    extend_schema_serializer,
    OpenApiResponse,
)
from rest_framework import serializers

from .. import conf
from .open_api_schemas import StixObject, ArangoTaxiiOpenApiExample
from . import models
from .settings import arango_taxii_server_settings

class SerializerBase(serializers.Serializer):
    @property
    def _serializer_fields(self):
        for field, field_obj in self.fields.items():
            if isinstance(field_obj, serializers.ListSerializer) or isinstance(
                field_obj, serializers.Serializer
            ):
                yield field, field_obj

    def run_validation(self, data):
        s = self.__class__(data=data, many=isinstance(self, serializers.ListSerializer))
        for field, field_obj in self._serializer_fields:
            field_obj.initial_data = data[field]
            field_obj.is_valid()
            data[field] = field_obj.data
        return super().run_validation(data)


class ServerInfoSerializer(serializers.Serializer):
    title = serializers.CharField(default=arango_taxii_server_settings.SERVER_TITLE)
    description = serializers.CharField(default=arango_taxii_server_settings.SERVER_DESCRIPTION)
    contact = serializers.CharField(default=arango_taxii_server_settings.CONTACT_URL)
    api_roots = serializers.ListField(child=serializers.CharField())


class APIRootSerializer(serializers.Serializer):
    max_content_length = serializers.IntegerField(
        default=arango_taxii_server_settings.MAX_CONTENT_LENGTH
    )
    title = serializers.CharField(required=True)
    versions = serializers.ListField(
        child=serializers.CharField(), default=[conf.media_type]
    )


class SingleCollectionSerializer(serializers.Serializer):
    id = serializers.CharField()
    title = serializers.CharField()
    description = serializers.CharField(required=False, allow_null=True)
    can_read = serializers.BooleanField(default=False)
    can_write = serializers.BooleanField(default=False)
    media_types = serializers.ListField(
        child=serializers.CharField(), default=[conf.media_type]
    )


class MultiCollectionSerializer(SerializerBase):
    collections = SingleCollectionSerializer(many=True)


@extend_schema_field(StixObject, component_name="objects_object")
class StixObjectField(serializers.DictField):
    pass


@extend_schema_serializer(
    examples=[
        ArangoTaxiiOpenApiExample(
            "relationship",
            {
                "date_added": "2024-01-16T00:00:00.000Z",
                "id": "relationship--da230f89-3019-5016-8b40-695f343988ea",
                "media_type": "application/stix+json;version=2.1",
                "version": "2023-02-28T00:00:00.000Z",
            },
        ),
        ArangoTaxiiOpenApiExample(
            "attack-pattern",
            {
                "date_added": "2024-06-07T16:10:44.168441Z",
                "id": "attack-pattern--09b130a2-a77e-4af0-a361-f46f9aad1345",
                "media_type": "application/stix+json;version=2.1",
                "version": "2023-08-14T17:54:22.970Z",
            },
        ),
    ]
)
class ManifestObjectSerializer(serializers.Serializer):
    id = serializers.CharField()
    date_added = serializers.DateTimeField()
    version = serializers.DateTimeField()
    media_type = serializers.CharField(default=conf.media_type)


@extend_schema_serializer(
    examples=[
        ArangoTaxiiOpenApiExample("example-empty", value={"objects": []}),
        ArangoTaxiiOpenApiExample(
            "example",
            value={
                "objects": [
                    {
                        "type": "threat-actor",
                        "spec_version": "2.1",
                        "id": "threat-actor--dfaa8d77-07e2-4e28-b2c8-92e9f7b04428",
                        "created": "2014-11-19T23:39:03.893Z",
                        "modified": "2014-11-19T23:39:03.893Z",
                        "name": "Disco Team Threat Actor Group",
                        "description": "This organized threat actor group operates to create profit from all types of crime.",
                        "threat_actor_types": ["crime-syndicate"],
                        "aliases": ["Equipo del Discoteca"],
                        "roles": ["agent"],
                        "goals": ["Steal Credit Card Information"],
                        "sophistication": "expert",
                        "resource_level": "organization",
                        "primary_motivation": "personal-gain",
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
                        "contact_information": "disco-team@stealthemail.com",
                    },
                    {
                        "type": "relationship",
                        "spec_version": "2.1",
                        "id": "relationship--a2e3efb5-351d-4d46-97a0-6897ee7c77a0",
                        "created": "2020-02-29T18:01:28.577Z",
                        "modified": "2020-02-29T18:01:28.577Z",
                        "relationship_type": "attributed-to",
                        "source_ref": "threat-actor--dfaa8d77-07e2-4e28-b2c8-92e9f7b04428",
                        "target_ref": "identity--733c5838-34d9-4fbf-949c-62aba761184c",
                    },
                ]
            },
        ),
    ]
)
class ObjectsSerializer(serializers.Serializer):
    objects = serializers.ListField(child=StixObjectField())


class TaxxiiStatusObjectField(serializers.ModelSerializer):
    id = serializers.CharField(source="stix_id")
    version = serializers.DateTimeField(source="get_version", read_only=True)
    created = serializers.DateTimeField(write_only=True, allow_null=True, required=False)
    modified = serializers.DateTimeField(write_only=True, allow_null=True, required=False)

    class Meta:
        model = models.ObjectStatus
        fields = ("message", "version", "id", "created", "modified")

    def run_validation(self, data=...):
        return super().run_validation(data)


class TaxiiStatusSerializer(serializers.ModelSerializer):
    status = serializers.CharField(source="get_status", required=False)
    total_count = serializers.IntegerField(source="get_total_count", required=False)
    success_count = serializers.IntegerField(source="get_success_count", required=False)
    successes = serializers.ListField(
        child=TaxxiiStatusObjectField(), required=False, source="get_successes"
    )
    failure_count = serializers.IntegerField(source="get_failure_count", required=False)
    failures = serializers.ListField(
        child=TaxxiiStatusObjectField(), required=False, source="get_failures"
    )
    pending_count = serializers.IntegerField(source="get_pending_count", required=False)
    pendings = serializers.ListField(
        child=TaxxiiStatusObjectField(), required=False, source="get_pendings"
    )
    username = serializers.CharField(write_only=True, required=False)
    password = serializers.CharField(write_only=True, required=False, allow_blank=True)
    db = serializers.CharField(write_only=True, required=False)
    collection = serializers.CharField(write_only=True, required=False)

    class Meta:
        model = models.UploadTask
        fields = "__all__"



class TaxiiErrorSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    description = serializers.CharField(required=False)
    error_id = serializers.CharField(required=False)
    error_code = serializers.CharField(required=False)
    http_status = serializers.CharField(required=True)

    @classmethod
    def error_responses(cls, errors: list[tuple[int, str]]) -> dict[int, OpenApiResponse]:
        responses = {}
        for status_code, message in errors:
            responses[status_code] = OpenApiResponse(
                cls,
                message,
                examples=[
                    ArangoTaxiiOpenApiExample(
                        "example",
                        value={"title": message, "http_status": str(status_code)},
                    )
                ],
            )
        return responses
