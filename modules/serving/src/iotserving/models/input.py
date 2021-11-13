from base64 import decodebytes

import torch


class Input:
    def __init__(self, data):
        self.data = data

    @classmethod
    def from_post_parameter(cls, param):
        data = param.get("image")
        data = decodebytes(data.encode("utf-8"))
        data = torch.frombuffer(data, dtype=torch.uint8)
        shape = param.get("shape")
        data = data.reshape(shape)
        data = data.permute(2, 0, 1)
        return cls(data)

    @property
    def data(self):
        return self._data.float()

    @data.setter
    def data(self, value):
        if not isinstance(value, torch.Tensor):
            raise ValueError
        self._data = value

    def to_minibatch(self):
        data = self.data.unsqueeze(0)
        return Input(data)
