#!/usr/bin/python3

""" prints x elements of a list """


def safe_print_list(my_list=[], x=0):
    cnt = 0

    try:
        for itr in range(x):
            print(my_list[itr], end="")
            cnt += 1
    except IndexError:
        pass
    print()
    return (cnt)
