#!/usr/bin/python3

""" Defines a class """


class Student:
    " class representing the student """

    def __init__(self, first_name, last_name, age):
        """
        Initializes the student
        Args:
            first_name: first name of the student
            last_name: last name of the student
            age: Age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Dictionary representation
        If attrs is a list of strings, only attribute names contained in the
        list must be retrieved. Otherwise, all attributes must be retrieved
        Args:
            attrs: attributes to represent
        """
        json_data = {}
        if attrs is None:
            attrs = self.__dict__.keys()
        for attr_name, attr_value in self.__dict__.items():
            if isinstance(attr_value, (str, int)) and attr_name in attrs:
                json_data[attr_name] = attr_value
        return (json_data)
