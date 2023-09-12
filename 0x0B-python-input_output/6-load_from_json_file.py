#!/usr/bin/python3

""" defines a function that creates an object """


import json


def load_from_json_file(filename):
    """
    creates the object from a JSON file
    Args:
        filename: JSON file
    """
    with open(filename, "r") as file:
        content = json.load(file)
        return (content)
