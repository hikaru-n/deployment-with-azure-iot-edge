from flask import Flask

app = Flask(__name__)


@app.route("/models/<str:name>")
def predict(modelname):
    return "Hello {}!".format(modelname)
