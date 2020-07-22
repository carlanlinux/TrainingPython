#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

x = 42
y = 73

if x < y:
    z = x * y
    print('x < y: x is {} and y is {}'.format(x, y))
    print('line 1')
    print('line 1')
    print('line 3')

# El ámbito de las variables se define por las funciones no por los bloques
print('z has de value of {}'.format(z))
