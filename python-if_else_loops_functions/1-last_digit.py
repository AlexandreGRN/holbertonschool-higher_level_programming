#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)

#get last digit of number
digt = abs(number) % 10

#print depending of last digit value
if digt > 5:
  print("Last digit of", number, "is", digt, "and is greater than 5")
elif digt == 0:
  print("Last digit of", number, "is 0 and is 0")
else:
  print("Last digit of", number, "is", digt, "and is less than 6 and not 0")