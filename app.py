from flask import Flask, render_template

app = Flask(__name__)

@app.route('/todo')
def todo_form():
    return render_template('todo.html')

from flask import Flask, request, redirect
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient("mongodb+srv://lakshjain1:1234@cluster.mongodb.net/?retryWrites=true&w=majority")
db = client["todo_db"]
collection = db["items"]

@app.route('/submittodoitem', methods=['POST'])
def submit_item():
    item_name = request.form.get('itemName')
    item_description = request.form.get('itemDescription')

    if item_name and item_description:
        collection.insert_one({
            "itemName": item_name,
            "itemDescription": item_description
        })
        return "To-Do item submitted successfully"
    return "Invalid submission", 400
