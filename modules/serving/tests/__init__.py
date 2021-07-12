import pathlib
import functools
import PIL

TEST_DATA_DIR = pathlib.Path.cwd() / "tests" / "data"


@functools.lru_cache
def get_image(name):
    image_name = TEST_DATA_DIR / name
    image = PIL.Image.open(image_name)
    image = image.convert("RGB")
    return image
