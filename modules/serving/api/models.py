from flask import Blueprint, jsonify

bp = Blueprint("models", __name__, url_prefix="models")


@bp.route("/")
def index():
    return ""


@bp.route("/models/<name>/inference", methods=["POST"])
def inference(name):
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
