#!/usr/bin/python3
"""Review module"""
from models.base_model import BaseModel


class Review(BaseModel):
    """This class defines a Review.
    Attributes:
        artist_id (str): the review's artist id.
        user_id (str): the review's issuer user id.
        text (str): the review.
    """

    artist_id = ""
    user_id = ""
    text = ""
