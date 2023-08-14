#!/usr/bin/python3

""" replaces elements in a list at a specific position """


def new_in_list(my_list, idx, element):
    if idx < 0 or idx >= len(my_list):
        return (my_list[:])

    copy_list = my_list[:]
    copy_list[idx] = element
    return (copy_list)
