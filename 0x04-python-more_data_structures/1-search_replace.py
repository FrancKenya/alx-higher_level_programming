#!/usr/bin/python3

""" Replaces all element occurences with another element in a new list """


def search_replace(my_list, search, replace):
    new_list = (map(lambda i: replace if i == search else i, my_list))

    return (list(new_list))
