from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)  # Allow cross-origin requests (e.g., from Android app)

# Initialize default message
latest_message = {
    "receiver": "client",
    "text": "—null"
}

@app.route("/send", methods=["POST", "GET"])
def receive():
    global latest_message
    data = request.get_json()

    # Validate and update message
    if not data or "receiver" not in data or "text" not in data:
        return jsonify({"status": "error", "message": "Invalid payload"}), 400

    latest_message = {
        "receiver": data["receiver"],
        "text": data["text"]
    }

    return jsonify({"status": "received", "data": latest_message})

@app.route("/latest", methods=["POST", "GET"])
def get_latest():
    return jsonify(latest_message)

@app.route("/", methods=["GET"])
def home():
    return "Relay server running."

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
