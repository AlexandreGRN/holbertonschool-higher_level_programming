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
            try:
                for i in list_objs:
                    list.append(Base.to_json_string(i.to_dictionary()))
            except:
                pass
            f.write(str(list).replace("\'", ""))

    @staticmethod
    def from_json_string(json_string):
        """ return the list of the json string """
        if json_string is None:
            return list()
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ return an instance with all attribute already """
        if "size" in dictionary:
            dummy = cls(1)
        else:
            dummy = cls(1, 1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ return a list of instance """
        list = []
        try:
            with open(str(cls.__name__) + ".json", "r", encoding="utf-8") as f:
                for i in cls.from_json_string(f.read()):
                    list.append(cls.create(**i))
                return list
        except:
            return list
