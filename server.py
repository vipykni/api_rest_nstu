from flask import Flask, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
import random
import hashlib
from datetime import datetime
import sqlite3
from base import (User, Log, Teacher, TeacherShedule, Group, Structure, Level, Faculty, Auditory, Corpus, Day, Time)


# connection
app = Flask(__name__)
# SQLite connect
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///shedule.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)



@app.route('/')
def home():
    return render_template("home.html")

@app.route('/user/<string:name>/<int:id>')
def user(name,id):
    return "User Page " + name + " - " + str(id)

@app.route('/regisration', methods=['POST','GET'])
def register():
    if request.method == "POST":
        name = request.form['name']
        login = request.form['login']
        password = request.form['password']
        token = hashlib.md5(bytes(random.randint(1, 10000000))).hexdigest()
        expiration = (datetime.now() + timedelta(days=30))
        user_id = int(User.query.order_by(User.id.desc()).first().id) + 1
        newUser = User(id=user_id, name=name, login=login, password=password, token=token,  expiration=expiration)
        try:
            db.session.add(newUser)
            db.session.commit()
            return redirect('/')
        except:
            return print("При добавлении возникла ошибка")
    return render_template("regisration.html")

def auth(ulogin, upassword):
    user_list = User.query.order_by(User.id).all()
    user_password = None
    for el in user_list:
        if ulogin == el.login:
            user_password = el.password
            break
    else:
        print('Login Failed')
    if upassword == user_password:
        print('Login Succsess')
    return


def userReg(login):
    user_list = User.query.order_by(User.id).all()
    for el in user_list:
        if login != el.login:
            return False
    return True

@app.route('/authorization', methods=['POST','GET'])
def authorization():
    if request.method == "POST":
        login = request.form['login']
        password = request.form['password']
        auth(login, password)

    return render_template("authorization.html")

@app.route('/teachers', methods=['GET', 'POST'])
def teachers():
    if request.method == "GET":
        print('Get method')
        teacher_list = Teacher.query.order_by(Teacher.id).all()
        print(teacher_list[0].name)
    else:
        print("Post method")

    return render_template('teachers.html', teacher_list=teacher_list)

@app.route('/facult', methods=['POST','GET'])
def facult():
    if request.method == "GET":
        print('Get method')
        Faculty_list = Faculty.query.order_by(Faculty.id).all()
        print(Faculty_list[0].name)
    else:
        print("Post method")
    return render_template('facult.html', Faculty_list=Faculty_list)



if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
