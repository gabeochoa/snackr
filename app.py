#!/usr/bin/env python
from flask import Flask, render_template, session, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
import mongoconn

loggedin = True

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/inventory')
def inventory(database = mongoconn.getAll(mongoconn.openDB())):
    if( not loggedin ):
        return "please log in"
    print(database)
    return render_template('inventory.html', inv = database)

if __name__ == '__main__':
    app.run(debug=True)
