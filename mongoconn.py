import pymongo
from pymongo import MongoClient
from keys import READ_MONGO_URL, WRITE_MONGO_URL
import json 
import bson 
import base64

def mongoconn():
    try:
        connection = MongoClient(WRITE_MONGO_URL)
    except:
        print("COULD NOT AUTHENTICATE")
        return None
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

def addJson(db, bobj):
    obj = base64.b64decode(bobj)
    data = (json.loads(obj))[0]
    print(data)
    db["food"].insert_one(data)
    #print(obj)