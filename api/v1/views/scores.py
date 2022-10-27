from models.score import Score
from models import storage
from api.v1.views import app_views
from flask import request, jsonify, abort


@app_views.route('/scores', methods=['GET', 'POST'], strict_slashes=False)
def scores():
    """Flask rout at /scores"""
    if request.method == 'POST':
        kwargs = request.get_json()
        if not kwargs:
            return {"error": "Not a JSON"}, 400
        if "name" not in kwargs:
            return {"error": "Missing name"}, 400
        new_score = Score(**kwargs)
        new_score.save()
        return new_score.to_dict(), 201

    elif request.method == 'GET':
        return jsonify([o.to_dict() for o in storage.all("Score").values()])


@app_views.route('/scores/<id>', methods=['GET', 'DELETE', 'PUT'],
                 strict_slashes=False)
def scores_id(id):
    """Flask route at /scores/<id>"""
    score = storage.get(Score, id)
    if (score):
        if request.method == 'DELETE':
            storage.delete(score)
            storage.save()
            return {}, 200

        elif request.method == 'PUT':
            kwargs = request.get_json()
            if not kwargs:
                return {"error": "Not a JSON"}, 400
            for key, value in kwargs.items():
                if key not in ["id", "created_at", "updates_at"]:
                    setattr(score, key, value)
            score.save()
        return score.to_dict()
    abort(404)
