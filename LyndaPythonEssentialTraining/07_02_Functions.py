#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    x = 5
    kitten(x)
    print(f'in main: x is {x}')


# Cualquier argumento con default debe estar detrás que el resto.
def kitten(a):
    a = 4
    print('Meow.')
    print(a)


# Indica que que aquí se encuentra el principal
if __name__ == '__main__': main()
