import pytest
import torch
import torchvision.transforms as FT

from iotserving.models import Model

from . import get_image


def _get_transformer():
    return FT.Compose(
        [
            FT.Resize((224, 224)),
            FT.ToTensor(),
        ]
    )


@pytest.fixture
def transformer():
    return _get_transformer()


@pytest.fixture
def input(transformer):
    input = transformer(get_image("cat.jpg"))
    return input.unsqueeze(0)


@pytest.fixture
def model():
    return Model("resnet18")


@pytest.fixture
def detaministic():
    torch.manual_seed(0)
