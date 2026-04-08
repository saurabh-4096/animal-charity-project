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

    contact_data = {
        "name": data.get("name"),
        "email": data.get("email"),
        "message": data.get("message")
    }

    contacts_collection.insert_one(contact_data)

    return jsonify({
        "success": True,
        "message": "Contact saved successfully"
    })


# Donation route
@app.route('/api/donations', methods=['POST'])
def donate():
    data = request.get_json()

    donation_data = {
        "name": data.get("name"),
        "email": data.get("email"),
        "amount": data.get("amount"),
        "message": data.get("message")
    }

    donations_collection.insert_one(donation_data)

    return jsonify({
        "success": True,
        "message": "Donation saved successfully"
    })


# Login route
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    email = data.get("email")
    password = data.get("password")

    if email == "admin@paws.com" and password == "1234":
        return jsonify({"success": True})

    return jsonify({
        "success": False,
        "message": "Invalid email or password"
    })


# Admin route to get contacts
@app.route('/api/admin/contacts', methods=['GET'])
def get_contacts():
    contacts = list(contacts_collection.find({}, {"_id": 0}))
    return jsonify(contacts)


# Admin route to get donations
@app.route('/api/admin/donations', methods=['GET'])
def get_donations():
    donations = list(donations_collection.find({}, {"_id": 0}))
    return jsonify(donations)


if __name__ == "__main__":
    app.run(debug=True)