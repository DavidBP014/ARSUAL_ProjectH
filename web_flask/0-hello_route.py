#!/usr/bin/python3
""" This is the 1st Flask setup script. """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        Flask route at root (http://localhost:5000/).
        Displays 'Hello Arsual!'.
    """
    return "Hello Arsual!"


if __name__ == '__main__':
    from waitress import serve
    serve(app, host="0.0.0.0", port=5000)
