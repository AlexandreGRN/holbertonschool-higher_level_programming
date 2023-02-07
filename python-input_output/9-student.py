#!/usr/bin/python3
""" doc """
class Student:
    """ Student class """

    def __init__(self, first_name, last_name, age):
        """ Initialisation """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ retrieve a dictionary representation of a student var """
        return self.__dict__
