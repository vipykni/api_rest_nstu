from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import datetime


# connection
app = Flask(__name__)
# SQLite connect
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shedule.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


def __repr__(self):
    return 'Shedule %r' % self.id


@app.route('/')
def home():
    return render_template("home.html")


@app.route('/regisration', methods=['POST','GET'])
def register():
    if request.method == "POST":
        name = request.form['name']
        login = request.form['login']
        password = request.form['password']
        token = random.getrandbits(128)
        print(name)
        print(login)
        print(password)
        print(token)
    return render_template("regisration.html")

@app.route('/authorization', methods=['POST','GET'])
def authorization():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        token = random.getrandbits(128)
        print(login)
        print(password)
        print(token)
    return render_template("authorization.html")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
