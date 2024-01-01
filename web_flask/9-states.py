#!/usr/bin/python3
"""
This module starts the Flask web application
"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def states():
    """Prints state and city objects"""
    states = storage.all(State)
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('9-states.html', my_states=sorted_states)


@app.route("/states/<id>", strict_slashes=False)
def state_id(id):
    """Prints state with id=id"""
    states = storage.get(State, id)
    if state:
        cities = s
    sorted_states = sorted(states.values(), key=lambda state: state.name)
    return render_template('9-states.html', my_states=sorted_states)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
