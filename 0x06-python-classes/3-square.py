#!/usr/bin/python3

""" a class Square """


class Square:
    """ Square representation """
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        return (self.__size ** 2)
