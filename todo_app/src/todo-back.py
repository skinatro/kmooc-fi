"""
Backend for the ToDo app using MongoDB
"""
import os
from flask import Flask, request, jsonify, redirect
from pymongo import MongoClient
from bson import ObjectId

app = Flask(__name__)

# MongoDB connection
username = os.environ.get("MONGO_USERNAME")
password = os.environ.get("MONGO_PASSWORD")
host = os.environ.get("MONGO_HOST")
db_name = os.environ.get("MONGO_DB")

MONGO_URI = f"mongodb://{username}:{password}@{host}:27017/{db_name}?authSource=admin"
client = MongoClient(MONGO_URI)
db = client[db_name]  
todos_collection = db["todos"]


@app.route('/todos', methods=['GET', 'POST'])
def todos():
    """
    GET -> Retrieve todos from MongoDB
    POST -> Add a new todo to MongoDB
    """
    if request.method == 'GET':
        todos = list(todos_collection.find({}, {"_id": 1, "task": 1}))
        # Convert ObjectId to string
        for t in todos:
            t["_id"] = str(t["_id"])
        return jsonify(todos)

    if request.method == 'POST':
        new_task = request.form.get('todo')
        if new_task:
            todos_collection.insert_one({"task": new_task})
        return redirect("/")

if __name__ == '__main__':
    PORT = os.environ.get("PORT")
    app.run(host="0.0.0.0", port=int(PORT), debug=False)
