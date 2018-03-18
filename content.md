class: center, middle

# Web development with Python

---

# Hi!

I'm [Martin](http://joyouscoding.com) - I'm an economist who has been building and helping people build software for the last 15 years.

I'm currently CTO of [Bluesquare](http://bluesquarehub.com) and I'm a frequent teacher at [LeWagon](https://lewagon.com).

---

(I also speak fast and have quite a bad English accent - enjoy!)

---

# Agenda - day 1

1.  Static vs Dynamic pages
2.  Model View Controller
3.  A first Flask application
4.  Templates and layout

---

# Agenda - day 2

1.  Parameters
2.  APIs and JSON
3.  Connecting from Flask
4.  Using libraries

---

# Day 1

---

## Static and Dynamic pages

Difference between:

* [joyouscoding.com](http://joyouscoding.com) - static
* [twitter.com](https://twitter.com) - dynamic

Not everyone sees the same thing

* Time
* Location
* User status

---

## Static and Dynamic pages, cont'

Facebook does not have a singe HTML page on their server for every user - those pages are dynamically generated for you when you visit the site.

The content is typically stored in a database and "injected" in the page.

This is what Flask and Python allows you to do (among many other languages).

---

## Model - View - Controller (MVC)

Flask is a "MVC" framework.

* Model: your data (often a SQL database)
* Controller: your business logic (python code)
* View: the HTML page (HTML/CSS)

We're not touching DB in this course - you've enough to do already, so we'll fake it with some hard coded data if needed.

---

## Let's create our first Flask site!

Run `pip install flask` to install Flask.
Create a new folder, and a file named "hello.py" with:

```python
from flask import Flask
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"
```

then just run `FLASK_APP=hello.py flask run` and go to localhost:8000 in your browser

---

## What happened?

* Flask is running a web server on your machine, which answer (by default) to the port 8000
* localhost means your own machine (equivalent: 127.0.0.1)
* The code tells flask to answer "Hello world" if a request arrives on the root page (/)
* Text is a perfectly valid HTML content, so the browser will interpret it properly

---

## Let's look at the code again

```python
# import the Flask library under the name "flask"
from flask import Flask

# create a new application using this file name (hello.py)
app = Flask(__name__)

# call this method if someone goes to the "/" path
@app.route("/")
def hello():
    # returns "Hello World!" as content
    return "Hello World!"
```

---

## This is just Python as you know it

After Flask `@app.route("/")` decorator, the `hello()` function is "just" a Python function.

Anything you've see last week would work there (as long as in the end you can output something as a string).

---

## More routes

We can add more routes and pages to the application:

```python
@app.route("/profile")
def profile():
    return "I'm Martin"
```

---

## Variable routes

Routes can use variable too:

```python
@app.route("/profile/<name>")
def profile(name):
    return "I'm %s" % name
```

In this case the profile function receive the `<name>` part of the url as an argument.

---

## Debug mode

Restarting the server each time is not fun - we can use Flask's debug mode to get "auto reload":

`FLASK_DEBUG=1 FLASK_APP=hello.py flask run`

---

## Templates (why)

We could continue that same way and emit proper HTML:

```python
@app.route("/hello/<name>")
def hello(name):
    return """
    <html>
        <head><title>Hello Flask</title></head>
        <body>
          <h1>Hello %s!</h1>
        </body>
    </html>""" % name
```

but this is not really practical.

---

## Templates

```python
# hello.py
@app.route("/betterhello/<name>")
def better_hello(name):
    # Instead of returning a string, we open a template
    # and pass the params
    return render_template('hello.html', name=name)
```

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello Flask</title>
</head>
<body>
    <h1>Hello {{ name }}!</h1>
</body>
</html>
```

---

## MVC

* `hello.py` is the "controller" with the logic
* `hello.html` is the "view" with how it shows on the screen

This is also called "separation of concerns" (logic vs presentation)

---

## Layouts

When you have several pages, some parts are common like a navbar - we don't want to copy paste it everywhere (why?)

---

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello Flask</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Navbar</a>
        ...
  </nav>
  <div class="container">
    <h1>Index</h1>
  </div>
</body>
</html>
```

---

## Layout

We can export all the common part to a common file:

```html
<!DOCTYPE html>
<html>
<head>
    <title>Hello Flask</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
</head>
<body>
  <nav class="navbar navbar-expand-lg navbar-light bg-light">
    <a class="navbar-brand" href="#">Navbar</a>
        ...
  </nav>
  <div class="container">
    {&#37; block body &#37;} {&#37; endblock &#37;}
  </div>
</body>
</html>
```

---

then use it inside each page:

```html
  {# index.html #}
  {&#37; extends "layout.html" &#37;}
  {&#37; block body &#37;}
    <h1>Index!</h1>
  {&#37; endblock &#37;}
```

```html
  {# home.html #}
  <pre>{&#37; extends "layout.html" &#37;}</pre>
  {&#37; block body &#37;}
    <h1>Home!</h1>
  {&#37; endblock &#37;}
```

---

## Going online

This is just to give you an insight - by running a web server on our own machine, we're just minutes away to deploy it on the internet.

Let's try it out!

???

* Install gunicorn

pip install gunicorn

* Add a Procfile

web: gunicorn hello:app

* Add minimal requirements.txt file

Flask==0.12.2
Flask-Cors==3.0.3
gunicorn==19.7.1
Jinja2==2.9.6

* Git commit and launch

---

## Day 1 References

* [Flask site](http://flask.pocoo.org/)
* [Flask mega tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world)
* [Jinja templates](http://jinja.pocoo.org)
* [Deploying a Flask app on Heroku](https://devcenter.heroku.com/articles/getting-started-with-python#introduction)
* [Python style guide](https://www.python.org/dev/peps/pep-0008/)

---

# Your turn!

* Simplest page (static) - create a profile page
* Example with layout - extend the profile page
* Example with logic (ex: small calculator)
* Bonus: Dad jokes (using an external library to get the data)

---

# Day 2

---
