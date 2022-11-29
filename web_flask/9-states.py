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
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def states_id(id):
    """ displays states """
    for state in storage.all(State).values:
        if state.id == id:
            return render_template('9-states.html', state=state)
    return render_tempalte('9-states.html')


@app.teardown_appcontext
def teardown(self):
    """ removes current sqlalchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
