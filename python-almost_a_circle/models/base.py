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

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns the JSON string representing of dict"""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """ save to json file """
        with open(str(cls.__name__) + ".json", "w", encoding="utf-8") as f:
            list = []
            for i in list_objs:
                list.append(Base.to_json_string(i.to_dictionary()))
            f.write(str(list).replace("\'", ""))
