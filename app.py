#!/usr/bin/env python
from flask import Flask, render_template, session, request
import os
import urllib
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
import mongoconn

loggedin = True

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add/<jason>')
def add(jason, database = mongoconn.openDB()):
    mongoconn.addJson(database, jason)
    return base64.b64decode(jason)

@app.route('/inventory')
def inventory(database = mongoconn.openDB()):
    if( not loggedin ):
        return "please log in"
    inv = mongoconn.getAll(database)
    print(inv)
    #print(inv[0])
    #for( item in inv ):

    #http://api.nal.usda.gov/ndb/reports/?ndbno={{ food['NDID']}}&type=f&format=json&api_key=xoNloOitF8uXEhuREu11T7y64Lz1tntsZGHcZwPs
    #urllib.urlretrieve("http://api.nal.usda.gov/ndb/reports/?ndbno=" +  +"&type=f&format=json&api_key=xoNloOitF8uXEhuREu11T7y64Lz1tntsZGHcZwPs")

    return "ss"
    #return render_template('inventory.html', inv = inv)

port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=port)
