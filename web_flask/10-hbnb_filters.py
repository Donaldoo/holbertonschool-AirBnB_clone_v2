#!/usr/bin/python3
""" starts flask web app """

from flask import Flask, render_template
from models.state import State
from models.city import City
from models.amenity import Amenity
from models import storage

app = Flask(__name__)


app.route('/hbnb_filters', strict_slashes=False)
def filters():
    states = storage.all(State).values()
    cities = storage.all(City).values()
    amenities = storage.all(Amenity).values()
    return render_template('10-hbnb_filters.html',
                           states=states, cities=cities, amenities=amenities)


@app.teardown_appcontext
def teardown(self):
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
