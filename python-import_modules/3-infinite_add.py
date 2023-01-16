#!/usr/bin/python3
import sys

if __name__ == "__main__":
    res = 0
    for count, arg in enumerate(sys.argv):
        if count != 0:
            res = res + int(arg)
    print(res)