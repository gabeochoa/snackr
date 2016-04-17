#!/usr/bin/env python
from flask import Flask, render_template, session, request, redirect, url_for
import os
import urllib
import base64

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
import mongoconn

NDID = {
    "peppers":"11333",
    "bread":"18064",
    "carrots":"11124",
    "broccoli":"11741",
    "grapes":"09132",
    "cookies":"28027",
    "watermelon":"09326",
    "avocado":"09038"
}

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
    #print(inv)
    #print(inv[0])
    # nutri = []
    # for item in inv:
    #     aa = urllib.urlretrieve("http://api.nal.usda.gov/ndb/reports/?ndbno=" + NDID[item["name"]] +"&type=f&format=json&api_key=xoNloOitF8uXEhuREu11T7y64Lz1tntsZGHcZwPs")
    #     nutri.append(aa)

    #http://api.nal.usda.gov/ndb/reports/?ndbno={{ food['NDID']}}&type=f&format=json&api_key=xoNloOitF8uXEhuREu11T7y64Lz1tntsZGHcZwPs
    #
    return render_template('inventory.html', inv = inv)#, nutri = nutri)


@app.route("/delete/<name>", methods = ['POST'])
def delete(name, database = mongoconn.openDB()):
    if request.method == 'POST':
        data = request.form 
    mongoconn.removeAll(database, request.form['submit'])
    return redirect(url_for('inventory'))










port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=port)


