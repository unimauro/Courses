def a():
    print('a() fue llamado')
    b()
    print('a() está corriendo')

def b():
    print('b() fue llamado')
    c()
    print('b() está corriendo')

def c():
    print('c() fue llamado')
    print('c() está corriendo')

a()


