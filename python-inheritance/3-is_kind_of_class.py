#!/usr/bin/python3
def is_kind_of_class(obj, a_class):
    """ is instance == said class + all inheritence of that class """
    return isinstance(obj, a_class)
