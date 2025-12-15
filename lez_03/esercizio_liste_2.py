



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
    return sum(lista)

def media_numeri(lista):
    '''
    calcola la media dei numeri nella lista
    >>> media_numeri([1, 2, 3])
    2.0
    >>> media_numeri([1, 2, 3, 4, 5])
    3.0
    >>> media_numeri([])
    0
    '''
    if len(lista) == 0:
        return 0
    return somma_numeri(lista) / len(lista)

def deviazione_standard(lista):
    '''
    calcola la deviazione standard dei numeri nella lista.
    >>> deviazione_standard([10, 10, 10])
    0.0
    >>> deviazione_standard([1, 2, 3, 4, 5])
    1.4142135623730951
    >>> deviazione_standard([])
    0.0
    '''
    m = media_numeri(lista)
    sq = []
    for x in lista:
        sq.append((x - m) ** 2)
    
    var = media_numeri(sq)
    return var ** 0.5
    

import doctest
doctest.testmod(verbose=False)


n = leggi_numero()
lista = lista_numeri(n)
media = media_numeri(lista)
print(media)
deviazione = deviazione_standard(lista)
print(deviazione)