
from flask import Flask
from flask_mongoengine import MongoEngine

# from pymongo import MongoClient
# client = pymongo.MongoClient("mongodb+srv://leekd:0914@test1.sqi24.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# db = client.test

app = Flask(__name__)
DB_URI = 'mongodb+srv://leekd:0914@test1.sqi24.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
app.config['MONGODB_HOST'] = DB_URI
db = MongoEngine(app)
if __name__=='__main__':
    app.run()