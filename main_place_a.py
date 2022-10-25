#!/usr/bin/python3
""" Test link Many-To-Many Place <> Amenity
"""
from models import *
from models.user import User
from models.artist import *
from models.arts import Arts


# creation of a User
user = User(email="john@snow.com", password="johnpwd")
user.save()

# creation of 2 Places
artist_1 = Artist(user_id=user.id, name="Jose 1")
artist_1.save()
artist_2 = Artist(user_id=user.id, name="Vicente 2")
artist_2.save()

# creation of 3 various Amenity
arts_1 = Arts(name="Violin")
arts_1.save()
arts_2 = Arts(name="Fotografo")
arts_2.save()
arts_3 = Arts(name="Malabarista")
arts_3.save()

# link place_1 with 2 amenities
artist_1.arts.append(arts_1)
artist_1.arts.append(arts_2)

# link place_2 with 3 amenities
artist_2.arts.append(arts_1)
artist_2.arts.append(arts_2)
artist_2.arts.append(arts_3)

storage.save()

print("OK")
