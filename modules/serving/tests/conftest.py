import os
import pathlib
from flask import Flask
import pytest
from app import predcit


def get_url():
    host = os.environ.get("APP_HOST", "localhost")
    if host == "localhost":
        return f"http://{host}:5000"
    return f"http://{host}:80"


@pytest.fixture
def url():
    return get_url()


def get_api():
    app = Flask(__name__, instance_relative_config=True)


@pytest.fixture
def restart_api():
    pathlib.Path(APP_SOURCE).touch()
