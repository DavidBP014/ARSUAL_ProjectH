#!/usr/bin/python3
"""This is the artists artts page handler for Flask."""
from api.v1.views.artists import artists_id
from api.v1.views import app_views
from api.v1 import *
from models import storage
from flask import abort, jsonify, request

from models.artist import Artist
from models.user import User
from models.arts import Arts


@app_views.route('/artists/<id>/artts', methods=['GET'])
def artists_id_artts(id):
    """Flask route at /artists/<id>/artts."""
    artist = storage.get(Artist, id)
    if (artist):
        if storage_t == 'db':
            return jsonify([r.to_dict() for r in artist.artts])
        elif storage_t == 'fs':
            return jsonify(artist.to_dict()["artts_ids"])
    abort(404)


@app_views.route('/artist/<id>/artts/<ar_id>', methods=['DELETE', 'POST'])
def artists_id_artts_id(id, ar_id):
    """Flask route at /artists/<id>/artts/<ar_id>."""
    artist = storage.get(Artist, id)
    if (artist):
        if request.method == 'DELETE':
            artist = storage.get(Artist, ar_id)
            if (artist):
                if storage_t == 'db':
                    if (artist in artist.artts):
                        artist.artts.remove(arts)
                        storage.save()
                        return jsonify({}, 200)
                    abort(404)
                elif storage_t == 'fs':
                    if (am_id in artist.arts_ids):
                        artist.arts_ids.remove(am_id)
                        storage.save()
                        return jsonify({}, 200)
                    abort(404)
            abort(404)
        elif request.method == 'POST':
            arts = storage.get(Arts, ar_id)
            artist = storage.get(Artist, id)
            if (artist):
                if (arts):
                    if storage_t == 'db':
                        if (arts not in artist.artts):
                            artist.artts.append(arts)
                            storage.save()
                            return jsonify(arts.to_dict(), 201)
                        return jsonify(arts.to_dict(), 200)
                    elif storage_t == 'fs':
                        if (ar_id not in artist.arts_ids):
                            artist.artts_ids.append(ar_id)
                            storage.save()
                            return jsonify(arts.to_dict(), 201)
                        return jsonify(arts.to_dict(), 200)
                    abort(404)
                abort(404)
            abort(404)
    abort(404)
