#!/usr/bin/python3

""" removes characters from a string """


def no_c(my_string):
    new = []
    for char in my_string:
        if char != 'C' and char != 'c':
            new.append(char)
    return ("".join(new))
