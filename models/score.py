#!/usr/bin/python3
"""This is the State Model module.
Contains the State class that inherits from BaseModel.
"""
from os import getenv
import models
from models.base_model import BaseModel, Base
from sqlalchemy.orm import relationship
from sqlalchemy import Column, String


class Score(BaseModel, Base):
    """
    This class defines a State.
    Attributes:
        score (str): the score's number.
    """
    __tablename__ = "scores"

    if getenv('ARSUAL_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)
    else:
        name = ""
