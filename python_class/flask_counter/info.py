from flask import (Flask, render_template, session)


app = Flask(__name__)
app.secret_key = "jfal4i5;q5h';sjkj;lkj;flhbumimimj[08hjdaf/45l'fjkjfd"


@app.route('/')
def index():
    if 'counter' not in session:
        session['counter'] = 0
    else:
        session['counter'] += 1
    print session.__dict__
    return render_template('index.html')


app.run(debug=True) 

