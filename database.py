
from os import name
from flask import Flask, request, render_template
from pymongo import MongoClient
from form import RegistrationForm

DB_URI = 'mongodb+srv://leekd:0914@cluster0.xbwiu.mongodb.net/myFirstDatabase?retryWrites=true&w=majority'
client= MongoClient(DB_URI)
__
#db 생성
db = client['miniproj']
#collection 생성
user_col = db['user_col']

user_schema = {
    "ID" : "aa",
    "PASSWORD" : "bb",
    "EMAIL" : "cc"
}

# # test document 생성
# testdoc = {"id":"testid", "email":"testemail", "password":"testpasswrd"}

# test = user_col.insert_one(testdoc)
print(form)