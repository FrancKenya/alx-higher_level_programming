#!/usr/bin/python3

""" defines a rectangle based on the previous task """


class Rectangle:
    """ a class that defines the rectangle """
    def __init__(self, width=0, height=0):
        """
        Initializing the rectangle
        Args:
            Width and height
        Raises:
            TypeError and ValueError
        """
        self.height = height
        self.width = width

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
        if self.__width == 0 or self.__height == 0:
            return (0)
        return (2 * (self.__width + self.__height))

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        return ("\n".join(["#" * self.__width] * self.__height))

    def __repr__(self):
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        print("Bye rectangle...")
