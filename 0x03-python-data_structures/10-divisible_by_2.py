#!/usr/bin/python3


""" finds all multiples of 2 in a list. """


def divisible_by_2(my_list=[]):
    rslt = []
    for number in my_list:

        rslt.append(number % 2 == 0)

    return (rslt)
