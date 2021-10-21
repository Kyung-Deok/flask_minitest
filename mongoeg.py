from flask_mongoengine import MongoEngine
from flask import Flask


class TestConfig():
    DEBUG = True
    MONGODB_SETTINGS = {
    'db': 'product',
    'host': "mongodb+srv://leekd:0914@test1.sqi24.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
    }


if __name__ == '__main__':
    app = Flask(__name__)
    app.config.from_object(TestConfig)
    db = MongoEngine()
    db.init_app(app)
    app.run(host='localhost', port=3000)
