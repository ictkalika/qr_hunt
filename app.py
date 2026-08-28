from flask import Flask, jsonify, render_template, send_file

from utils import dataSearch, qrGen

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the QR Hunt"


@app.route("/get-info/<code>")
def get_info(code):
    id = dataSearch.search_id(code)
    data = dataSearch.search_data(id)
    return jsonify(data)


@app.route("/qr/<code>")
def qr(code):
    path = qrGen.generate_qr(code, "qr.png")
    return send_file(path, mimetype="image/png")


if __name__ == "__main__":
    app.run(debug=True)
