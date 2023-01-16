#!/usr/bin/python3
for j in range(9):
    i = j + 1
    for i in range(i, 10):
        if j != 0 | i != 1:
            print(', ', end='')
        print("{}{}".format(j, i), end='')
    i = i + 1
print("\n")
