def leggi_numero():
    return int(input("Inserisci un numero: "))

def lista_numeri(n):
    '''
    leggi una lista di n numeri
    '''

    lista = []
    for _ in range(n):
        lista.append(leggi_numero())
    return lista

def somma_numeri(lista):
    '''
    somma gli elementi della lista con una somma in accumulo
    '''
    somma = 0
    for x in lista:
        somma += x
    return somma


n = leggi_numero()
lista = lista_numeri(n)
somma = somma_numeri(lista)
print(somma)