import torch
from models import get_model


class Model(torch.nn.Module):
    def __init__(self, name):
        super().__init__()
        self._model = get_model(name)

    @torch.no_grad()
    def predict(self, input):
        return self._model(input)
