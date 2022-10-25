#!/usr/bin/python3
""" This is the 3rd Flask setup script. """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        Flask route at root.
        Displays 'Hello Arsual!'.
    """
    return "Hello Arsual!"


@app.route('/artists', strict_slashes=False)
def artists():
    """
        Flask route at /hbnb.
        Displays 'Artists'.
    """
    return "Artists"


@app.route('/don_Orlando/<text>', strict_slashes=False)
def don_Orlando(text):
    """
        Flask route at /Don Orlando/<text>.
        Displays 'espicificacion + <text>'.
    """
    return "don Orlando {}".format(text.replace('_', ' '))


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
