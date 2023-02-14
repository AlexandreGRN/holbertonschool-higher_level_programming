#!/usr/bin/python3
""" Empty class """
import json


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

    def to_json_string(list_dictionaries):
        """ returns the JSON string representing of dict"""
        # if len(list_dictionaries) == 0:
        return json.dumps(list_dictionaries)