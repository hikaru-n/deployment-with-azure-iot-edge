import os
from threading import Thread
from typing import Dict
import json
import requests

from base64 import b64encode


class EmptyImageBuffer(Exception):
    """Raise image buffer has no data."""


def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    if host == "localhost":
        port = 5000
    else:
        port = 80
    return f"http://{host}:{port}"


class _Payload:
    def __init__(self, image) -> None:
        shape = image.shape
        image = b64encode(image).decode("utf-8")
        self.value = json.dumps({"image": image, "shape": shape})


class _Response:
    def __init__(self, value):
        self._check_including_estimater_results(value)
        self._value = value

    def _check_including_estimater_results(self, value):
        if not isinstance(value, Dict):
            raise TypeError

        if value.get("Prediction", None) is None:
            raise ValueError

    def __str__(self):
        return str(self._value)


class APIClient(Thread):
    def __init__(self, images, responses, model="resnet18"):
        super().__init__()
        self._images = images
        self._responses = responses
        self._model = model
        self._alive = True

    def kill(self):
        self._images.queue.clear()
        self._responses.queue.clear()
        self._alive = False

    def _post(self, payload):
        url = get_api_url()
        response = requests.post(
            f"{url}/models/{self._model}/predict", json=payload.value
        )
        return _Response(response.json())

    def _get_response(self):
        image = self._images.get()
        payload = _Payload(image)
        return self._post(payload)

    def _run(self):
        response = self._get_response()
        self._responses.put(response)

    def run(self):
        while self._alive:
            self._run()
