#!/usr/bin/python3

for values in range(ord('Z'), ord('a'), -1):
    print("{}".format(chr(values)), end="")
    if values % 2 == 0:
        values += 32
    else:
        values -= 32
