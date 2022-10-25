#!/usr/bin/python3
""" Test .get() and .count() methods
"""
from models import storage
from models.arts import Arts

print("All objects: {}".format(storage.count()))
print("Arts objects: {}".format(storage.count(Arts)))

first_arts_id = list(storage.all(Arts).values())[0].id
print("First arts: {}".format(storage.get(Arts, first_arts_id)))
