from flask import Flask, request, jsonify
from flask_cors import CORS
from config import contacts_collection, donations_collection

app = Flask(__name__)
CORS(app)

# Home route
@app.route('/api', methods=['GET'])
def home():
    return jsonify({"message": "Server is running!"})


# Contact route
@app.route('/api/contact', methods=['POST'])
def contact():
    data = request.get_json()

    contacts_collection.insert_one({
        "name": data.get("name"),
        "email": data.get("email"),
        "message": data.get("message")
    })

    return jsonify({"success": True})


# Donation route
@app.route('/api/donations', methods=['POST'])
def donate():
    data = request.get_json()

    donations_collection.insert_one({
        "name": data.get("name"),
        "email": data.get("email"),
        "amount": data.get("amount"),
        "message": data.get("message")
    })

    return jsonify({"success": True})


# Login route
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email", "")
    password = data.get("password", "")

    if "@" in email and password.isdigit():
        return jsonify({"success": True})

    return jsonify({"success": False})


# Admin routes
@app.route('/api/admin/contacts', methods=['GET'])
def get_contacts():
    contacts = list(contacts_collection.find({}, {"_id": 0}))
    return jsonify(contacts)


@app.route('/api/admin/donations', methods=['GET'])
def get_donations():
    donations = list(donations_collection.find({}, {"_id": 0}))
    return jsonify(donations)


