#!/usr/bin/python3
""" doc """
import json


def to_json_string(my_obj):
    """ transform an object(type: dictionnary) into a json rprent of obj """
    return json.dumps(my_obj)
