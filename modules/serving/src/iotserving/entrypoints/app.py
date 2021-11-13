import json
from flask import Flask, request
from iotserving import transforms

from iotserving.models import Model
from iotserving.models import Input

app = Flask(__name__)


@app.route("/models/<string:name>/predict", methods=["POST"])
def predict(name):
    model = Model(name)
    param = json.loads(request.json)
    input = Input.from_post_parameter(param)
    transformer = transforms.Transformer()
    input = transformer(input)
    input = input.to_minibatch()
    result = model.forward(input.data)
    print(result.argmax(axis=1))
    return {"model": ""}
