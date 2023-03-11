
# A very simple Flask Hello World app for you to get started with...
from flask import render_template, Flask, url_for, request
from flask_cors import CORS

app = Flask(__name__)

cors = CORS(app)

@app.route('/')
def hello_world():
    return render_template("index.html")

if __name__ == "__main__":
    url_for('static', filename='static\js\index.js')
    url_for('static', filename='static\css\index.css')