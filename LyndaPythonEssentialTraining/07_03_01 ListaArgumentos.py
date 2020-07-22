#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    kitten('meow', 'grrr', 'purr')

# El * indica que es un argumeto de valores variable. Nos reocorremos todos los args y hacemos las operaciones dentro
# de un if y el else por si no tiene argumentos.


def kitten(*args):
    if len(args):
        for s in args:
            print(s)
    else: print('Meow.')


if __name__ == '__main__': main()
