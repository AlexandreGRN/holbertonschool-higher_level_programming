#!/usr/bin/python3
def is_same_class(obj, a_class):
    """ exactly means not a inheritence of a_class """
    return type(obj) == a_class
