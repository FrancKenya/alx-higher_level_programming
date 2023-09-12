#!/usr/bin/python3

""" Defines a function that returns JSON """


import json


def to_json_string(my_obj):
    """
    Function serializing the string
    Args:
        my_obj: object serilaized
    Returns: JSON representation of an object
    """
    my_obj-data = json.dumps(my_obj)
    return (my_obj-data)
