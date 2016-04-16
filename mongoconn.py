import pymongo
from pymongo import MongoClient
from keys import READ_MONGO_URL, WRITE_MONGO_URL
import json 
import bson 

def mongoconn():
    connection = MongoClient(WRITE_MONGO_URL)
    db = connection.get_default_database()
    print db.collection_names()
    return db#['collection']

def openDB():
    return mongoconn()

def getAll(db):
    inv = []
    for pl in db["food"].find({}):
        inv.append(pl)
    return inv

def addJson(db, obj):
    data = (json.loads(obj))[0]
    print(data)
    db["food"].insert_one(data)
    #print(obj)