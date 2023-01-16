#!/usr/bin/python3
import sys

if __name__ == "__main__":
    #print numb of args
    if len(sys.argv) == 1:
        print("0 arguments.")
        sys.exit(0)
    elif len(sys.argv) == 2:
        print("{} argument:".format(len(sys.argv)-1))
    else:
        print("{} arguments:".format(len(sys.argv)-1))
    #enum every args
    for i, arg in enumerate(sys.argv, 0):
        if i != 0:
            print("{}: {}".format(i, arg))