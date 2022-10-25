#!/usr/bin/python3
""" This is the 2nd Flask setup script. """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        Flask route at root (http://localhost:5000/).
        Displays 'Hello Arsual!'.
    """
    return "Hello Arsual!"


@app.route('/artists', strict_slashes=False)
def artists():
    """
        Flask route at /artist (http://localhost:5000/artists).
        Displays 'Artists'.
    """
    return "Artists"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
