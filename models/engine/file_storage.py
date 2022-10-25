#!/usr/bin/python3
"""
This is the File Storage module.
Contains the FileStorage class.
"""
import json
from os import path

from models.base_model import BaseModel
from models.user import User
from models.artist import Artist
from models.arts import Arts
from models.score import Score


class FileStorage():
    """
    This class serializes and deserializes instances to JSON and vice-versa.
    Attributes:
        __file_path (str): path to the JSON file.
        __objects (dict): will store all objects by <class name>.id.
    """

    __file_path = "file.json"
    __objects = {}

    all_classes = {'BaseModel': BaseModel, 'User': User,
                   'Score': Score, 'Arts': Arts,
                   'Artist': Artist}

    def all(self, cls=None):
        """
        returns a dictionary
        Return:
            returns a dictionary of __object
        """
        all_return = {}

        # if cls is valid
        if cls:
            if cls.__name__ in self.all_classes:
                # copy objects of cls to temp dict
                for key, value in self.__objects.items():
                    if key.split('.')[0] == cls.__name__:
                        all_return.update({key: value})
        else:  # if cls is none
            all_return = self.__objects

        return all_return

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id.
        Args:
            obj: the object to set in.
        """
        FileStorage.__objects["{}.{}".format(type(obj).__name__, obj.id)] = obj

    def save(self):
        """serialize the file path to JSON file path
        """
        my_dict = {}
        for key, value in self.__objects.items():
            my_dict[key] = value.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(my_dict, f)

    def delete(self, obj=None):
        """Delete the object obj if obj is in __objects"""
        if obj is not None:
            for key, value in FileStorage.__objects.items():
                if value is obj:
                    tmp = key
            FileStorage.__objects.pop(tmp)

    def reload(self):
        """serialize the file path to JSON file path"""
        try:
            with open(self.__file_path, 'r', encoding="UTF-8") as f:
                for key, value in (json.load(f)).items():
                    value = eval(value["__class__"])(**value)
                    self.__objects[key] = value
        except FileNotFoundError:
            pass

    def close(self):
        """Reload JSON objects"""
        return self.reload()

    def get(self, cls, id):
        """retrieves an object in the storage"""
        if cls and id:
            obj = self.all(cls).get("{}.{}".format(cls.__name__, id), None)
            return obj
        return None

    def count(self, cls=None):
        """count the number of objects in the storage"""
        return len(self.all(cls))
