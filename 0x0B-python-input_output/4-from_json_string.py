#!/usr/bin/python3

""" defines a function that returns an object """

import json


def from_json_string(my_str):
    """
    function returning python data structure
    Args:
        my_str: string to be converted
    Returns: Converted string
    """
    string_converted = json.loads(my_str)
    return (string_converted)
