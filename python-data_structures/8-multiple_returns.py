#!/usr/bin/python3
def multiple_returns(sentence):
    if not sentence or sentence == "":
        return
    return (len(sentence), sentence[0])
