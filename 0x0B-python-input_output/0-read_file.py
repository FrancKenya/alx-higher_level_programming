#!/usr/bin/python3

""" defines a function reads a .txt and prints it out """


def read_file(filename=""):
    """
    function that reads and prints at std out
    Args:
        filename: File being read
    """
    try:
        with open(filename, encoding="utf-8") as file:
            for content in file:
                print(content, end="")
    except FileNotFoundError:
        pass
