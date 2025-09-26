from flask import Flask

app = Flask(__name__)

@app.route("/")
def say_hello():
    return '<p> Welcome≈, world I am flask app! <a href="./contact">Contact<a><p>'

@app.route("/about")
def about():
    return '<p> This app is running on <a href="https://flask.com">Flask<a> <p>'

@app.route("/contact")
def contact():
    return '<p> My email is afolabiadekanle@gmail.com <p>'


