def conteoDescendente(numero):
    print(numero)
    if numero == 0:
        #Caso Base
        print('Buscando el Caso Base')
        return
    else:
        #Caso Recursivo
        conteoDescendente(numero -1)
        print(numero, 'retornando')
        return

conteoDescendente(3)
