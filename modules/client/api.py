import os


def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    if host == "localhost":
        port = 5000
    else:
        port = 80
    return f"http://{host}:{port}"
