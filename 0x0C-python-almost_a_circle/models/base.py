#!/usr/bin/python3

""" Defines a base model class """


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
