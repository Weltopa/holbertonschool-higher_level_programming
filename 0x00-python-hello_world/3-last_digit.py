#!/usr/bin/python3
import random
number = random.randit(-10000, 10000)
x = number
if x < 0:
    x = x * -1
x = x % 10
if number < 0:
    x = x * -1
if x > 5:
    print("Last digit of", number, "is", x, "and is greater than 5")
elif x == 0:
    print("Last digit of", number, "is", x, "and is 0")
else:
    print("Last digit of", number, "is", x, "and is less than 6 and not 0")
