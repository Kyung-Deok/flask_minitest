
from flask import Flask, request, render_template
from flask_mongoengine import mongoengine

# # from pymongo import MongoClient
# URI = "mongodb+srv://leekd:0914@test1.sqi24.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
# client = MongoClient(URI)

# print(client.list_database_names)

app = Flask(__name__)
DB_URI = 'mongodb+srv://leekd:0914@test1.sqi24.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
app.config['MONGODB_HOST'] = DB_URI
mongo = mongoengine(app)

if __name__ == '__main__':
    app.run()