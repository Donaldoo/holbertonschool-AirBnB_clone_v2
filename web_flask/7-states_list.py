#!/usr/bin/python3
"""
Starts a Flask web app
"""

from models.state import State
from models import storage
from flask import Flask, render_template
app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """ removes current sqlalchemy session """
    storage.close()


@app.route('/states_list', strict_slashes=False)
def states_list():
    """ displays states """
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
