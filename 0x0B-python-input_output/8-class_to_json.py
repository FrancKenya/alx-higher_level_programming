#!/usr/bin/python3

""" Defines a function that returns the dictionary description """


def class_to_json(obj):
    """
    A function defined that returns the dictionary description
    Args:
        obj: an instance of class
    Returns:
        dictionary description with simple data structure
    """
    results = obj.__dict__
    return (results)
