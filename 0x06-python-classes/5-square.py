#!/usr/bin/python3

""" defining a square """


class Square:
    """ square representation """
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """ setting size """
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """ returning current area """
        return (self.__size ** 2)

    def my_print(self):
        """ printing square """
        if self.__size == 0:
            print()
            return
        for _ in range(self.__size):
            print("#" * self.__size)
