#!/usr/bin/python3
def uppercase(str):
    for c in range (len(str)):
        u = ord(str[c])
        if u >= 97 and u <= 122:
            u = u - 32
        print("{}".format(chr(u)), end = '')
