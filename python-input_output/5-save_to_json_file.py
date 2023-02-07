#!/usr/bin/python3
""" doc """
import json


def save_to_json_file(my_obj, filename):
    """ write the json representation of my_obj """
    with open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
        f.close
