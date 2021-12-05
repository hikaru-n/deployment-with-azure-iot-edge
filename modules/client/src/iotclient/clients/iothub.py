from threading import Thread

from azure.iot.device import IoTHubDeviceClient, Message

from iotclient import get_azure_connection_string


class EmptyMessage(Exception):
    """Raise when message has no data."""


def _get_device_client():
    value = get_azure_connection_string()
    return IoTHubDeviceClient.create_from_connection_string(value)


class IoTHub(Thread):
    def __init__(self, responses):
        super().__init__()
        self.responses = responses
        self._impl = _get_device_client()
        self._alive = True

    def kill(self):
        self._alive = False

    def _send(self):
        if self.responses.empty():
            raise EmptyMessage
        data = self.responses.get()
        message = Message(str(data))
        self._impl.send_message(message)

    def run(self):
        while self._alive:
            try:
                self._send()
            except EmptyMessage:
                pass
