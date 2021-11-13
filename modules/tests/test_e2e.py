from iotclient import get_api_url
import requests


def test(payload):
    url = get_api_url()
    model_name = "resnet18"
    data = requests.post(f"{url}/models/{model_name}/predict", json=payload)
    print(data.text)
