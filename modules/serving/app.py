import torch
from flask import Flask, jsonify


def create_app():
    app = Flask(__name__)


@app.route("/predict", methods=["POST"])
def predict():
    eta = 10
    model_name = "resnet"
    class_name = "mikan"
    label = 0
    prob = 0.5
    return jsonify(
        {
            "eta (s)": eta,
            "model": model_name,
            "label": label,
            "class_name": class_name,
            "prob": prob
        }
    ), 201
