#!/usr/bin/python3
""" Starts a Flash Web Application """
from models import storage
from models.score import Score
from models.arts import Arts
from models.artist import Artist
from flask import Flask, render_template
from uuid import uuid4
app = Flask(__name__)
# app.jinja_env.trim_blocks = True
# app.jinja_env.lstrip_blocks = True


@app.teardown_appcontext
def close_db(error):
    """ Remove the current SQLAlchemy Session """
    storage.close()


@app.route('/3-arsual/', strict_slashes=False)
def arsual():
    """ ARSUAL is alive! """
    scores = storage.all(Score).values()
    scores = sorted(scores, key=lambda k: k.name)

    artts = storage.all(Arts).values()
    artts = sorted(artts, key=lambda k: k.name)

    artists = storage.all(Artist).values()
    artists = sorted(artists, key=lambda k: k.name)

    values = {"scores": scores, "artts": artts,
              "artists": artists, "cache_id": uuid4()}

    return render_template('3-arsual.html',
                           artts=artts,
                           artists=artists)


if __name__ == "__main__":
    """ Main Function """
    app.run(host='0.0.0.0', port=3000, debug=True)
