#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    """Render the list of the states"""
    states = storage.all('State').values()
    cities = storage.all('City').values()
    amenities = storage.all('Amenity').values()
    return render_template("10-hbnb_filters.html", states=states, cities=cities, amenities=amenities)


@app.teardown_appcontext
def teardown_db(db):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
