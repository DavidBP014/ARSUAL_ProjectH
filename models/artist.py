#!/usr/bin/python3
"""This is the Place Model module.
Contains the Place class that inherits from BaseModel.
"""
from models.base_model import BaseModel


class Artist(BaseModel):
    """This class defines an Place.
    Attributes:
        city_id (str): the place's city id.
        user_id (str): the place's user id.
        name (str): the place's name.
        description (str): the place's description.
        number_rooms (int): the place's number of rooms.
        number_bathrooms (int): the place's number of bathrooms.
        max_guest (int): the place's maximum number of guests.
        price_by_night (int): the place's price by night.
        latitude (float): the place's latitude.
        longitude (float): the place's longitude.
        amenity_ids (list): the place's list of amenities ids.
    """


    name = ""
    description = ""
    Type = ""
    Precio = ""
