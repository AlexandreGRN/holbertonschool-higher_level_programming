#!/usr/bin/python3
""" Hello """


def add_integer(a, b=98):
    """ Function that add 2 ints"""
    try:
        a = int(a)
    except:
        raise TypeError("a must be an integer")
    try:
        b = int(b)
    except:
        raise TypeError("b must be an integer")
    return (a+b)
