#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = True
print('x is {}'.format(x))
print(type(x))

x = False
print('x is {}'.format(x))
print(type(x))

x = 7 > 5
print('x is {}'.format(x))
print(type(x))

# Ausencia de valor
x = None
print('x is {}'.format(x))
print(type(x))

x = 0  # 0 Es false
# None es false
# Empty screen is false
if x:
    print("True")
else:
    print("False")


x = "" # Empty screen is false

if x:
    print("True")
else:
    print("False")

x = None # None es false

if x:
    print("True")
else:
    print("False")
