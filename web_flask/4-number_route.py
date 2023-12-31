#!/usr/bin/python3
"""
This module starts the Flask web application
"""
from flask import Flask


app = Flask(__name__)
@app.route("/", strict_slashes=False)
def hello():
    """Prints Hello HBNB"""
    return "Hello HBNB"
@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """Prints HBNB"""
    return "HBNB"
@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    """Prints C followed by text input"""
    return "C " + str(text).replace("_", " ")
@app.route("/python", strict_slashes=False, defaults={"text": "is cool"})
@app.route("/python/<text>", strict_slashes=False)
def python_text(text):
    """Prints Python followed by input text"""
    return "Python " + str(text).replace("_", " ")
@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Prints a input number followed by is a number"""
    return str(n) + " is a number"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
