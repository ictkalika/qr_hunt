import json
from pathlib import Path

# So, here I am trying to get the root directory of this app
BASE_DIR = Path(__file__).resolve().parent.parent


DATA_FILE = BASE_DIR / "data" / "data.json"
ID_FILE = BASE_DIR / "data" / "id.json"


def load_data():
    try:
        with open(DATA_FILE, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {"error": "JSON data file not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}


def get_all_codes():
    try:
        with open(ID_FILE, "r", encoding="utf-8") as file:
            id_map = json.load(file)
        return list(id_map.keys())

    except FileNotFoundError:
        return {"error": "ID map file not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}


def search_id(hex_code):
    try:
        with open(ID_FILE, "r", encoding="utf-8") as file:
            id_map = json.load(file)
        return id_map.get(hex_code)
    except FileNotFoundError:
        return {"error": "ID map file not found"}
    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}


def search_data(item_id):
    data = load_data()
    if "error" in data:
        return data

    return data.get(str(item_id), {"error": "Item not found"})
