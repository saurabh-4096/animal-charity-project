from pymongo import MongoClient
import os

# MongoDB Atlas connection
MONGO_URI = os.environ.get("MONGO_URI")

client = MongoClient(MONGO_URI)

# create database
db = client["animal_charity"]

# collections
contacts_collection = db["contacts"]
donations_collection = db["donations"]