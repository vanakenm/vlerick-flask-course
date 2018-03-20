from flask import Flask
from flask import render_template
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template('ask.html')


@app.route("/candrink")
def hello():
    age = int(request.args.get('age', ''))
    return render_template('candrink.html', age=age)
