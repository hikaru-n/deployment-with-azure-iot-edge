import pathlib
import functools

from PIL import Image
import numpy as np

TEST_DATA_DIR = pathlib.Path.cwd() / "tests" / "data"


@functools.lru_cache
def get_image(name):
    image_name = TEST_DATA_DIR / name
    image = Image.open(image_name)
    image = image.convert("RGB")
    return np.array(image)
