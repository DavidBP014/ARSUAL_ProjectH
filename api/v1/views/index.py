#!/usr/bin/python3
"""This is the index page handler for Flask"""
from api.v1.views import app_views
from models import storage

classes = {"artts": "Arts",
           "artists": "Artist",
           "scores": "Score",
           "users": "User"}

@app_views.route('/status')
def status():
    """Flask route at /status."""
    return {"status": "OK"}


@app_views.route('stats')
def stats():
    """
       Flask route at /stats.
       Display the number of each objects by type.
    """
    return {key: storage.count(value) for key, value in classes.items()}