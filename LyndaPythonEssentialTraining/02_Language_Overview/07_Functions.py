#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    kitten(5, 6, 7)


# Cualquier argumento con default debe estar detrás que el resto.
def kitten(n, b=1, c=0):
    print(f'{n} Meow.')
    print(n, b, c)


# Indica que que aquí se encuentra el principal
if __name__ == '__main__': main()
