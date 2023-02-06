#!/usr/bin/python3
""" raise an exception """


class BaseGeometry:
    """ base geometry """

    def area(self):
        """ raise an exception """
        raise Exception("area() is not implemented")
