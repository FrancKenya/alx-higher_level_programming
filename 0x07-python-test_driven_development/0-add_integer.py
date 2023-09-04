#!/usr/bin/python3

""" A function that adds two integer """


def add_integer(a, b=98):
    """
    adds integer a nad b
    Args:
        a: first number
        b: second number
    Returns:
        an int (sum of a and b)
    Raises:
        TypeError: When either a or b aint a number
    """
    if not isinstance(a, int) and not isinstance(a, float):
        raise TypeError("a must be an integer")
    if not isinstance(b, int) and not isinstance(b, float):
        raise TypeError("b must be an integer")

    a = int(a)
    b = int(b)

    return (a + b)
