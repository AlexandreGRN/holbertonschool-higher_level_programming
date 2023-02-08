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
        if attrs is not None:
            result = {}
            keys = set(attrs).intersection(set(self.__dict__.keys()))
            for k in keys:
                result[k] = self.__dict__[k]
            return result
        else:
            return self.__dict__

    def reload_from_json(self, json):
        for keys in json:
            if keys in self.__dict__:
                self.__dict__[keys] = json[keys]
