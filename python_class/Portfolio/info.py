from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('index.html')

@app.route('/aboutme')
def about_me():
    return render_template('aboutme.html')

@app.route('/myprojects')
def projects():
    return render_template('myprojects.html')    
    
app.run(debug=True)  