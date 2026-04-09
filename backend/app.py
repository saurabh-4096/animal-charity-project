from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return jsonify({"message": "Backend is running!"})


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email", "")
    password = data.get("password", "")

    if "@" in email and password.isdigit():
        return jsonify({"success": True})
    
    return jsonify({"success": False})


@app.route("/api/contact", methods=["POST"])
def contact():
    return jsonify({"success": True})


@app.route("/api/donations", methods=["POST"])
def donate():
    return jsonify({"success": True})


@app.route("/api/admin/contacts")
def contacts():
    return jsonify([])


@app.route("/api/admin/donations")
def donations():
    return jsonify([])


if __name__ == "__main__":
    app.run()