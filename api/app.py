from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# MongoDB connection
MONGO_URI = os.environ.get("MONGO_URI")

contacts = None
donations = None

if MONGO_URI:
    client = MongoClient(MONGO_URI)
    db = client["animal_charity"]
    contacts = db["contacts"]
    donations = db["donations"]


@app.route("/")
def root():
    return jsonify({"message": "Flask backend is running!"})


@app.route("/api")
def api_home():
    return jsonify({"message": "Server is running!"})


@app.route("/api/contact", methods=["POST"])
def contact():
    data = request.get_json()

    if contacts is not None:
        contacts.insert_one(data)

    return jsonify({
        "success": True,
        "message": "Contact form submitted successfully"
    })


@app.route("/api/donations", methods=["POST"])
def donate():
    data = request.get_json()

    if donations is not None:
        donations.insert_one(data)

    return jsonify({
        "success": True,
        "message": "Donation submitted successfully"
    })


@app.route("/api/login", methods=["POST"])
def login():
    data = request.get_json()
    email = data.get("email", "")
    password = data.get("password", "")

    # Login rule:
    # Any email containing @
    # Any password that is only numbers
    if "@" in email and password.isdigit():
        return jsonify({
            "success": True,
            "message": "Login successful"
        })

    return jsonify({
        "success": False,
        "message": "Invalid email or password"
    })


@app.route("/api/admin/contacts")
def get_contacts():
    if contacts is None:
        return jsonify([])

    return jsonify(list(contacts.find({}, {"_id": 0})))


@app.route("/api/admin/donations")
def get_donations():
    if donations is None:
        return jsonify([])

    return jsonify(list(donations.find({}, {"_id": 0})))


if __name__ == "__main__":
    app.run(debug=True)