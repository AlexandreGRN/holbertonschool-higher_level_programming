#!/usr/bin/python3
""" Empty class """


class Base:
    """ Base class """
    def __init__(self, id=None):
        __nb_objects = 0
        if id is not None:
            if isinstance(id, int):
                self.id = id
        else:
            self.__nb_objects += 1
            self.id = __nb_objects
