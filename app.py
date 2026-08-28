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
    qr_img = qrGen.generate_qr(code)
    return send_file(qr_img, mimetype="image/png", download_name="qr_code.png")


if __name__ == "__main__":
    app.run(debug=True)
