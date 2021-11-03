import requests
import pytest


@pytest.mark.usefixtures("restart_api")
def test_api_returns_predict(url):
    requests.post(f"{url}/predict")
