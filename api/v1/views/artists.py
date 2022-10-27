#!/usr/bin/python3
"""This is the artists page handler for Flask."""
from api.v1.views import app_views
from models import storage
from flask import abort, jsonify, request

from models.artist import Artist
from models.user import User
from models.score import Score
from models.arts import Arts


@app_views.route('/artists/<id>', methods=['GET', 'DELETE', 'PUT'])
def artists_id(id):
    """Flask route at /artists/<id>."""
    artist = storage.get(Artist, id)
    if (artist):
        if request.method == 'DELETE':
            artist.delete()
            storage.save()
            return {}, 200

        elif request.method == 'PUT':
            kwargs = request.get_json()
            if not kwargs:
                return {"error": "Not a JSON"}, 400
            for key, value in kwargs.items():
                if key not in ["id", "user_id",
                               "created_at", "updated_at"]:
                    setattr(artist, key, value)
            artist.save()
        return place.to_dict()
    abort(404)


@app_views.route('/artists_search', methods=['POST'])
def artists_search():
    """Flask route at /artists_search"""
    kwargs = request.get_json()
    if not kwargs:
        return {"error": "Not a JSON"}, 400
    scores = kwargs.get('scores', [])
    artts = kwargs.get('artts', [])
    if scores == artts == []:
        artists = storage.all("Artist").values()
    else:
        artists = []
        for score_id in scores:
            score = storage.get(Score, score_id)
    search_result = []
    arts_objs = []
    for arts_id in artts:
        arts = storage.get(Arts, arts_id)
        if arts:
            arts_objs.append(arts)
    for artist in artists:
        artts_cnt = 0
        for arts in arts_objs:
            if arts not in artist.artts:
                artts_cnt += 1
        if artts_cnt == 0:
            search_result.append(artist.to_dict())

    return jsonify(search_result)
