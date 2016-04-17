#!/usr/bin/env python
from flask import Flask, render_template, session, request

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
    return jason

@app.route('/inventory')
def inventory(database = mongoconn.openDB()):
    if( not loggedin ):
        return "please log in"
    inv = mongoconn.getAll(database)
    print(inv)
    return render_template('inventory.html', inv = inv)

port = int(os.environ.get('PORT', 5000))
if __name__ == '__main__':
    app.run(debug=True, port)
