from flask import Flask, request, redirect, render_template, session, flash
from mysqlconnection import MySQLConnector
import re
import md5
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
app = Flask(__name__)
mysql = MySQLConnector(app,'login')
app.secret_key = "thisisthebestkeyeveromgwhyisitsoamazingitissocool"

email_store = str('sam@asdfas.com')

query = 'SELECT email FROM users WHERE users.email =' + email_store
x =  mysql.query_db(query)
print  x

app.run(debug=True)