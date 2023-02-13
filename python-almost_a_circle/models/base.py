#!/usr/bin/python3
""" Empty class """


class Base:
    """ Base class """
    __nb_objects = 0
    def __init__(self, id=None):
        if id is not None:
            if isinstance(id, int):
                self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
