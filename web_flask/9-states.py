#!/usr/bin/python3
"""
Starts a Flask web app
"""

from models.state import State
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.route('/states', strict_slashes=False)
def states():
    """ fetching data """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ displays states """
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', states=state, id=state.id)
    return render_tempalte('9-states.html', states=state)


@app.teardown_appcontext
def teardown(self):
    """ removes current sqlalchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
