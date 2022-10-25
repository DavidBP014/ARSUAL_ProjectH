#!/usr/bin/python3
"""This is the artts page handler for Flask."""
from api.v1.views import app_views
from models import storage
from flask import abort, jsonify, request

from models.arts import Arts


@app_views.route('/artts', methods=['GET', 'POST'])
def artts():
    """Flask route at /artts."""
    if request.method == 'POST':
        kwargs = request.get_json()
        if not kwargs:
            return {"error": "Not a JSON"}, 400
        if "name" not in kwargs:
            return {"error": "Missing name"}, 400
        new_art = Arts(**kwargs)
        new_art.save()
        return new_art.to_dict(), 201

    elif request.method == 'GET':
        return jsonify([a.to_dict() for a in storage.all("Arts").values()])


@app_views.route('/artts/<id>', methods=['GET', 'DELETE', 'PUT'])
def artts_id(id):
    """Flask route at /artts/<id>."""
    art = storage.get(Art, id)
    if (art):
        if request.method == 'DELETE':
            art.delete()
            storage.save()
            return {}, 200

        elif request.method == 'PUT':
            kwargs = request.get_json()
            if not kwargs:
                return {"error": "Not a JSON"}, 400
            for key, value in kwargs.items():
                if key not in ["id", "created_at", "updated_at"]:
                    setattr(art, key, value)
            art.save()
        return art.to_dict()
    abort(404)
