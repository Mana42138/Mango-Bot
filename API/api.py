

import requests
import time
import json

import flask
from flask import Flask, request, jsonify
from flask_cors import CORS

API_PATH = "/v1/API"

app = Flask(__name__)

CORS(app)

@app.route(f'{API_PATH}/test', methods=["GET"])
def test():
    return {"TEST": 200}


def main():
    app.run('0.0.0.0', 8080)

