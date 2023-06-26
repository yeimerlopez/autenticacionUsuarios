from flask import Flask, render_template,request, redirect, url_for, flash
from flask_mysqldb import MySQL

from config import config

#models
from models.ModelUser import ModelUser

#Entities
from models.entities.User import User


app=Flask(__name__)

db=MySQL(app)

@app.route('/')
def index():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    print("antes del if")
    if request.method == 'POST':
        # print(request.form['username'])
        # print(request.form['password'])
        print("dentro del if de login")
        user = User(0, request.form['username'], request.form['password'])
        logged_user = ModelUser.login(db, user)
        if logged_user != None:
            if logged_user.password:
                return redirect(url_for('home'))
            else:
                flash("invalid pasword ... ")
                return render_template('auth/login.html')

        else:
            flash("User not found ...")
            return render_template('auth/login.html')

    else:
        return render_template('auth/login.html')
    
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/register', methods=['GET', 'POST'])
def register():
    print("estoy aca")
    if request.method == 'POST':
        

        user = User(0, request.form['username'], request.form['password'],request.form['fullname'])
        register_user = ModelUser.create_user(db, user)
        if register_user != None:
            
            return redirect(url_for('login'))
           

        else:
                      
           flash("User not create...")
           return redirect(url_for('register.html'))

    else:
        print("me meti por aca")
        return render_template('register.html')
    





if __name__=='__main__':
    app.config.from_object(config['development'])
    app.run()
