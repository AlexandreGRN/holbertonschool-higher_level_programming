#!/usr/bin/python3
""" test if same class or class itself """


def is_kind_of_class(obj, a_class):
    """ is instance == said class + all inheritence of that class """
    return isinstance(obj, a_class)
