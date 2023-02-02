#!/usr/bin/python3
""" Indent and print a text line by line """


def text_indentation(text):
    """ Micka == bad """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    text = text.replace("\n", "")
    text = text.replace(".", ".\n\n")
    text = text.replace("?", "?\n\n")
    text = text.replace(":", ":\n\n")

    print(text, end="")
