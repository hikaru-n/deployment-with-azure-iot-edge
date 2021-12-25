import os
import time
from threading import Thread

import cv2


def _warmup():
    time.sleep(5)


def _get_video_capture():
    index = int(os.environ.get("CAMERA_INDEX", 0))
    capture = cv2.VideoCapture(index)
    _warmup()
    return capture


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
        can_captured, image = self._impl.read()
        if can_captured:
            self._images.put(image)

    def run(self):
        while self._alive:
            self._run()
