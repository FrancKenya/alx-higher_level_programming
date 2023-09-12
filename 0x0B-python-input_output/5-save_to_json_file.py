#!/usr/bin/python3

""" Defines a function that writes an object """


def save_to_json_file(my_obj, filename):
    """
    Fucntion using JSON to write an object
    Args:
        my_obj: written object
        filename: to be written on
    """
    with open(filename, "w") as file:
        content = json.dump(my_obj, file)
        return (content)
