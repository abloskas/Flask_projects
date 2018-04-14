from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')



@app.route('/ninja')
def ninjaPic():
    return render_template('ninja.html')
    
@app.route('/ninja/<color>')
def ninjas(color = None):
    # if color ==
    if color == 'blue':
        return render_template('blue.html')    
    elif color == 'red':
        return render_template('red.html') 
    elif color == 'orange':
        return render_template('orange.html')  
    elif color == 'purple':
        return render_template('purple.html')  
    else: 
        return render_template('notapril.html')  

 
    
app.run(debug=True)  