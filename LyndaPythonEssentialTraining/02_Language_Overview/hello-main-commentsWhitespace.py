import platform


def main():
    message()


def message():
    print('This is pyton version {}'.format(platform.python_version()))
    print('line 2')
    if False:
        print('line 3')             # Simulación de comentario en bloque
    else:                           # haciendo cosas así
        print('not true')           # siempre poner # segudo de un espacio

print('Como está antes del main y dentado fuera de las funciones aparecerá esto primero')

if __name__ == '__main__':
    main()
