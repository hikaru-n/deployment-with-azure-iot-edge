import pytest
from src.models import Model


@pytest.mark.parametrize(
    "name", ["resnet18", "resnet34", "resnet50", "resnet101", "resnet152"]
)
def test_get_model(name):
    Model(name)


@pytest.mark.parametrize("name", ["unknown", "miss"])
def test_get_model_raise_when_model_name_is_unavailable(name):
    with pytest.raises(ValueError):
        Model(name)


def test_model_predict(input, model):
    result = model.predict(input)
    print(result.numpy().mean())
