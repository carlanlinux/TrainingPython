#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def f1(f):
    def f2():
        print('This is before the function call')
        f()
        print('This is after the function call')
    return f2


def f3():
    print('this is f3')


# f3 = f1(f3) --> Asignas a la función 3 el valor de la f1 pasándole como argumento la f3 de forma recursiva
# f3() --> Ejecutar la función
# Esto se sustituye con el decorator que sería lo de abajo:
@f1
def f3():
    print('this is f3')


f3()
