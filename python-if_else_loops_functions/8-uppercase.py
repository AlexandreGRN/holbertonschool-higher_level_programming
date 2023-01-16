def uppercase(str):
    for c in range (len(str)):
        if ord(str[c]) >= 97 and ord(str[c]) <= 122:
            print("{}".format(chr(ord(str[c]) - 32)), end = '')
        else:
            print("{}".format(str[c]), end = '')
