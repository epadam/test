from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def hello () -> str:
    return render_template("home.html") 

@app.route('/predict', methods=['POST'])
def predict ():
    return 'text'

if __name__=="__main__":
    app.run("0.0.0.0", port=80, debug=True)
