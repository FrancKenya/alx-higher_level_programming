#!/usr/bin/python3

""" Returns a tuple with the length of a string and its first character """


def multiple_returns(sentence):
    if sentence == "":
        return (0, None)
    else:
        return (len(sentence), sentence[0])
