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


@pytest.mark.usefixtures("use_fake_camera_capture")
def test():
    client = Client()
    client.run()
    client.shutdown()
