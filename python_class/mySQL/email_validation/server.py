from flask import Flask, render_template, request, redirect, session, flash, url_for
# from datetime import datetime
from mysqlconnection import MySQLConnector
import re
EMAIL_REGEX = re.compile(r"^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")

app = Flask(__name__)
mysql = MySQLConnector(app, 'email_validation')
app.secret_key = 'thisisanawesomekeywhatwhatwhatwhatwhat'

@app.route('/')
def index():
    return render_template('index.html')

# @app.route('/add', methods=["POST"])
# def add():
   
#     flash('THANKS FOR YOUR EMAIL!', 'success')
#     return redirect('/success')

@app.route('/validate', methods=['POST'])
def result():
    if request.method == 'POST':
        passFlag = True
        if len(request.form['email']) < 1:
            flash('ERROR! EMAIL IS BAD!', 'failure')
            passFlag = False
        elif not EMAIL_REGEX.match(request.form['email']):
            flash('INVALID EMAIL FORMAT.TRY AGAIN. DUH', 'failure')
            passFlag = False
            return redirect('/')
        if passFlag == True:
            query = "INSERT INTO email (email, created_at, updated_at) VALUES (:email, NOW(), NOW())"
            data = {
                'email': request.form['email']
            }
            mysql.query_db(query, data)
            flash('THANKS FOR YOUR EMAIL!', 'success')
            return redirect('/success')

@app.route('/success')
def success():
    query = "SELECT * FROM email"
    email = mysql.query_db(query)
    return render_template('success.html', emails=email)


app.run(debug=True)