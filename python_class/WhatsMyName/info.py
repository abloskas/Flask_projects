from flask import (Flask, render_template, redirect, request, url_for)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route("/process", methods=['POST'])
def process():
    print(request.form['your-name'])
    return redirect(url_for("index"))


app.run(debug=True)  