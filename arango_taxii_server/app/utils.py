from rest_framework import pagination, response
from arango_taxii_server import conf
from .settings import arango_taxii_server_settings as settings

from .arango_helper import ArangoResponse


class Response(response.Response):
    DEFAULT_HEADERS = {
        "Access-Control-Allow-Origin": "*",
    }

    def __init__(
        self,
        data=None,
        status=None,
        template_name=None,
        headers=None,
        exception=False,
        content_type=conf.taxii_type,
    ):
        headers = headers or {}
        headers.update(self.DEFAULT_HEADERS)
        super().__init__(data, status, template_name, headers, exception, content_type)


class ErrorResp(Response):
    def __init__(self, status, title, details=None):
        super().__init__(
            {"title": title, "http_status": str(status), "details": dict(content=details)},
            status=status,
        )


class TaxiiEnvelope(pagination.PageNumberPagination):
    max_page_size = settings.MAX_PAGINATION_LIMIT
    page_size = settings.DEFAULT_PAGINATION_LIMIT
    page_size_query_param = "limit"
    page_query_param = "next"

    def __init__(self, results_key="objects") -> None:
        self.results_key = results_key
        super().__init__()

    def get_paginated_response(self, data, resp: ArangoResponse):

        return Response(
            {
                "more": resp.dict.get("hasMore"),
                "next": resp.dict.get("next"),
                self.results_key: data,
            },
            headers={
                "X-TAXII-Date-Added-First": resp.dict.get("added_first"),
                "X-TAXII-Date-Added-Last": resp.dict.get("added_last"),
            },
        )

    def get_paginated_response_schema(self, schema):
        return {
            "type": "object",
            "required": ["more", self.results_key],
            "properties": {
                "more": {
                    "type": "boolean",
                    "example": False,
                },
                "next": {
                    "type": "string",
                    "example": "112121_2",
                    "nullable": True
                },
                self.results_key: schema,
            },
        }

    def __call__(self, *args, **kwargs):
        return self.__class__(results_key=self.results_key, *args, **kwargs)
