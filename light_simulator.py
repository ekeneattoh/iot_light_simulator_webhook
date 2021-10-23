from flask import Flask, jsonify
from flask_cors import CORS

application = Flask(__name__)

# to allow CORS
CORS(application)


@application.route("/", methods=["GET"])
def home() -> dict:
    return {
        "data": "IOT Light Simulator"
    }


@application.route("/light-on", methods=["POST"])
def light_on() -> dict:
    return {
        "data": "Light is ON"
    }


@application.route("/light-off", methods=["POST"])
def light_off() -> dict:
    return {
        "data": "Light is OFF"
    }


if __name__ == "__main__":
    application.run(host="0.0.0.0")
