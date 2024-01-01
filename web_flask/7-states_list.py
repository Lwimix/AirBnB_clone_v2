#!/usr/bin/python3
"""
This module starts the Flask web application
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def list_states():
    """Prints state objects"""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('7-states_list.html', my_states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
