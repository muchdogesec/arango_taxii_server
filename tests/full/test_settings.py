from unittest.mock import patch
import pytest
from django.core.signals import setting_changed
from arango_taxii_server.app.settings import (
    arango_taxii_server_settings,
    ARANGO_TAXII_DEFAULTS,
    SETTINGS_NAME,
)
from arango_taxii_server.app.views import ArangoView


# Dummy importables to test import string functionality
def dummy_view():
    pass


def dummy_filter():
    pass


@pytest.mark.django_db
def test_arango_taxii_settings_updates_all_keys(settings):
    # All keys to override
    new_values = {
        "APIROOT_BASE_URL": "https://my-taxii.example.com",
        "SERVER_TITLE": "Custom TAXII Server",
        "SERVER_DESCRIPTION": "Customized server for testing",
        "CONTACT_URL": "https://example.com/contact",
        "CONTACT_EMAIL": "test@example.com",
        "VERSION": "1.0.1",
        "MAX_CONTENT_LENGTH": 5 * 1024 * 1024,
        "DEFAULT_PAGINATION_LIMIT": 25,
        "MAX_PAGINATION_LIMIT": 150,
        "SUPPORT_WRITE_OPERATIONS": False,
        "ARANGODB_HOST_URL": "http://arangodb.internal",
        "AUTHENTICATION_CLASSES": [f"{__name__}.dummy_view"],
        "PERMISSION_CLASSES": [f"{__name__}.dummy_view"],
        "FILTER_COLLECTIONS": f"{__name__}.dummy_filter",
        "FILTER_API_ROOTS": f"{__name__}.dummy_filter",
        "ARANGO_AUTH_FUNCTION": f"{__name__}.dummy_filter",
        "SPECTACULAR_KWARGS": {"TITLE": "TAXII"},
    }

    # Apply new settings
    settings.ARANGO_TAXII_SETTINGS = new_values
    setting_changed.send(
        sender=None,
        setting=SETTINGS_NAME,
        value=new_values,
        enter=False,
    )

    # Assert all values are updated correctly
    for key, expected_value in new_values.items():
        actual = getattr(arango_taxii_server_settings, key)

        if key in ("AUTHENTICATION_CLASSES", "PERMISSION_CLASSES"):
            # Expect a list of callables
            assert isinstance(actual, list)
            assert all(callable(item) for item in actual)
            assert actual[0].__name__ == "dummy_view"

        elif key in ("FILTER_COLLECTIONS", "FILTER_API_ROOTS", "ARANGO_AUTH_FUNCTION"):
            assert callable(actual)
            assert actual.__name__ == "dummy_filter"

        else:
            assert actual == expected_value


def test_arango_taxii_settings_defaults(settings):
    settings.ARANGO_TAXII_SETTINGS = {}
    for key, expected in ARANGO_TAXII_DEFAULTS.items():
        actual = getattr(arango_taxii_server_settings, key)

        # Import strings should be resolved to callables or lists of callables
        if key in ("AUTHENTICATION_CLASSES", "PERMISSION_CLASSES"):
            assert isinstance(actual, list), f"{key} should be a list"
            assert all(
                callable(item) for item in actual
            ), f"{key} items must be callables"

        elif key in ("FILTER_COLLECTIONS", "FILTER_API_ROOTS", "ARANGO_AUTH_FUNCTION"):
            if expected is not None:
                assert callable(actual), f"{key} should be callable"
            else:
                assert actual is None

        else:
            assert actual == expected, f"{key} should default to {expected}"


def test_filter_function__collection(settings, read_write_client):
    filter_fn = f"{__name__}.dummy_filter"
    settings.ARANGO_TAXII_SETTINGS = {"FILTER_COLLECTIONS": filter_fn}
    with patch(filter_fn) as mock_auth_class:
        resp = read_write_client.get(f"/api/taxii2/test1_database/collections/")
        assert resp.status_code == 200
        mock_auth_class.assert_called_once()


def test_filter_function__api_roots(settings, read_write_client):
    filter_fn = f"{__name__}.dummy_filter"
    settings.ARANGO_TAXII_SETTINGS = {"FILTER_API_ROOTS": filter_fn}
    with patch(filter_fn) as mock_auth_class:
        resp = read_write_client.get(f"/api/taxii2/")
        assert resp.status_code == 200
        mock_auth_class.assert_called_once()


@pytest.mark.parametrize(
    "path",
    ["/api/taxii2/test1_database/collections/", "/api/taxii2/"],
)
def test_filter_function__default(read_write_client, path):
    filter_fn = "arango_taxii_server.app.views.noop_filter"
    with patch(filter_fn) as mock_auth_class:
        resp = read_write_client.get(path)
        assert resp.status_code == 200
        mock_auth_class.assert_called_once()


@pytest.mark.parametrize(
    "fn_retval",
    [
        ("bad_user", "bad_user2"),
        ("bad_user", "bad_user2", "identity--abcd"),
    ],
)
def test_get_arango_session(settings, read_write_client, fn_retval):
    settings.ARANGO_TAXII_SETTINGS = {"ARANGO_AUTH_FUNCTION": lambda *x: fn_retval}
    with patch("arango_taxii_server.app.views.ArangoSession") as mock_arango_session:
        resp = read_write_client.get("/api/taxii2/test1_database/collections/")
        mock_arango_session.assert_called_with(*fn_retval)



def test_get_arango_session__default(settings, read_write_client):
    with patch("arango_taxii_server.app.views.ArangoSession") as mock_arango_session:
        resp = read_write_client.get("/api/taxii2/test1_database/collections/")
        mock_arango_session.assert_called_with("user_rw", "user_rw")


