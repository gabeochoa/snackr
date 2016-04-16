#!/usr/bin/env python
from flask import Flask, render_template, session, request

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'

loggedin = True

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/inventory')
def inventory():
    if( not loggedin ):
        return "please log in"
    return render_template('inventory.html')

if __name__ == '__main__':
    app.run(debug=True)
