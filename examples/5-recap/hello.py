from flask import Flask
from flask import render_template
from flask import request
import json

app = Flask(__name__)


@app.route("/")
def index():
    with open('data.json') as json_data:
        d = json.load(json_data)
        print(d)
        return render_template('index.html', data=d)
