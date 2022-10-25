#!/usr/bin/python3
""" Artist Module for Arsual project """
from os import getenv
import models
from models.base_model import BaseModel, Base
from models.arts import Arts
from sqlalchemy import Column, Table, String, Integer, ForeignKey
from sqlalchemy.orm import relationship

if getenv("ARSUAL_TYPE_STORAGE") == "db":
    artist_arts = Table("artist_arts", Base.metadata,
                        Column("artists_id", String(60),
                               ForeignKey("artists.id"),
                               primary_key=True),
                        Column("arts_id", String(60),
                               ForeignKey("artts.id"),
                               primary_key=True))


class Artist(BaseModel, Base):
    """ A Artist to stay """

    __tablename__ = "artists"

    if getenv("ARSUAL_TYPE_STORAGE") == "db":
        user_id = Column(String(60), ForeignKey("users.id"), nullable=False)
        name = Column(String(128), nullable=False)
        description = Column(String(1024))
        price_by_hour = Column(Integer, nullable=False, default=0)

        arts = relationship("Arts", secondary=artist_arts,
                            backref="artist_artts",
                            viewonly=False)

    else:
        user_id = ""
        name = ""
        description = ""
        price_by_hour = 0
        arts_ids = []

        @property
        def artts(self):
            """Artts getter"""
            artts = models.storage.all(Arts)
            lst = []
            for arts in artts.values():
                if arts.id in self.arts_ids:
                    lst.append(arts)
            return lst

        @artts.setter
        def artts(self, obj):
            """Artts setter"""
            if type(obj) == Arts:
                self.arts_ids.append(obj.id)
