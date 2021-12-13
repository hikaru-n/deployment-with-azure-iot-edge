import torch
import torchvision.models.resnet as resnet


def _get_model(name, *args, **kwargs):
    if name == "resnet18":
        return resnet.resnet18(*args, **kwargs)
    elif name == "resnet34":
        return resnet.resnet34(*args, **kwargs)
    elif name == "resnet50":
        return resnet.resnet50(*args, **kwargs)
    elif name == "resnet101":
        return resnet.resnet101(*args, **kwargs)
    elif name == "resnet152":
        return resnet.resnet152(*args, **kwargs)
    else:
        raise ValueError()


class Model(torch.nn.Module):
    def __init__(self, name, pretrained=True):
        super().__init__()
        self._instance = _get_model(name, pretrained=pretrained).eval()

    @torch.no_grad()
    def forward(self, input):
        return self._instance(input)
