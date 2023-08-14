#!/usr/bin/python3

""" removes characters from a string """


def no_c(my_string):
    new = " "
    for c in my_string:
        if c != 'C' and c != 'c':
            new += c

    return (new)
