#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    numberPrint = 0
    for i in range(x):
        my_list[i]
        try:
            print("{:d}".format(my_list[i]), end="")
            numberPrint += 1
        except:
            numberPrint = numberPrint
    print()
    return numberPrint
