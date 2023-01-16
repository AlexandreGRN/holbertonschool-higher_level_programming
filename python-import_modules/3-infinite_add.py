#!/usr/bin/python3
import sys

res = 0
for count, arg in enumerate(sys.argv):
    if count != 0:
        res = res + int(arg)

print(res)