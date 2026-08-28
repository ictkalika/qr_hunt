from flask import Flask, jsonify, render_template

from utils.dataSearch import load_data, search_data, search_id

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the QR Hunt"


if __name__ == "__main__":
    app.run(debug=True)
