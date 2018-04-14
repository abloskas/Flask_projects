from flask import (Flask, render_template, request)

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/result", methods=["POST"])
def result():
    return render_template("result.html", form=request.form)

app.run(debug=True)      