from pymongo import MongoClient

# MongoDB Atlas connection
client = MongoClient("mongodb+srv://admin:animal123@cluster0.qzdofhr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

# create database
db = client["animal_charity"]

# collections
contacts_collection = db["contacts"]
donations_collection = db["donations"]