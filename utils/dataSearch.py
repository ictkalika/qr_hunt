import json
import os

DATA_FILE = "data.json"


def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"error": "JSON data file not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}
