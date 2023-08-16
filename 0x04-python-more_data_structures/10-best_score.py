#!/usr/bin/python3

""" Returns a key with the biggest integer value """


def best_score(a_dictionary):
    if not a_dictionary:
        return (None)
    i = (max(a_dictionary, key=a_dictionary.get))
    return (i)
