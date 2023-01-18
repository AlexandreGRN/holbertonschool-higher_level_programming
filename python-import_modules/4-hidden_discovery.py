#!/usr/bin/python3
import hidden_4
if __name__ == "__main__":
    #go through the whole file // dir return an array of strings -> i == string
    for i in (dir(hidden_4)):
        #search for target words then print it
        if i[0:2] != "__":
            print(i)