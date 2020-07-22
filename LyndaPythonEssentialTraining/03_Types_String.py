#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


x = 'Da igual usar comillas simples que dobles'
print('x is {}'.format(x))
print(type(x))

x = "Da igual usar comillas simples que dobles"
print('x is {}'.format(x))
print(type(x))

x = '''
Puedo
poner varias líneas
Con las tres comillas
Que también peuden ser dobles
'''
print('x is {}'.format(x))
print(type(x))

x = 'seven'.capitalize() # Como son clases tienen sus métodos
print('x is {}'.format(x))
print(type(x))

x = 'seven'.upper() # Como son clases tienen sus métodos
print('x is {}'.format(x))
print(type(x))

x = 'SEVEN'.lower() # Como son clases tienen sus métodos
print('x is {}'.format(x))
print(type(x))

# Método format importante. Se usan las {} como placeholders para el valor que queremos poner.
# Primero número máximo de espaciosque va a dejar para el formato y luego el número en cuestión.
# Se pueden invertir el orden y poner condiciones
x = 'seven {} {}'.format(8, 9)
print('x is {}'.format(x))
print(type(x))

# F strings es una forma útil de dar formato, pero sólo está disponible par python 3.6
a = 8
b = 9
# usando :< o :> le dices el número de espacios en blanco que quieres dejar entre los caracteres a derecha < o izquierda >
x = f"seven {a:<9} {b:>9}" # usar f string es lo mismo que usar el método format, normalmente se usa desde una variable
print('x is {}'.format(x))
print(type(x))

# F strings es una forma útil de dar formato, pero sólo está disponible par python 3.6
a = 8
b = 9
# usando :< o :> le dices el número de espacios en blanco que quieres dejar entre los caracteres a derecha < o izquierda >
# si pones un 0 delante del número de ceros es el caracter con lo que lo quiere rellenar
x = f"seven {a:<09} {b:>09}" # usar f string es lo mismo que usar el método format, normalmente se usa desde una variable
print('x is {}'.format(x))
print(type(x))