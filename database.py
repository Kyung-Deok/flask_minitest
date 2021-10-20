
from flask import Flask, request, render_template
from flask_pymongo import PyMongo

# # from pymongo import MongoClient
# URI = "mongodb+srv://leekd:0914@test1.sqi24.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
# client = MongoClient(URI)

# print(client.list_database_names)

app = Flask(__name__)
DB_URI = 'mongodb+srv://leekd:0914@test1.sqi24.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
app.config['MONGO_URI'] = DB_URI
mongo = PyMongo(app)

