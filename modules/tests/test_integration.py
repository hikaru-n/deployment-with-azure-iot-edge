from iotclient.clients.client import Client

from . import get_image


class _FakeVideoCapture:
    def __init__(self, *args, **kwags):
        pass

    def read(self):
        return True, get_image("cat.jpg")


def use_fake_camera_capture(mocker):
    mocker.patch("cv2.VideoCapture", _FakeVideoCapture)


class _FakeIoTHubDeviceClient:
    def __init__(*args) -> None:
        pass

    @classmethod
    def create_from_connection_string(cls, *args):
        return cls(*args)

    def send_message(self, *message):
        pass


def _nullify_device_client(mocker):
    def null(*args):
        return _FakeIoTHubDeviceClient

    mocker.patch("iotclient.clients.iothub._get_device_client", null)


class TestIntegration:
    def test(self, mocker):
        use_fake_camera_capture(mocker)
        _nullify_device_client(mocker)

        client = Client()
        client.run()
        client.shutdown()

        actual = client.iothub.responses.get()
        assert actual._value.get("Prediction") == 285
