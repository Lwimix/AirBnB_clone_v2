#!/usr/bin/python3
"""
This module starts the Flask web application
"""
from flask import Flask, render_template


app = Flask(__name__)
@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB"
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"
@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    return "C " + str(text).replace("_", " ")
@app.route("/python", strict_slashes=False, defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    return "Python " + str(text).replace("_", " ")
@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    return str(n) + " is a number"
@app.route("/number_template/<int:n>", strict_slashes=False)
def num_template(n):
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
