import pymongo
from pymongo import MongoClient
from keys import MONGO_URL

def mongoconn():
    connection = MongoClient(MONGO_URL)
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