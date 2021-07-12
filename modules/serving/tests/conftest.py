import pytest
import torchvision.transforms as FT
from src.models import Model

from . import get_image


def _get_transformer():
    return FT.Compose(
        [
            FT.Resize((224, 224)),
            FT.ToTensor(),
        ]
    )


@pytest.fixture
def _transformer():
    return _get_transformer()


@pytest.fixture
def input(_transformer):
    input = _transformer(get_image("cat.jpg"))
    return input.unsqueeze(0).double()


@pytest.fixture
def model():
    return Model("resnet18")
