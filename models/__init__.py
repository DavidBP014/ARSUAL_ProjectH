#!/usr/bin/python3

"""Module to create a unique FileStorage instance for the aplication"""
from os import getenv
from models.base_model import BaseModel
from models.user import User
from models.score import Score
from models.arts import Arts
from models.artist import Artist

if getenv('ARSUAL_TYPE_STORAGE') == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
    storage.reload()

else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()
    storage.reload()
