#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


x = [1, 2, 3, 4, 5]  # Sequence type es como un array
y = (1, 2, 3, 4, 5)  # tuple es como un array pero con paréntesis. Las tuple no se pueden cambiar. Sin non mutables
# Por defecto mejor usar los paréntesis y sólo usar los corchetes si sé que en un futuro voy a tener que cambiar algún valor
x[2] = 42
for i in x:
    print('i is {}'.format(i))
print(type(x))

x = range(5)
for i in x:
    print('i is {}'.format(i))
print(type(x))

x = range(5, 200, 10)  # numero inicial, numero final, cada cuánto se incrementa hasta llegar el final
for i in x:
    print('i is {}'.format(i))
print(type(x))

x = list(range(5))  # lista meto los números en una lista y puedo cambiarlo con notación array
x[2] = 42
for i in x:
    print('i is {}'.format(i))
print(type(x))

x = {'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5}  # Creamos diccionario clave/valor
x['three'] = 42
for k, v in x.items():  # Lo recorremos inclyendo dos variables y con el nombre del diccionario que queremos recorrer
    # llamando a su método items.
    print('key: {}, value: {}'.format(k, v))
print(type(x))
