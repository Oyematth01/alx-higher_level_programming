#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
numb_str = str(number)
if numb_str > '5':
    print(f"Last digit of {number} is {numb_str[-1]} and is greater than 5")
elif numb_str == '0':
    print(f"Last digit of {number} is {numb_str[-1]} and is 0")
elif int(numb_str[-1]) < 6 and int(numb_str[-1]) != 0:
    print(f"Last digit of {number} is {numb_str[-1]} and is less than 6 and not 0")
