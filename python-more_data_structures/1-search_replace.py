#!/usr/bin/python3
def search_replace(my_list, search, replace):
    newList = []
    # go through full list
    for i in my_list:
        # copy or replace
        if i == search:
            newList.append(replace)
        else:
            newList.append(i)
    return newList
