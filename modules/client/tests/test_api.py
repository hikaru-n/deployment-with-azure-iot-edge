import pytest
from api import get_api_url


def replace_env(mocker, name, value=None):
    if value is None:
        return
    mocker.patch("os.environ", {name: value})


@pytest.mark.parametrize("env_name, value", [("", None), ("API_HOST", "estimater")])
def test_get_api_url(mocker, env_name, value):
    replace_env(mocker, env_name, value)

    if value is None:
        assert get_api_url() == "http://localhost:5000"
    else:
        assert get_api_url() == f"http://{value}:80"
