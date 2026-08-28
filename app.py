from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to the QR Hunt"


if __name__ == "__main__":
    app.run(debug=True)
