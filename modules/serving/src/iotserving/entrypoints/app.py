from flask import Flask

from iotserving.models import get_model

app = Flask(__name__)


@app.route("/models/<string:modelname>/predict")
def predict(modelname):
    model = get_model(modelname)
    return "Hello {}!".format(model)
