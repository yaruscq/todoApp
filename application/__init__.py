# __init__

from flask import Flask
from flask_pymongo import PyMongo
from pymongo.mongo_client import MongoClient


app = Flask(__name__)

app.config['SECRET_KEY'] = '769999a2e3322d82f95e8287ccdced4eb31490c5'
app.config["MONGO_URI"] = 'mongodb+srv://qq:tGh0v7dvlMmDIvtS@cluster0.pttm2.mongodb.net/cqdatabase?retryWrites=true&w=majority&appName=Cluster0'


# Create a new client and connect to the server
# mongodb database
mongodb_client = PyMongo(app)
db = mongodb_client.db
todos_collection = db.todos_flask # type: ignore


from application import routes

# # Send a ping to confirm a successful connection
# try:
#     mongodb_client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)