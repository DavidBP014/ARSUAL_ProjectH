#!/usr/bin/python3
""" This is the 4th Flask setup script. """

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
        Flask route at root.
        Displays 'Hello Arsual!'.
    """
    return "Hello Arsual!"


@app.route('/arsual', strict_slashes=False)
def arsual():
    """
        Flask route at /ardual.
        Displays 'Arsual'.
    """
    return "Arsual"


@app.route('/orlando_perez/<text>', strict_slashes=False)
def Orlando_Perez(text):
    """
        Flask route at /Orlandon Perez/<text>.
        Displays 'Orlando Perez + <text>'.
    """
    return "0rlando perez {}".format(text.replace('_', ' '))


@app.route('/juandas', strict_slashes=False)
@app.route('/juandas/<text>', strict_slashes=False)
def juandas(text="is cool"):
    """
        Flask route at /juandas/(<text>).
        Displays 'juandas + <text>'.
        Default value of <text> : 'is cool'.
    """
    return "juandas {}".format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """
        Flask route at /number/<n>.
        Displays '<n> + is an number' if <n> is a int.
    """
    return "{} is a number".format(n)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
