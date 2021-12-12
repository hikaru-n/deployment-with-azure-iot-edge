import pytest
from iotclient import get_api_url, get_azure_connection_string


def _overwrite_environment_value(mocker, name, value=None):
    if value is None:
        mocker.patch("os.environ", {})
    else:
        mocker.patch("os.environ", {name: value})


def test_cannot_get_connection_string_if_unnset_environment_value(mocker):
    _overwrite_environment_value(mocker, "CONNECTION_STRING")
    with pytest.raises(RuntimeError):
        get_azure_connection_string()


def test_can_get_connection_string(mocker):
    _overwrite_environment_value(mocker, "CONNECTION_STRING", "authorized")
    get_azure_connection_string()


def test_api_url_has_localhost_when_unset_api_host(mocker):
    _overwrite_environment_value(mocker, "API_HOST")
    assert get_api_url() == "http://localhost:5000"


def test_api_url_has_specified_host_name(mocker):
    hostname = "awesome"
    _overwrite_environment_value(mocker, "API_HOST", hostname)
    assert get_api_url() == f"http://{hostname}:80"
