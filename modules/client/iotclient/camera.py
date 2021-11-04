import os
from threading import Thread

import cv2


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
