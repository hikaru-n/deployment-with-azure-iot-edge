import torchvision.models.resnet as resnet


def get_model(name, *args, **kwargs):
    if name == "resnet18":
        return resnet.resnet18(*args, **kwargs).double()
    elif name == "resnet34":
        return resnet.resnet34(*args, **kwargs).double()
    elif name == "resnet50":
        return resnet.resnet50(*args, **kwargs).double()
    elif name == "resnet101":
        return resnet.resnet101(*args, **kwargs).double()
    elif name == "resnet152":
        return resnet.resnet152(*args, **kwargs).double()
    else:
        raise ValueError()
