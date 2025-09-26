from flask import Flask

app = Flask(__name__)

@app.route("/")
def say_hello():
	return '<p> Hello, world I am flask app!<p>'

@app.route("/about")
	return '<p> This app is running on <a href="https://flask.com">Flask<a> <p>'

