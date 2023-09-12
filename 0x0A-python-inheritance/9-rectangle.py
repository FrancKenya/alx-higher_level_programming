#!/usr/bin/python3

""" Defines a class rectangle """

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ The BaseGeometry rectangle represented """
    def __init__(self, size):
        """ Intiliazes the rectangle
        Args:
            height: height of the new Rectangle
            width: width of the rectangle
        """
        self.__width = width
        self.__height = height
        self.integer_validator("width", width)
        self.integer_validator("height", height)

    def area(self):
        """ calculate the area of the rectangle """
        return (self.__width * self.__height)

    def __str__(self):
        """ str representation of the rectangle """
        return (f"[Rectangle] {self.__width}/{self.__height}")
