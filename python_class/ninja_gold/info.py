from flask import Flask, render_template, redirect, session, request, url_for
from datetime import datetime
import random

app = Flask(__name__)
app.secret_key = 'thisisthefutureman'

@app.route('/')
def index():
    if 'gold' in session:
        session['gold'] = session['gold']
    else:
        session['gold'] = 0    

    try:
        session['activities']
    except KeyError:
        session['activities'] = []     
 

    session['farm'] = random.randrange(10, 21)
    session['cave'] = random.randrange(5, 11)
    session['house'] = random.randrange(2, 6)
    session['casino'] = random.randrange(-50, 51)
    session['temp'] = 0
    return render_template("index.html")

@app.route('/process_money', methods=['POST'])
def money():
    if request.form['building'] == 'farm':
        session['gold'] += session['farm']
        session['temp'] = session['farm']
    if request.form['building'] == 'cave':
        session['gold'] += session['cave']
        session['temp'] = session['cave']
    if request.form['building'] == 'house':
        session['gold'] += session['house']
        session['temp'] = session['house']
    if request.form['building'] == 'casino':
        session['gold'] += session['casino']     
        session['temp'] = session['casino'] 
 
    activity = ''
    if session['temp'] >= 0: 
        activity += 'Earned ' + str(session['temp']) + ' golds from the ' + str(request.form['building'])
    if session['temp'] < 0:
        activity += 'Entered a casino and lost ' + str(session['temp']) + '...Ouch..'     

    time = datetime.now().strftime('%Y/%m/%d %I:%M %p')
    activity += '! (' + str(time) + ')'
    session['activities'].insert(0, activity)
    
    return redirect(url_for('index'))  


app.run(debug=True)    