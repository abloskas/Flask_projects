from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'login')
app.secret_key = "thisisthebestkeyeveromgwhyisitsoamazingitissocool"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    if len(request.form['first_name']) < 3:
        flash('PLEASE ENTER FULL NAME')
    elif len(request.form['last_name']) < 3:
        flash('PLEASE ENTER FULL LAST NAME') 
    elif not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")  
    elif request.form['password'] != request.form['password2']:
        flash('PLEASE MAKE SURE PASSWORDS MATCH')
    else:
        data = {
            'First_Name': request.form['first_name'],
            'Last_Name': request.form['last_name'],
            'Email': request.form['email'],
            'Password': md5.new(request.form['password']).hexdigest()
        }
        query = 'INSERT INTO users(first_name, last_name, email, password) VALUES (:First_Name, :Last_Name, :Email, :Password)'

        mysql.query_db(query, data)
    return redirect('/')

@app.route('/login', methods=["POST"])   
def login():
    if not EMAIL_REGEX.match(request.form['email']):
        flash("Invalid Email Address!")  
    elif len(request.form['password']) < 1:
        flash('enter password pls')   
    else:
        data = {
            'email': request.form['email'],
            'Password': md5.new(request.form['password']).hexdigest()
        } 
        query = 'SELECT email FROM users WHERE users.email = :email'
        if mysql.query_db(query, data) == []:
            flash('you are not a user')
            return redirect('/')
        email=(mysql.query_db(query, data))[0]['email'] 
        query = 'SELECT password FROM users WHERE users.email = :email'
        password=(mysql.query_db(query, data))[0]['password'] 
        if request.form['email'] == email and password == md5.new(request.form['password']).hexdigest():
            return render_template('index.html', email=email)
        elif password != md5.new(request.form['password']).hexdigest():
            flash('username OR password is WRONG')
        elif email_check == []:
            flash('you fucked up')
    return redirect('/')


app.run(debug=True)