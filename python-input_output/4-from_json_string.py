#!/usr/bin/python3
""" doc """
import json


def from_json_string(my_str):
    """ transfo a json string into a json object """
    return json.loads(my_str)
