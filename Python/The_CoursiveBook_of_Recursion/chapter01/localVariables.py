def a():
    spam='Ant'
    print('spam es' + spam)
    b()
    print('spam es' + spam)

def b():
    spam='Perro'
    print('spam es' + spam)
    c()
    print('spam es' + spam)

def c():
    spam='Guanaco'
    print('spam es' + spam)

a()
