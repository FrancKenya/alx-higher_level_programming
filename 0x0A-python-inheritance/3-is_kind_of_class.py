#!/usr/bin/python3

""" checks if f the object is an instance or instance of class inherited """


def is_kind_of_class(obj, a_class):
    """
    checks for an instance or instance of class inherited
    Args:
        obj: Object checked
        a_class: One compared with
    Returns: True or False
    """
    return isinstance(obj, a_class)
