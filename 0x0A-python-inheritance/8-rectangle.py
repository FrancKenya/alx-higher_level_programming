#!/usr/bin/python3


""" Defines class rectangle """


# Import task 7 BaseGeometry

BaseGeometry = __import__('7-base_geometry') .BaseGeometry


class Rectangle(BaseGeometry):
    """ BaseGeometry rectangle """

    def __init__(self, width, height):
        """
        Initializes the rectangle
        Args:
            width: width of that rectangle
            height: height of the rectangle
        """
        self.integer_validator("height", height)
        self.__height = height
        self.integer_validator("width", width)
        self.__width = width
