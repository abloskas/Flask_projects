from flask import Flask, render_template, session, request, redirect 
import random 

app = Flask(__name__)
app.secret_key = 'forscoreandsevenyearsago'

@app.route('/')
def index():
    session['num'] = random.randrange(0, 101)
    print session['num']
    return render_template("index.html")

@app.route('/guess', methods=['POST'])
def result():
    if int(request.form['correct']) == session['num']:
        answer = "CORRECT!!!"
        session['class'] = 'correct'
    elif int(request.form['correct']) < session['num']:
        answer = "Guess is TOO LOW"
        session['class'] = 'wrong'
    else:
        answer = "Guess is TOO HIGH"
        session['class'] = 'wrong'
    session['answer'] = answer    
    return redirect("/")
app.run(debug=True)
