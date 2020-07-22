#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def main():
    for i in inclusive_range(25):
        print(i, end=' ')  # Parameter end of print end: Optional[str]
    print()


def inclusive_range(*args):  # utilizamos el número de argumentos variables
    numargs = len(args)  # guardamos en una variable el número de argumentos metidos, length del array de args
    start = 0  # desde dónde empezamos a contar
    step = 1  # cada cuánto pasa al siguente
    
    # initialize parameters
    if numargs < 1:
        raise TypeError(f'expected at least 1 argument, got {numargs}')
    elif numargs == 1:
        stop = args[0]
    elif numargs == 2:
        (start, stop) = args
    elif numargs == 3:
        (start, stop, step) = args
    else:
        raise TypeError(f'expected at most 3 arguments, got {numargs}')

    # generator
    i = start
    while i <= stop:
        #  Now yield is like return except it's for a generator. It yields a value and then after it yields the value
        #  the function continues until it yields the next value
        yield i
        i += step


if __name__ == '__main__': main()
