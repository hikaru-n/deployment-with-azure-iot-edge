import pytest

import torch

from iotserving.models import Model


@pytest.mark.parametrize(
    "name", ["resnet18", "resnet34", "resnet50", "resnet101", "resnet152"]
)
def test_can_get_model(name):
    Model(name)


@pytest.mark.parametrize("name", ["unknown", None])
def test_cannot_get_model_if_model_name_is_unavailable(name):
    with pytest.raises(ValueError):
        Model(name)


@pytest.mark.usefixtures("detaministic")
def test_model_predict(input, model):
    actual = model(input).mean()
    expected = torch.tensor(2.4057388145592995e-05)
    torch.testing.assert_allclose(actual, expected)
