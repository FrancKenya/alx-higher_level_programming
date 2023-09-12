#!/usr/bin/python3


""" defines a function that Writes a string to a text file """


def write_file(filename="", text=""):
    """
    writes a string to a text file
    Args:
    filename: the text file
    text: string being written
    """
    with open(filename, "w", encoding="utf-8") as file:
        string_written = file.write(text)
        return (string_written)
