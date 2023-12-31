#!/usr/bin/python3

""" a class Rectangle that defines a rectangle """


class Rectangle:
    """
    a class Rectangle that defines a rectangle
    Args:
        Has private instance attribute: width nad height
    Raises:
        TypeError
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def height(self):
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
