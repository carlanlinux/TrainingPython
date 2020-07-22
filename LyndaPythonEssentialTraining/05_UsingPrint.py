x = 42
# Usando py versión 3 se usa format para dar formato. Versiones anteriores se hacía con placeholdars. era %d y luego
# pasando el valor que ese placeholder admitiera
print('Hello World. %d' % x)
# forma normal de hacerlo
print('Hello World. {}'.format(x))
# forma más actual de hacerlo
print(f'Hello World. {x}')
