from flask import Flask, request
from spotify.cacheHandler import CacheHandler


app = Flask(__name__)
cache = CacheHandler()

@app.route("/")
def home():
    return "Welcome to test server!"

@app.route("/callback")
def callback():
    """
    Endpoint for handling Authorzation Code Flow.
    """

    if request.method == "GET":
        # get query parameters
        code = request.args["code"] if "code" in request.args else None
        error = request.args["error"] if "error" in request.args else None
        state = request.args["state"] if "state" in request.args else None

        # store results in cache
        if code: cache.saveData("code", code)
        if error: cache.saveData("error", error)
        if state: cache.saveData("state", state)

    return "Endpoint for handling Authorization Code Flow"


if __name__ == "__main__":
    app.run(port=5000)