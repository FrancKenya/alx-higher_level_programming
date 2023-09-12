#!/usr/bin/python3

""" defines a function that appends a string """


def append_write(filename="", text=""):
    """
    Function that appends a string at a txt file
    Args:
        filename: name of the file it's written
        text: text being written
    Returns: number of characters added
    """
    with open(filename, "a", encoding="utf-8") as file:
        filename_append = file.write(text)
        return (filename_append)
