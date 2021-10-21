
from flask import Flask, request, render_template
from flask_mongoengine import MongoEngine

# app = Flask(__name__)
DB_URI = 'mongodb+srv://leekd:0914@test1.sqi24.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
# app.config['MONGODB_HOST'] = DB_URI
# mongo = mongoengine(app)

# if __name__ == '__main__':
#     app.run()

# from flask_pymongo import PyMongo
# app = Flask(__name__)
# app.config["MONGO_URI"] = DB_URI
# mongo = PyMongo(app)

app = Flask(__name__)
class TestConfig():
    DEBUG = True
    MONGODB_SETTINGS = {
        'db': 'product',
        'host': DB_URI
    }

if __name__ == '__main__':
    app.config.from_object(TestConfig)
    db = MongoEngine()
    db.init_app(app)
    app.run(host='localhost', port=3000)