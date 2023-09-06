#!/usr/bin/python3

""" prints a square with the character # """


def print_square(size):
    """
    function that prints #
    Args:
        size: size of the square
    Raises:
        ValueError: when size is negative
        TypeError: if size is not an int
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for num in range(size):
        print("#" * size)
