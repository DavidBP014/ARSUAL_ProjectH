#!/usr/bin/python3
"""This is the Blueprint handles for Flask."""
from flask import Blueprint

app_views = Blueprint('app_views', __name__, url_prefix='/api/v1')

from api.v1.views.index import *
from api.v1.views.scores import *
from api.v1.views.artts import *
from api.v1.views.users import *
from api.v1.views.artists import *
from api.v1.views.artists_artts import *
