import os
from threading import Thread

import cv2


def _get_video_capture():
    index = os.environ.get("CAMERA_INDEX", 0)
    return cv2.VideoCapture(index)


class Camera(Thread):
    def __init__(self, images):
        super().__init__()
        self._images = images
        self._impl = _get_video_capture()
        self._alive = True

    def kill(self):
        self._images.queue.clear()
        self._alive = False

    def _run(self):
        image = self._impl.read()
        self._images.put(image)

    def run(self):
        while self._alive:
            self._run()
