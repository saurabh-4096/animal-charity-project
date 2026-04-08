from pymongo import MongoClient
import os

MONGO_URI = os.environ.get("MONGO_URI")

if not MONGO_URI:
    raise Exception("MONGO_URI environment variable is missing")

client = MongoClient(MONGO_URI)

db = client["animal_charity"]

contacts_collection = db["contacts"]
donations_collection = db["donations"]