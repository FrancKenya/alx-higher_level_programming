#!/usr/bin/python3

""" defines a square """


class Square:
    """ square representation """
    def __init__(self, size=0):
        """ initialization """
        self.size = size

    @property
    def size(self):
        """ set size """
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
