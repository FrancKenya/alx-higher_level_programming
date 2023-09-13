#!/usr/bin/python3

""" Defines BaseGeometry class """


class BaseGeometry:
    """ class representing the BaseGeometry """

    def area(self):
        """ Raises the exception """

        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value
        Args:
            name: The name of the argument
            value: the value being validated
        Raises:
            TypeError: if not an integer
            ValueError: if number is negative or 0
        """

        if not isinstance(value, int):
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
