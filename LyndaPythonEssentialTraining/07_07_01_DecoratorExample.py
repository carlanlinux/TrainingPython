#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

import time


def elapsed_time(f):
    def wrapper():
        t1 = time.time()
        f()
        t2 = time.time()
        print(f'Elapsed time: {(t2 - t1) * 1000} ms')
    return wrapper


@elapsed_time  # Este decorator está envolviendo la función elapsed timem llama a la primera función y ejecuta dentro
# la función de abajo que se le pasa como parámetro a la que lo envuelve
def big_sum():
    num_list = []
    for num in (range(0, 10000)):
        num_list.append(num)
    print(f'Big sum: {sum(num_list)}')


def main():
    big_sum()


if __name__ == '__main__': main()
