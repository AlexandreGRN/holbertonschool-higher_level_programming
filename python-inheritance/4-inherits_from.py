#!/usr/bin/python3
""" test for inherited class only """


def inherits_from(obj,a_class):
    """ from == obj cannot be a_class and need to be inherited from a_class """
    if isinstance(obj, a_class) and not type(obj) == a_class:
        return True
    return False
