#!/usr/bin/env python
from flask import Flask, render_template, session, request, redirect, url_for
import os
import urllib
import base64
from urllib2 import Request, urlopen, URLError
import mongoconn 
import json 

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'


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
    print('ey')
    if request.method == 'POST':
        data = request.form 
    mongoconn.removeAll(database, name)
    return redirect(url_for('inventory'))

@app.route('/nutrition/<name>')
def nutrition(name):
    apiurl = "http://api.nal.usda.gov/ndb/reports/?ndbno=" + NDID[name] +"&type=f&format=json&api_key=xoNloOitF8uXEhuREu11T7y64Lz1tntsZGHcZwPs"
    request = Request(apiurl)
    stats = []
    try:
        response = urlopen(request)
        jj = response.read()
        jsonout = json.loads(jj)
        stats.append(jsonout["report"]["food"]["name"])#get name
        for nut in jsonout["report"]["food"]["nutrients"]:
            if(nut["name"] in ["Energy", "Protien", "Total lipid (fat)"]):
                stats.append( str(nut["value"]) + " " + nut["unit"])
    except URLError, e:
        print 'Got an error code:', e
    return render_template('nutrients.html', name = name, stats = stats)


port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True,port=port)














