#!/usr/bin/python3

""" function that returns True if the oblect is exactly an instance """


def is_same_class(obj, a_class):
    """
    checks if object is an instance
    Args:
        obj: object being changed
        a_class: one being compared
    Returns:
        True if confirmed or False if not
    """
    if type(obj) is a_class:
        return (True)
    return (False)
