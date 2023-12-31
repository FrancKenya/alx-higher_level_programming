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
        with open(filename, "w") as jsonfile:
            if list_objs is None:
                jsonfile.write("[]")
            else:
                jsonfile.write(cls.to_json_string(
                    [obj.to_dictionary() for obj in list_objs]))

    @staticmethod
    def from_json_string(json_string):
        """
        Return list of JSON string representation.
        Args:
            json_string: String representation of a list of dictionaries.
        Returns:
            If json_string is None or empty - an empty list
            Otherwise return list represented by json_string.
        """
        if json_string is None or json_string == "[]":
            return []
        i = (json.loads(json_string))
        return (i)

    @classmethod
    def create(cls, **dictionary):
        """
        Returns a class instantiated from a dictionary of attributes.
        Args:
            **dictionary: Key/value pairs of attributes to be initialize.
            Returns:
                An instance of the class with attributes from the ictionary.
        """
        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return (new)

    @classmethod
    def load_from_file(cls):
        """
        A list of class instances from a JSON file.
        Returns:
            A list of instances if not empty
        """
        filename = str(cls.__name__) + ".json"
        try:
            with open(filename, "r") as jsonfile:
                data = jsonfile.read()
                if not data:
                    return []
                list_dicts = cls.from_json_string(data)
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
