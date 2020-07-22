#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/


def isprime(n):
    if n <= 1:
        return False
    # cuando sabemos cuántas veces recorrer un bucle podemos usar range(número veces)
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True


def list_primes():
    for n in range(100):
        if isprime(n):
            # end lo usamos para poner algo diferente al final del print en vez del salto de línea por defecto
            # flush es para limpiar el output buffer
            print(n, end=' ', flush=True)


list_primes()

# n = 5
# if isprime(n):
#     print(f'{n} is prime')
# else:
#     print(f'{n} not prime')
