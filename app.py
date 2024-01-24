# app.py

from pymongo import MongoClient

import datetime


client = MongoClient("mongodb://mongodb:27017/")

db = client.testdb

collection = db.testcollection


# Add data with timestamp

current_time = datetime.datetime.now()

collection.insert_one({"message": "Hello from Python to MongoDB!", "timestamp": current_time})


# Read data

for doc in collection.find():

    print(doc)
