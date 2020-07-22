import platform

# Es una expressión y un statement a la vez
version = platform.python_version()
# Aunque no devuelva nada las funciones en py siempre devuelven algo, aunque sea none
print('This is python version {}'.format(version))
