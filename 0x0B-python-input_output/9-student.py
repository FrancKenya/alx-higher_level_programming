#!/usr/bin/python3

""" writes a class Student that defines a student """


class Student:
    """ class representing student """
    def __init__(self, first_name, last_name, age):
        """ Initializes the student
        Args:
            first_name: first name of the student
            last_name: Last name of the student
            age: age of the student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ dictionary representation """
        results = self.__dict__
        return (results)
