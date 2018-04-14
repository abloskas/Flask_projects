from flask import Flask, request, redirect, render_template, session, flash, url_for
from mysqlconnection import MySQLConnector
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'wall')
app.secret_key = "thisisthebestkeyeveromgwhyisitsoamazingitissocool"

@app.route('/')
def home():
    if 'id' in session:
        return redirect('/wall')
    else:
        return render_template('/login.html')

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
            flash('You are not registered. Please register.')
            return redirect('/')
        email=(mysql.query_db(query, data))[0]['email'] 
        query = 'SELECT password FROM users WHERE users.email = :email'
        password=(mysql.query_db(query, data))[0]['password'] 
        query = 'SELECT * FROM users WHERE users.email = :email'
        aUser = (mysql.query_db(query, data)[0])
        print aUser
        session['id'] = aUser['id']
        session['name'] = aUser['first_name']
        print session['name']
        if request.form['email'] == email and password == md5.new(request.form['password']).hexdigest():
            session['log'] = True
            return redirect('/wall')
        elif password != md5.new(request.form['password']).hexdigest():
            flash('username OR password is WRONG')
        elif email_check == []:
            flash('you done goofed up')
    return redirect('/')

@app.route('/posted', methods=['POST'])
def posted():
    print 'hello'
    print request.form['comment']
    data = {
        'message': request.form['comment'],
        'id': session['id']
    }
    query = "INSERT INTO messages (message, users_id) VALUES (:message, :id)"
    mysql.query_db(query, data) 
    return redirect('/wall')

@app.route('/wall')
def wall():
    if session['log'] != True:
        redirect('/')
    query = 'SELECT * FROM wall.messages LEFT JOIN users ON messages.users_id = users.id ORDER BY messages.created_at DESC'
    all_comments = mysql.query_db(query)
    query = 'SELECT * FROM comments LEFT JOIN messages ON messages.m_id = comments.messages_id LEFT JOIN users ON users.id = comments.users_id'
    all_replies = mysql.query_db(query)
    print all_replies
    # print all_comments
    return render_template('index.html', comments=all_comments, all_replies=all_replies)  

@app.route('/reply', methods=["POST"])
def reply():
    data = {
        'reply': request.form['reply'],
        'id': session['id'],
        'm_id': request.form['message_id']
    }
    query = 'INSERT INTO comments (comment, messages_id, users_id) VALUES (:reply, :m_id, :id)'
    mysql.query_db(query, data)
    return redirect('/wall')


@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')    


app.run(debug=True)