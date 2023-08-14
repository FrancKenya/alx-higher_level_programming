#!/usr/bin/python3

""" prints reversed integers in a list """


def print_reversed_list_integer(my_list=[]):
    for i in my_list[::-1]:
        print("{}".format(i))
