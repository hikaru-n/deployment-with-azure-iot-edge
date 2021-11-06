from queue import Queue

from iotclient.clients import Camera, IoTHub


class Client:
    def __init__(self, buffersize=3):
        self.images = Queue(buffersize)
        self.camera = Camera(images=self.images)

        self.messages = Queue(buffersize)
        self.iothub = IoTHub(messages=self.messages)

    def run(self):
        self.camera.start()
        self.iothub.start()
