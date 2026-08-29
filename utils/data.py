import json
import os
import random
import string
from pathlib import Path

# So, here I a
# m trying to get the root directory of this app
DATA_DIR = Path(__file__).resolve().parent.parent / "data"

if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

DATA_FILE = DATA_DIR / "data.json"
ID_FILE = DATA_DIR / "data" / "id.json"


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


def generate_hex_code():
    hex_list = get_all_codes()
    hex_characters = "0123456789ABCDEF"
    while True:
        hex_code = ""
        for i in range(6):
            hex_code += random.choice(hex_characters)

        if hex_code not in hex_list:
            return hex_code


def add_data(question, answer):
    data = load_data()

    if "error" in data:
        return data

    try:
        with open(ID_FILE, "r", encoding="utf-8") as file:
            id_map = json.load(file)

    except FileNotFoundError:
        return {"error": "ID map file not found"}

    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}

    if not question or not question.strip():
        return {"error": "Question cannot be empty"}

    if not answer or not answer.strip():
        return {"error": "Answer cannot be empty"}

    new_id = max(id_map.values(), default=0) + 1

    hex_code = generate_hex_code()

    data[str(new_id)] = {"question": question, "answer": answer}

    id_map[hex_code] = new_id

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=2)

    with open(ID_FILE, "w", encoding="utf-8") as file:
        json.dump(id_map, file, indent=2)

    return {"id": new_id, "hex_code": hex_code}
