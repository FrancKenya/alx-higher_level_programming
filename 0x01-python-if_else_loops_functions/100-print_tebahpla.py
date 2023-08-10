#!/usr/bin/python3
j = 0
for value in range(ord('Z'), ord('a') - 1, -1):
    print("{}".format(chr(value - j)), end="")
    j = 32 - j
