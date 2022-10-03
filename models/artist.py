#!/usr/bin/python3
"""Artist module"""
from models.base_model import BaseModel


class Artist(BaseModel):
    """This class defines an Artist.
    Attributes:
        city_id (str): the Artist's city id.
        user_id (str): the Artist's user id.
        name (str): the Artist's name.
        description (str): the Artist's description.
        Activity (str): the Artist's Activity
        price_by_presentation (int): the Artist's price by Presentation.
        amenity_ids (list): the Artist's list of amenities ids.
    """

    city_id = ""
    user_id = ""
    name = ""
    description = ""
    activity = ""
    price_by_Presentation = 0
    amenity_ids = []
