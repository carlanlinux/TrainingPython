#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/
#importamos al completo de la librería decimal para poder trabajar con dienero sin problemas
from decimal import *

x = 7 * 3
print('x is {}'.format(x))
print(type(x))

x = 7.0 * 3
print('x is {}'.format(x))
print(type(x))

x = 7 / 3  # Devuelve un float porque lo divide con el resto
print('x is {}'.format(x))
print(type(x))

x = 7 // 3  # Devuelve un entero porque no tiene en cuenta el resto, sólo el cociente
print('x is {}'.format(x))
print(type(x))

x = 7 % 3  # Devuelve un entero porque no tiene en cuenta el resto, sólo el cociente
print('x is {}'.format(x))
print(type(x))

# Ojo no usar floats para dinero, porque por la precisión del float, hay operaciones que no hace correctamente
x = .1 + .1 + .1 - .3
print('x is {}'.format(x))
print(type(x))

# Ojo no usar floats para dinero, porque por la precisión del float, hay operaciones que no hace correctamente
# Para eso hacer un import del tipo decimal que se encarga de gestionarlo
a = Decimal('.10')
b = Decimal('.30')
x = a + a + a - b
print('x is {}'.format(x))
print(type(x))
