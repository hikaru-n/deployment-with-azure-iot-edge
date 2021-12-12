import queue
import os

import pytest
from iotclient.clients import IoTHub
from iotclient.clients.api import _Response


def cannot_connect_with_iothub():
    """
    By setting environment CONNECTION_STRING,
    you can confirm message sent with following cmd.
    $ az iot hub monitor-events --output table --hub-name $TF_VAR_iothub_name
    """
    return os.environ.get("CONNECTION_STRING", None) is None


@pytest.fixture
def responses():
    data = queue.Queue(1)
    data.put(_Response({"Prediction": "on unit test1"}))
    return data


class _FakeIoTHubDeviceClient:
    def __init__(*args) -> None:
        pass

    @classmethod
    def create_from_connection_string(cls, *args):
        return cls(*args)

    def send_message(self, *args):
        pass


def _nullify_device_client(mocker):
    def null(*args):
        _FakeIoTHubDeviceClient

    mocker.patch("iotclient.clients.iothub._get_device_client", null)


class TestIoTHubClient:
    def _test_send_message(self, responses):
        client = IoTHub(responses)
        client._send()

    @pytest.mark.skipif(cannot_connect_with_iothub(), reason="can`t send to message")
    def test_send_message_to_iothub(self, responses):
        self._test_send_message(responses)

    def test_send_message(self, mocker, responses):
        _nullify_device_client(mocker)
        self._test_send_message(responses)
