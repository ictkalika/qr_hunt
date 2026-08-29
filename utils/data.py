import json
import os
import random
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent.parent / "data"


if not os.path.exists(DATA_DIR):
    os.makedirs(DATA_DIR)

DATA_FILE = DATA_DIR / "data.json"
ID_FILE = DATA_DIR / "id.json"


def load_json(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            content = file.read().strip()

            if content == "" or content == "{" or content == "}":
                return {}

            file.seek(0)
            return json.load(file)

    except FileNotFoundError:
        with open(file_path, "w", encoding="utf-8") as file:
            json.dump({}, file, indent=2)

        return {}

    except json.JSONDecodeError:
        return {"error": "Invalid JSON format"}


def get_all_codes():
    id_map = load_json(ID_FILE)

    if "error" in id_map:
        return id_map

    return list(id_map.keys())


def search_id(hex_code):
    id_map = load_json(ID_FILE)

    if "error" in id_map:
        return id_map

    return id_map.get(hex_code)


def search_data(item_id):
    data = load_json(DATA_FILE)

    if "error" in data:
        return data

    return data.get(str(item_id), {"error": "Item not found"})


def generate_hex_code():
    hex_list = get_all_codes()

    if isinstance(hex_list, dict) and "error" in hex_list:
        return hex_list

    hex_characters = "0123456789ABCDEF"

    while True:
        hex_code = ""

        for i in range(6):
            hex_code += random.choice(hex_characters)

        if hex_code not in hex_list:
            return hex_code


def add_data(question, answer):
    data = load_json(DATA_FILE)

    if "error" in data:
        return data

    id_map = load_json(ID_FILE)

    if "error" in id_map:
        return id_map

    if not question or not question.strip():
        return {"error": "Question cannot be empty"}

    if not answer or not answer.strip():
        return {"error": "Answer cannot be empty"}

    new_id = max(id_map.values(), default=0) + 1

    hex_code = generate_hex_code()

    if isinstance(hex_code, dict) and "error" in hex_code:
        return hex_code

    data[str(new_id)] = {"question": question.strip(), "answer": answer.strip()}

    id_map[hex_code] = new_id

    with open(DATA_FILE, "w", encoding="utf-8") as file:
        json.dump(data, file)

    with open(ID_FILE, "w", encoding="utf-8") as file:
        json.dump(id_map, file)

    return {"id": new_id, "hex_code": hex_code}
