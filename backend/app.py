from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient
import os

app = Flask(__name__)
CORS(app)

# MongoDB connection
MONGO_URI = os.environ.get("MONGO_URI")

client = None
db = None
contacts = None
donations = None

try:
    if MONGO_URI:
        client = MongoClient(MONGO_URI)
        db = client["animal_charity"]
        contacts = db["contacts"]
        donations = db["donations"]
        print("✅ MongoDB Connected Successfully")
    else:
        print("❌ MONGO_URI not found")
except Exception as e:
    print("❌ MongoDB Connection Error:", e)


@app.route("/")
def home():
    return jsonify({"message": "Backend is running!"})


# ✅ ONLY THIS PART CHANGED (REAL LOGIN USING MONGODB)
@app.route("/api/login", methods=["POST"])
def login():
    try:
        data = request.get_json()
        email = data.get("email")
        password = data.get("password")

        if db is None:
            return jsonify({"success": False})

        user = db["users"].find_one({
            "email": email,
            "password": password
        })

        if user:
            return jsonify({"success": True})
        else:
            return jsonify({"success": False})

    except Exception as e:
        print("Login Error:", e)
        return jsonify({"success": False})


@app.route("/api/contact", methods=["POST"])
def contact():
    try:
        data = request.get_json()

        if contacts is not None:
            contacts.insert_one({
                "name": data.get("name"),
                "email": data.get("email"),
                "message": data.get("message")
            })

        return jsonify({"success": True})
    except Exception as e:
        print("Contact Save Error:", e)
        return jsonify({"success": False, "message": "Failed to save contact"}), 500


@app.route("/api/donations", methods=["POST"])
def donate():
    try:
        data = request.get_json()

        if donations is not None:
            donations.insert_one({
                "name": data.get("name"),
                "email": data.get("email"),
                "amount": data.get("amount"),
                "message": data.get("message")
            })

        return jsonify({"success": True})
    except Exception as e:
        print("Donation Save Error:", e)
        return jsonify({"success": False, "message": "Failed to save donation"}), 500


@app.route("/api/admin/contacts")
def get_contacts():
    try:
        if contacts is not None:
            all_contacts = list(contacts.find({}, {"_id": 0}))
            return jsonify(all_contacts)

        return jsonify([])
    except Exception as e:
        print("Fetch Contacts Error:", e)
        return jsonify([])


@app.route("/api/admin/donations")
def get_donations():
    try:
        if donations is not None:
            all_donations = list(donations.find({}, {"_id": 0}))
            return jsonify(all_donations)

        return jsonify([])
    except Exception as e:
        print("Fetch Donations Error:", e)
        return jsonify([])


# ✅ UPDATED: Recent Donations API (REAL DATA FROM MONGODB)
@app.route("/api/recent-donations")
def recent_donations():
    try:
        if donations is not None:
            recent = list(
                donations.find({}, {"_id": 0})
                .sort("_id", -1)
                .limit(5)
            )
            return jsonify(recent)

        return jsonify([])
    except Exception as e:
        print("Recent Donations Error:", e)
        return jsonify([])


if __name__ == "__main__":
    app.run()