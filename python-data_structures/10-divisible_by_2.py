#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if not my_list:
        return
    multiTorF = []
    for i in my_list:
        if i % 2 == 0:
            multiTorF.append(True)
        else:
            multiTorF.append(False)
    return multiTorF
