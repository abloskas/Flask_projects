from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
app = Flask(__name__)
mysql = MySQLConnector(app,'friends')
app.secret_key = "thisisthebestkeyeveromgwhyisitsoamazingitissocool"

@app.route('/')
def index():
    query = "SELECT * FROM friend"                           # define your query
    friends = mysql.query_db(query)                           # run query with query_db()
    return render_template('index.html', friends=friends) # pass data to our template


@app.route('/friends', methods=['POST'])
def create():
    # Write query as a string. Notice how we have multiple values
    # we want to insert into our query.
    query = "INSERT INTO friend (name, age, created_at, updated_at) VALUES (:name, :age,  NOW(), NOW())"
    # We'll then create a dictionary of data from the POST data received.
    data = {
             'name': request.form['name'],
             'age': request.form['age']
           }
    # Run query, with dictionary values injected into the query.
    mysql.query_db(query, data)
    return redirect('/')

app.run(debug=True)