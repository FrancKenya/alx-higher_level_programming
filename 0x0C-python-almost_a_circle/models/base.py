#!/usr/bin/python3

""" Defines a base model class """


import json


class Base:
    """  The Base Model Class for all the other classes in this project """

    __nb_objects = 0

    def __init__(self, id=None):
        """
        Initializes a base instance
        Args:
        id: The id forthe instance
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ Returns the JSON string representation of a list of dicts."""
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        list_dict = json.dumps(list_dictionaries)
        return (list_dict)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        Write the JSON string representation of list of objects
        Args:
            list_objs: list of Base instances
        """
        filename = cls.__name__ + ".json"
        if list_objs is None:
            list_objs = []
        with open(filename, "w") as jsonfile:
            jsonfile.write(cls.to_json_string([
                obj.to_dictionary() for obj in list_objs]))
