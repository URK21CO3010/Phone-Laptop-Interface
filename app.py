# app.py
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests from Android app

latest_message = ""

@app.route("/send", methods=["POST"])
def receive():
    global latest_message
    data = request.get_json()
    latest_message = data.get("text", "")
    return jsonify({"status": "received", "text": latest_message})

@app.route("/latest", methods=["GET"])
def get_latest():
    return jsonify({"text": latest_message})

if __name__ == "__main__":
    app.run()
