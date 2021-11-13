import json
from base64 import b64encode

import pytest

from . import get_image


@pytest.fixture
def payload():
    image = get_image("cat.jpg")
    shape = image.shape
    image = b64encode(image).decode("utf-8")
    return json.dumps({"image": image, "shape": shape})
