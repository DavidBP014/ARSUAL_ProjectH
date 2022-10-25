#!/usr/bin/python3
""" Arsual Module for Arsual project """
from os import getenv
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String


class Arts(BaseModel, Base):
    """ The arts class """

    __tablename__ = "artts"

    if getenv('ARSUAL_TYPE_STORAGE') == "db":
        name = Column(String(128), nullable=False)

    else:
        name = ""
