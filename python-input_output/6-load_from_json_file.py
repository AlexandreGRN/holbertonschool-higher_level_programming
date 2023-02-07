#!/usr/bin/python3
""" doc """
import json


def load_from_json_file(filename):
    """ get the string from a file & loads a json from it """
    with open(filename, "r", encoding="utf-8") as f:
        strFile = f.read()
        return json.loads(strFile)
