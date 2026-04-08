from pymongo import MongoClient
import os

# MongoDB Atlas connection
MONGO_URI = os.environ.get("MONGO_URI")

if not MONGO_URI:
    raise ValueError("MONGO_URI environment variable is not set")

client = MongoClient(MONGO_URI)

# Database
db = client["animal_charity"]

# Collections
contacts_collection = db["contacts"]
donations_collection = db["donations"]