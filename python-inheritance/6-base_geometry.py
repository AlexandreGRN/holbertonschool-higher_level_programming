#!/usr/bin/python3
""" raise an exception """


class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
