#!/usr/bin/env python3
# Copyright 2009-2017 BHG http://bw.org/

secret = 'swordfish'
pw = ''
auth = False
count = 0
max_attempt = 5
while pw != secret:
    count += 1
    if count > max_attempt:
        break
    # if count == 3: continue Esto se saltaría el flujo normal del bucle y cuando valiera 3 no haría nada y pasría al
    # siguiente
    pw = input(f"{count}: What's the secret word? ")
else:  # Else se utliza para añadir un bloque en el caso que el bucle termine sin un break con normalidad.
    auth = True

print("Authoriszed" if auth else "Calling the FBI...")