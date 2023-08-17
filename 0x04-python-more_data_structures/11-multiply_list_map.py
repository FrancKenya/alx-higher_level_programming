#!/usr/bin/python3

""" Returns a list with values * number """


def multiply_list_map(my_list=[], number=0):
    i = (map((lambda x: x * number), my_list))
    return (list(i))
