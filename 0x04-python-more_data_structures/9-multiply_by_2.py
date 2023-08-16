#!/usr/bin/python3

""" Returns a new dictionary with all values * 2 """


def multiply_by_2(a_dictionary):
    copied_dict = a_dictionary.copy()
    list_1 = list(copied_dict.keys())
    for j in list_1:
        copied_dict[j] *= 2
    return (copied_dict)
