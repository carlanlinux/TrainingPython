#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


x = [1, "two", 3.0, 'four', 5]
y = (1, "two", 3.0, 'four', 5)
print('x is {}'.format(x))
print(type(x))
print(type(y))
print(id(x[1]))
print(id(y[1]))
print('ahora es patata')
x[1] = "patata"
print(id(x[1]))
print(id(y[1]))

if x[1] is y[1]:
    print('yep')
else:
    print('nope')

if isinstance(y, tuple):
    print('Is a tuple')
elif isinstance(y, list):
    print("Is a list")
else:
    print("nope")
