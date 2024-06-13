from textwrap import indent
import requests
import time
import json
import os

import flask
from flask import Flask, request, jsonify, abort
from flask_cors import CORS

API_PATH = "/v1/API"

app = Flask(__name__)


@app.route(f'{API_PATH}/test', methods=["GET"])
def test():
    return {"TEST": 200}


@app.route(f'{API_PATH}/getusers', methods=["GET"])
def getusers():
    if not os.path.exists("API/database.json"):
        abort(404, description="Database file not found")

    with open("API/database.json", "r") as file:
        file_content = file.read()
        if not file_content.strip():
            abort(500, description="Database file is empty")

    try:
        data = json.loads(file_content)
    except json.JSONDecodeError:
        abort(500, description="Error decoding JSON")

    return jsonify(data)


@app.route(f'{API_PATH}/get_history', methods=["GET"])
def get_history():

    if not os.path.exists("target.json"):
        abort(404, description="File not found")

    with open("target.json", "r") as file:
        file_content = file.read()

    if not file_content.strip():
        return {"success": False, "data": {}}

    try:
        data = json.loads(file_content)

    except json.JSONDecodeError:
        abort(500, description="Error decoding JSON")

    return jsonify({"success": True, "data": data})


@app.route(f'{API_PATH}/add_history', methods=["GET"])
def add_history():

    rid = request.args.get('rid', default="1", type=str)
    uid = request.args.get('uid', default="2", type=str)

    if not os.path.exists("target.json"):
        abort(404, description="File not found")

    with open("target.json", "r") as file:
        file_content = file.read()

    with open("reserved.json", "r") as file:
        reserved_content = file.read()

    try:
        data = json.loads(file_content)
        reserved_data = json.loads(reserved_content)
        data[rid] = uid
        reserved_data[rid] = {}

        with open("target.json", "w") as file:
            file.write(json.dumps(data, indent=4))

        with open("reserved.json", "w") as file:
            file.write(json.dumps(reserved_data, indent=4))

    except json.JSONDecodeError:
        abort(500, description="Error decoding JSON")

    return jsonify({"success": True, "data": data})


@app.route(f'{API_PATH}/add_messages', methods=["POST"])
def add_messages():
    data = request.json
    rid = request.args.get('rid', default="1", type=str)

    with open("reserved.json", "r") as file:
        reserved_content = file.read()

    try:
        reserved_data = json.loads(reserved_content)
        if rid in reserved_data:
            del reserved_data[rid]
        reserved_data[rid] = data["msg"]

        with open("reserved.json", "w") as file:
            file.write(json.dumps(reserved_data, indent=4))

    except json.JSONDecodeError:
        abort(500, description="Error decoding JSON")

    return jsonify({"success": True, "data": data})


@app.route(f'{API_PATH}/get_messages', methods=["GET"])
def get_messages():

    rid = request.args.get('rid', default="1", type=str)

    with open("reserved.json", "r") as file:
        reserved_content = file.read()

    try:
        reserved_data = json.loads(reserved_content)

    except json.JSONDecodeError:
        abort(500, description="Error decoding JSON")

    return jsonify({"success": True, "data": reserved_data})


@app.route(f'{API_PATH}/remove_data', methods=["POST"])
def remove_data():
    data = request.json
    if not data:
        abort(400, description="No data provided")

    with open("target.json", "r") as file:
        file_content = file.read()

    try:
        file_data = json.loads(file_content)
        if data["id"] in file_data:
            del file_data[str(data["id"])]
            with open("target.json", "w") as file:
                file.write(json.dumps(file_data))
            return jsonify({"message": "Data removed successfully"})
    except json.JSONDecodeError:
        abort(500, description="Error decoding JSON")

    return jsonify(data)


@app.route(f'{API_PATH}/add_users', methods=["POST"])
def add_users():
    data = request.json

    if not os.path.exists("API/database.json"):
        abort(404, description="Database file not found")

    with open("API/database.json", "r") as file:
        existing_data = json.load(file)

    for guild_id, guild_data in data.items():
        if guild_id not in existing_data:
            existing_data[guild_id] = guild_data
        else:
            for member_id, member_data in guild_data.items():
                if member_id not in existing_data[guild_id]:
                    existing_data[guild_id][member_id] = member_data

    with open("API/database.json", "w") as file:
        json.dump(existing_data, file, indent=4)

    return "Users added successfully"


def main():
    app.run('0.0.0.0', 8080, debug=False)


if __name__ == "__main__":
    main()
