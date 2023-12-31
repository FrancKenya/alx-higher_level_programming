#!/usr/bin/python3

""" defines a rectangle """


class Rectangle:
    """ a class Rectangle that defines a rectangle """
    def __init__(self, width=0, height=0):
        """
        Intitalizing the rectangle
        Args:
            width and height
        Raises:
            ValueError and TypeError
        """
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

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        return (2 * (self.__width + self.__height))
