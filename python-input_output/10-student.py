#!/usr/bin/python3
""" doc """


class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """ Initialisation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ retrieve a dictionary representation of a student var """
        if attrs:
            keys = set(attrs).intersection(set(self.__dict__.keys()))
            result = {k:self.__dict__[k] for k in keys}
            return result
        else:
            return self.__dict__
