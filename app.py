# main.py

import json
import os

from flask import Flask, jsonify, render_template

app = Flask(__name__)

# Path to your JSON data
DATA_FILE = os.path.join("data", "data.json")


def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"error": "JSON data file not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}


@app.route("/")
def home():
    return "Welcome to the QR Hunt"


@app.route("/api/data")
def get_data():
    return jsonify(load_data())


if __name__ == "__main__":
    app.run(debug=True)
