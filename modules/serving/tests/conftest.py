import os

import pytest
import requests
import torchvision.transforms as FT
from tenacity import retry, stop_after_delay

from src.models import Model

from . import get_image


def _get_transformer():
    return FT.Compose(
        [
            FT.Resize((224, 224)),
            FT.ToTensor(),
        ]
    )


def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    if host == "localhost":
        port = 5000
    else:
        port = 80
    return f"http://{host}:{port}"


@retry(stop=stop_after_delay(10))
def wait_for_webapp_to_come_up():
    return requests.get(get_api_url())


@pytest.fixture
def _transformer():
    return _get_transformer()


@pytest.fixture
def input(_transformer):
    input = _transformer(get_image("cat.jpg"))
    return input.unsqueeze(0).double()


@pytest.fixture
def model():
    return Model("resnet18")


@pytest.fixture
def restart_api():
    ...
