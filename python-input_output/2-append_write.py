#!/usr/bin/python3
""" doc """


def append_write(filename="", text=""):
    """ doc """
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        f.close
    return len(text)
