#!/usr/bin/python3

""" Defines a class Rec that inherits from BaseGeometry """


# import the task 9_rectangle
Rectangle = __import__('9-rectangle').Rectangle


class Rectangle(BaseGeometry):
    """ Representation of the rectangle """
    def __init__(self, size):
        """
        Initializes the rectangle
        Args:
            size: size of the square
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
