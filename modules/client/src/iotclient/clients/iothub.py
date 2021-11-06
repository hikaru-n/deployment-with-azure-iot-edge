from typing import Dict
from threading import Thread

from azure.iot.device import IoTHubDeviceClient, Message

from iotclient import get_azure_connection_string


class IoTHub(Thread):
    def __init__(self, messages):
        super().__init__()
        self.messages = messages
        self._device_client = self._get_device_client()

    def _get_device_client(self):
        value = get_azure_connection_string()
        return IoTHubDeviceClient.create_from_connection_string(value)

    def _check_message_include_estimater_results(self, message):
        if not isinstance(message, Dict):
            raise TypeError

        if message.get("Prediction", None) is None:
            raise ValueError

        if message.get("ElapsedTime", None) is None:
            raise ValueError

    def _send(self):
        if not self.messages.empty():
            data = self.messages.get()
            self._check_message_include_estimater_results(data)
            message = Message(str(data))
            self._device_client.send_message(message)

    def run(self):
        while True:
            self._send()
