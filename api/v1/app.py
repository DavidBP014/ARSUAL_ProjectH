#!/usr/bin/python3
"""This is the API server"""
from models import storage
from api.v1.views import app_views
from flask import Flask
from os import getenv

app = Flask(__name__)
app.register_blueprint(app_views)


@app.teardown_appcontext
def teardown_db(exception):
    """closes the storage on teardown"""
    storage.close()


@app.errorhandler(404)
def error_404(exception):
    """Returns the 404 error custom message"""
    return {"error": "Not found"}, 404

if __name__ == "__main__":
    host = getenv("ARSUAL_API_HOST", "0.0.0.0")
    port = getenv("ARSUAL_API_PORT", "5000")
    app.run(host=host, port=port, threaded=True, debug=True)
