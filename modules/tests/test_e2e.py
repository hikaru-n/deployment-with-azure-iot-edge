import pytest
from iotclient.clients.client import Client

from . import get_image


class _FakeVideoCapture:
    def __init__(self, *args, **kwags):
        pass

    def read(self):
        return get_image("cat.jpg")


@pytest.fixture
def use_fake_camera_capture(mocker):
    mocker.patch("cv2.VideoCapture", _FakeVideoCapture)


class _FakeIoTHubClient:
    def __init__(self, responses):
        self.responses = responses

    def start(self):
        pass

    def kill(self):
        pass


@pytest.fixture
def nullify_iothub(mocker):
    mocker.patch("iotclient.clients.client.IoTHub", _FakeIoTHubClient)


@pytest.mark.usefixtures("nullify_iothub")
@pytest.mark.usefixtures("use_fake_camera_capture")
def test():
    client = Client()
    client.run()
    client.shutdown()

    actual = client.iothub.responses.get()
    assert actual._value.get("Prediction") == 285
