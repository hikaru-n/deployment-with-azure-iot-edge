import os
from typing import Dict

from threading import Thread
from queue import Queue

import cv2
from azure.iot.device import IoTHubDeviceClient, Message


class IoTHub(Thread):
    def __init__(self, messages):
        super().__init__()
        self.messages = messages
        self._device_client = self._get_device_client()

    def _get_device_client(self):
        con_str = os.environ.get("CONNECTION_STRING", "")
        if not con_str:
            raise RuntimeError("Environ name CONNECTION_STRING must be set.")
        return IoTHubDeviceClient.create_from_connection_string(con_str)

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


class Camera(Thread):
    def __init__(self, images):
        super().__init__()
        self.images = images
        self.video_capture = self._get_video_capture()

    def _get_video_capture(self):
        index = os.environ.get("CAMERA_INDEX", 0)
        return cv2.VideoCapture(index)

    def run(self):
        while True:
            data = self.video_capture.read()
            self.images.put(data)

    def get_data(self):
        return self.images.get()


class Client:
    def __init__(self, buffersize=3):
        self.images = Queue(buffersize)
        self.camera = Camera(images=self.images)

        self.messages = Queue(buffersize)
        self.iothub = IoTHub(messages=self.messages)

    def run(self):
        self.camera.start()
        self.iothub.start()


def main():
    client = Client()
    client.run()


if __name__ == "__main__":
    main()
