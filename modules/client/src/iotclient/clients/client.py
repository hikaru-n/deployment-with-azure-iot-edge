import queue

from iotclient.clients import Camera, IoTHub, APIClient


class Client:
    def __init__(self, buffersize=3):
        images = queue.Queue(buffersize)
        self.camera = Camera(images=images)

        responses = queue.Queue(buffersize)
        self.api = APIClient(images, responses)

        self.iothub = IoTHub(responses)

    def run(self):
        self.camera.start()
        self.api.start()
        self.iothub.start()

    def shutdown(self):
        self.camera.kill()
        self.api.kill()
