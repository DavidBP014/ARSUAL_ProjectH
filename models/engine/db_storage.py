#!/usr/bin/python3
"""This module defines a class to manage db storage"""
from os import getenv, remove
from sqlalchemy.engine.url import URL
from sqlalchemy.orm.session import Session
from sqlalchemy.orm import sessionmaker, scoped_session
from sqlalchemy import create_engine
import MySQLdb

from models.base_model import BaseModel, Base
from models.user import User
from models.artist import Artist
from models.arts import Arts
from models.score import Score


class DBStorage():
    """This class manages storage in a database."""

    __engine = None
    __session = None

    classes = [Arts, Artist, Score, User]

    def __init__(self):
        """Instantiates the DBStorage class"""

        mySQL_u = getenv("ARSUAL_MYSQL_USER")
        mySQL_p = getenv("ARSUAL_MYSQL_PWD")
        db_host = getenv("ARSUAL_MYSQL_HOST")
        db_name = getenv("ARSUAL_MYSQL_DB")

        url = {'drivername': 'mysql+mysqldb', 'host': db_host,
               'username': mySQL_u, 'password': mySQL_p, 'database': db_name}

        self.__engine = create_engine(URL(**url), pool_pre_ping=True)

        if getenv('ARSUAL_ENV') == "test":
            Base.metadata.drop_all(self.__engine)

    def all(self, cls=None):
        """Returns a dictionary of models currently in database"""
        objs = []
        dct = {}
        if cls is None:
            for item in self.classes:
                objs.extend(self.__session.query(item).all())
        else:
            if type(cls) is str:
                cls = eval(cls)
            objs = self.__session.query(cls).all()

        for obj in objs:
            dct[obj.__class__.__name__ + '.' + obj.id] = obj
        return dct

    def new(self, obj):
        """Adds the object to the database"""
        self.__session.add(obj)

    def save(self):
        """Commits all changes to the database"""
        self.__session.commit()

    def delete(self, obj=None):
        """Deletes obj from the database"""
        if obj is not None:
            self.__session.delete(obj)

    def reload(self):
        """Creates all tables of the database"""
        Base.metadata.create_all(self.__engine)

        s_factory = sessionmaker(bind=self.__engine, expire_on_commit=False)
        Session = scoped_session(s_factory)
        self.__session = Session()

    def close(self):
        """Handles close of DBStorage"""
        self.__session.close()

    def get(self, cls, id):
        """retrieves an object in the database"""
        if cls and id:
            return self.__session.query(cls).filter_by(id=id).first()
        return None

    def count(self, cls=None):
        """count the number of objects in the database"""
        return len(self.all(cls))
