from flask import Flask
import redis
import time

r = redis.Redis(host='redis-server', port=6379)
app = Flask(__name__)

@app.route("/")
def say_hello():
    return '<p> Welcome, I am flask app! <a href="./contact">Contact<a><p>'


@app.route('/about')
def about():
    data = r.get('about')
    if data is not None:
        if time.time() - data['time'] > 600:
            return data['html']

    data = '<p>This application is running on the Flask web framework.</p><p>Learn more about Flask at <a href="https://flask.palletsprojects.com/">https://flask.palletsprojects.com/</a></p><p>Learn more about Python at <a href="https://www.python.org/">https://www.python.org/</a></p><p><a href="/">Back to home</a></p>'
    r.set('about', {
        'html': data,
        'time': time.time()
    })
    return data

@app.route("/contact")
def contact():
    return '<p> My email is c23330061@gmail.com <p>'


