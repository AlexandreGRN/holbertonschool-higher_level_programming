#!/usr/bin/python3
""" idk what is the documentation for python script """
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

try:
    save(load("add_item.json") + sys.argv[1:], "add_item.json")
except:
    save(sys.argv[1:], "add_item.json")
