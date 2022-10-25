#!/usr/bin/python3
""" Starts a Flask application related to HBNB. """

from flask import Flask, render_template
from models import storage
from models.score import Score

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session after each request."""
    storage.close()


@app.route('/score_list', strict_slashes=False)
def scores_list():
    """
        Flask route at /score_list.
        Displays the list of the Score in the database.
    """
    scores = storage.all(Score).values()
    return render_template('7-scores_list.html', scores=scores)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
