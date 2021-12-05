import json
from flask import Flask, request
from iotserving import transforms

from iotserving.models import Model
from iotserving.models import Input

app = Flask(__name__)


def _get_input():
    param = json.loads(request.json)
    input = Input.from_post_parameter(param)
    transformer = transforms.Transformer()
    input = transformer(input)
    return input.to_minibatch()


@app.route("/models/<string:name>/predict", methods=["POST"])
def predict(name):
    model = Model(name)
    input = _get_input()
    result = model.forward(input.data)
    result = result.argmax(axis=1).item()
    return {"Prediction": result}
