#!/usr/bin/python3


""" checks if bject is an instance of a class is inherited """


def inherits_from(obj, a_class):
    """
    Checks for instance of a class inherited from specified classrgs:
    Args:
        Obj: one being compared
        a_class: One compared with
    Returns: True or false
    """
    return (issubclass(type(obj), a_class))
