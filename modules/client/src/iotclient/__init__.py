import os


def get_azure_connection_string():
    value = os.environ.get("CONNECTION_STRING")
    if value is None:
        raise RuntimeError("Environ name CONNECTION_STRING must be set.")
    return value


def get_api_url():
    host = os.environ.get("API_HOST", "localhost")
    if host == "localhost":
        port = 5000
    else:
        port = 80
    return f"http://{host}:{port}"
