from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# MongoDB
MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["animal_charity"]

contacts = db["contacts"]
donations = db["donations"]


@app.route('/api')
def home():
    return jsonify({"message": "Server is running!"})


@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()

    contacts.insert_one(data)

    return jsonify({"success": True})


@app.route('/api/donations', methods=['POST'])
def donate():
    data = request.get_json()

    donations.insert_one(data)

    return jsonify({"success": True})


# ✅ LOGIN (your custom rule)
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email", "")
    password = data.get("password", "")

    if "@" in email and password.isdigit():
        return jsonify({"success": True})

    return jsonify({"success": False})


@app.route('/api/admin/contacts')
def get_contacts():
    return jsonify(list(contacts.find({}, {"_id": 0})))


@app.route('/api/admin/donations')
def get_donations():
    return jsonify(list(donations.find({}, {"_id": 0})))


app = app