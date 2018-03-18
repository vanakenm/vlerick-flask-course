from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


@app.route("/profile/<name>")
def profile(name):
    return "I'm %s" % name
