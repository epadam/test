from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello () -> str:
    return render_template("home.html") 

@app.route('/predict', methods=['POST'])
def predict ():
    return 'text'

app.run(debug=True)
