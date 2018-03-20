from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('ask.html')


@app.route("/candrink", methods=['POST'])
def hello():
    age = int(request.form['age'])
    return render_template('candrink.html', age=age)
