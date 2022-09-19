def cortoConBaseCase(hacerUnaLlamadaRecursiva):
    print('cortoConBaseCase(%s) llamando.' % hacerUnaLlamadaRecursiva)

    if not hacerUnaLlamadaRecursiva:
        #Caso Base
        print('Retornando desde el Caso Base.')
        return
    else:
        #Caso Recursivo
        cortoConBaseCase(False)
        print('Retornando desde una llamada recursiva.')
        return

print('Llamando cortoConBaseCase(False):')
cortoConBaseCase(False)
print()
print('Llamando cortoConBaseCase(True):')
cortoConBaseCase(True)
