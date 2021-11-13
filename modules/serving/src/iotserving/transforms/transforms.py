import abc

import torchvision.transforms as T
import torchvision.transforms.functional as F


class Augmentation(abc.ABC):
    def __call__(self, *args, **kwargs):
        raise NotImplementedError()


class Resize(Augmentation):
    def __init__(self, size):
        self._size = size

    def __call__(self, input):
        input = F.to_pil_image(input)
        input = F.resize(input, self._size)
        input = F.to_tensor(input)
        return input


class Transformer:
    def __init__(self, elements=None) -> None:
        self._elements = [
            Resize((224, 224)),
            T.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
        ]

    def __call__(self, input):
        for t in self._elements:
            input.data = t(input.data)
        return input
