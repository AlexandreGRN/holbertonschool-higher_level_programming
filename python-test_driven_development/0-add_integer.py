#!/usr/bin/python3
""" Hello """


def add_integer(a, b=98):
    """ Function that add 2 ints"""
    try:
        num1 = int(a)
    except:
        raise TypeError("a must be an integer")
    try:
        num2 = int(b)
    except:
        raise TypeError("b must be an integer")
    return (int(a)+int(b))
