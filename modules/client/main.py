from threading import Thread
from queue import Queue

import cv2


class Camera(Thread):

    def __init__(self, index, bucket):
        super().__init__()
        self.stream = cv2.VideoCapture(index)
        self.bucket = bucket

    def run(self):
        while True:
            data = self.stream.read()
            self.bucket.put(data)

    def get_data(self):
        return self.bucket.get()


class Client:
    def __init__(self, camera=None, buffersize=3):
        self.bucket = Queue(buffersize)
        if camera is None:
            camera = Camera(index=0, bucket=self.bucket)
        self.camera = camera

    def run(self):
        self.camera.start()


def main():
    client = Client()
    client.run()


if __name__ == "__main__":
    main()
