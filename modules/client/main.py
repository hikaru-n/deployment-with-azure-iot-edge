import json
import time
import cv2
import requests


class VideoStream:

    def __init__(self, video_path):
        self.video_path = video_path

    def capture(self):
        return self.vstream.read()

    def __enter__(self):
        self.vstream = cv2.VideoCapture(self.video_path)
        return self.vstream

    def __exit__(self, *args):
        self.vstream.release()


class ImageCurlClient:

    def __init__(self,endpoint=''):
        self.endpoint = endpoint

    @staticmethod
    def send_img(self, img):
        headers = {'Content-Type': 'application/octet-stream'}
        try:
            response = requests.post(
                self.endpoint, params=self.preprocess_params, data=img)

        except Exception as e:
            print("send_img Exception -" + str(e))
            return "[]"

        return json.dumps(response.json())
