#!/usr/bin/python3

""" defines a class """


class Student:
    """ Represent the student """
    def __init__(self, first_name, last_name, age):
        """ Initializes student
        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Dictionary representation
        If attrs is a list of strings, only attributes name contain
        in this list must be retrieved.
        Otherwise, all attributes must be retrieved
        Args:
            attrs: Attributes represented
        """
        if attrs is None:
            return self.__dict__
        else:
            return {key: value for key, value in self.__dict__.items()
                    if key in attrs}

    def reload_from_json(self, json):
        """
        Replaces attributes
        Args:
            json: used to replace attributes
        """
        for key, value in json.items():
            setattr(self, key, value)
