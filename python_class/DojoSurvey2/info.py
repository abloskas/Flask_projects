from flask import (Flask, render_template, request, flash, redirect, url_for)

app = Flask(__name__)
app.secret_key = "thisisthetimeofyourlifesoliveitwell"

@app.route('/')
def index():
    return render_template('index.html')


@app.route("/result", methods=["POST"])
def result():
    cond = False
    if not request.form['name'] or request.form['comment']:
        flash('YOUR FORM IS EMPTY. PLEASE FILL IN ALL FIELDS.')
        cond = True
    if len(request.form['comment']) > 120:
        flash('YOUR COMMENT IS OVER THE CHARACTER LIMIT.')
        cond = True

        if cond is True:
            return redirect(url_for('index'))

    return render_template("result.html", form=request.form)

app.run(debug=True)