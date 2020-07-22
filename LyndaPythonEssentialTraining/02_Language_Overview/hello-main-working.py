import platform


def main():
    message()


def message():
    print('This is pyton version {}'.format(platform.python_version()))


if __name__ == '__main__':
    main()
