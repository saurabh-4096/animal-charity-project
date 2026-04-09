from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# MongoDB connection
MONGO_URI = os.environ.get("MONGO_URI")
client = MongoClient(MONGO_URI)
db = client["animal_charity"]

contacts = db["contacts"]
donations = db["donations"]

# Home route
@app.route('/api', methods=['GET'])
def home():
    return jsonify({"message": "Server is running!"})

# Contact route
@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()
    contacts.insert_one(data)
    return jsonify({"success": True, "message": "Contact saved successfully"})

# Donation route
@app.route('/api/donations', methods=['POST'])
def donate():
    data = request.get_json()
    donations.insert_one(data)
    return jsonify({"success": True, "message": "Donation saved successfully"})

# Login route
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email", "")
    password = data.get("password", "")

    # Accept any email with @ and numeric password
    if "@" in email and password.isdigit():
        return jsonify({"success": True})

    return jsonify({
        "success": False,
        "message": "Email must contain @ and password must be numeric only"
    })

# Admin route to get contacts
@app.route('/api/admin/contacts', methods=['GET'])
def get_contacts():
    return jsonify(list(contacts.find({}, {"_id": 0})))

# Admin route to get donations
@app.route('/api/admin/donations', methods=['GET'])
def get_donations():
    return jsonify(list(donations.find({}, {"_id": 0})))

# Required for Vercel
app = app