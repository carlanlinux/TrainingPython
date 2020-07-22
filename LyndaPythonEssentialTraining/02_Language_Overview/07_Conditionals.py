x = 42
y = 73

if x > y:
    print('x > y: is {} and y is {}'.format(x, y))
elif x < y:
    print('x < y: is {} and y is {}'.format(x, y))
elif x == 5:  # no hay case en python, se usan varios elif con lo que se necesite
    print('x = y do stuff')
else:
    print('do something else')
