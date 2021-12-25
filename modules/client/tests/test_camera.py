import os
from queue import Queue

import numpy as np
from iotclient.clients import Camera
import pytest
from . import get_image


def not_found_web_camera():
    number = os.environ.get("INDEX", 0)
    return not os.path.exists(f"/dev/index{number}")


class _FakeVideoCapture:
    def __init__(self, *args, **kwargs):
        pass

    def read(self):
        return True, get_image("cat.jpg")


def use_fake_camera_capture(mocker):
    mocker.patch("cv2.VideoCapture", _FakeVideoCapture)


class TestCameraClient:
    def _test_run(self, images):
        client = Camera(images)
        client._run()

    @pytest.mark.skipif(not_found_web_camera(), reason="not found web camera")
    def test_camera_capture(self):
        images = Queue(1)
        self._test_run(images)

    def test_camera_capture_local_image(self, mocker):
        use_fake_camera_capture(mocker)
        images = Queue(1)
        self._test_run(images)

        actual = images.get()
        expect = get_image("cat.jpg")
        np.testing.assert_allclose(actual, expect)
