 #!/usr/bin/python3
""" Starts a Flask application related to HBNB. """

from os import getenv
from flask import Flask, render_template
from models import storage
from models.score import Score
from models.arts import Arts

app = Flask(__name__)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the database session after each request."""
    storage.close()


@app.route('/arsual_filters', strict_slashes=False)
def arsual_filters():
    """
        Flask route at /arsual_filters.
        Fills the two popovers in arsual homepage.
    """
    scores = storage.all(Score).values()
    artts = storage.all(Arts).values()
    values = {"scores": scores, "artts": artts}
    return render_template('10-arsual_filters.html', **values)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
