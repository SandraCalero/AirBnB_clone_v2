#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states')
@app.route('/states/<id>')
def states_id(id=None):
    """Render the list of the states"""
    states = storage.all(State).values()
    if id is None:
        return render_template("9-states.html", states=states, id=id)
    else:
        for unique_state in states:
            if unique_state.id == id:
                return render_template("9-states.html",
                                       unique_state=unique_state)
        return render_template("9-states.html")


@app.teardown_appcontext
def teardown_db(db):
    """Remove the current SQLAlchemy Session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
