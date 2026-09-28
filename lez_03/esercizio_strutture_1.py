
'''
Chiedere all'utente di inserire una matrice N * N (un quadrato di numeri)
    * Stampare il quadrato di numeri
    * Calcolare la somma di tutti gli elementi
    * Trovare la riga di somma massima
    * Trovare la colonna di somma massima
'''

def leggi_matrice():
    N = int(input('Inserisci numero di righe e colonne della matrice\n'))
    m = []
    for _ in range(N):
        
        '''
        riga = []
        for _ in range(N):
            riga.append(int(input('Inserisci numero ')))
        '''
        riga = [int(input('Inserisci numero ')) for _ in range(N)]
        
        m.append(riga)
    return m

def stampa_matrice(m):
    for r in m:
        print(r)

def trova_riga_somma_massima(m):
    '''
    restituisce una lista con la riga di somma massima
    >>> trova_riga_somma_massima([[1,2,3],\
                                  [4,5,6],\
                                  [7,8,9]])
    [7, 8, 9]
    >>> trova_riga_somma_massima([[10,2,3]])
    [10, 2, 3]
    >>> trova_riga_somma_massima([])
    
    >>> trova_riga_somma_massima([[-1]])
    [-1]
    '''
    riga_massima = None
    for r in m:
        if riga_massima is None or sum(r) > sum(riga_massima):
            riga_massima = r
    return riga_massima

def trova_colonna_somma_massima(m):
    '''
    restituisce una lista con la colonna di somma massima
    '''
    colonna_massima = [0]
    for j in range(len(m[0])):
        c = [r[j] for r in m]
        if sum(c) > sum(colonna_massima):
            colonna_massima = c
    return colonna_massima

import doctest
doctest.testmod(verbose=True)


m = leggi_matrice()
stampa_matrice(m)
print('riga massima',trova_riga_somma_massima(m))
print('colonna massima',trova_colonna_somma_massima(m))


