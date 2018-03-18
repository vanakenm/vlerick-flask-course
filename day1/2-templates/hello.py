from flask import Flask
from flask import render_template
app = Flask(__name__)


@app.route("/hello/<name>")
def hello(name):
    return """
    <html>
        <head><title>Hello Flask</title></head>
        <body>
          <h1>Hello %s!</h1>
        </body>
    </html>""" % name


@app.route("/betterhello/<name>")
def better_hello(name):
    return render_template('hello.html', name=name)
