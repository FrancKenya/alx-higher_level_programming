#!/usr/bin/python3

""" defines a class """


class MyList:
    """ inherits from list """

    def print_sorted(self):
        """ prints the list, but sorted (ascending sort) """
        sorted_final_list = sorted(self)
        print(sorted_final_list)
