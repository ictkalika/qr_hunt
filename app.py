from flask import Flask, jsonify, render_template, request, send_file

from utils import data, qrGen

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the QR Hunt"


@app.route("/get-info/<code>")
def get_info(code):
    id = data.search_id(code)
    data = data.search_data(id)
    return jsonify(data)


@app.route("/qr/<code>")
def qr(code):
    qr_img = qrGen.generate_qr(code)
    return send_file(qr_img, mimetype="image/png", download_name="qr_code.png")


@app.route("/upload", methods=["POST"])
def upload():
    body = request.get_json()
    question = body.get("question")
    answer = body.get("answer")
    if not question or not answer:
        return jsonify({"error": "Question and answer are required"}), 400

    response = data.add_data(question, answer)

    if "error" in response:
        return jsonify(response), 500

    return jsonify(response), 201


if __name__ == "__main__":
    app.run(debug=True)
