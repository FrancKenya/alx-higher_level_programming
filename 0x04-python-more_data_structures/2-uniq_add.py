#!/usr/bin/python3

""" Adds all unique integers once in a list """


def uniq_add(my_list=[]):
    new_set = set()
    num = 0

    for i in my_list:
        if i not in new_set:
            new_set.add(i)
            num += i

    return (num)
