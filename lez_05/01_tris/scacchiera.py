
def crea_scacchiera():
    '''
    Questa funzine crea una scacchiera 3*3 per il gioco del tris.
    Ritorna la scacchiera come lista di liste di stringhe.
    Inizializza la scacchiera con stringhe vuote per rappresentare le caselle vuote.
    '''
    return [['' for _ in range(3)] for _ in range(3)]

def metti_pedina(scacchiera, riga, colonna, simbolo):
    '''
    Questa funzione posiziona una pedina sulla scacchiera.
    Controlla che la posizione sia valida e che la casella sia vuota.

    >>> scacchiera = crea_scacchiera()
    >>> metti_pedina(scacchiera, 0, 0, 'X')
    True
    >>> metti_pedina(scacchiera, 0, 0, 'O')
    False
    >>> metti_pedina(scacchiera, 5, 5, 'O')
    False
    '''
    if 0 <= riga < 3 and 0 <= colonna < 3:
        if scacchiera[riga][colonna] == '':
            scacchiera[riga][colonna] = simbolo
            return True
    return False

def tris(scacchiera, simbolo):
    '''
    Questa funzione controlla se un giocatore ha vinto.
    Controlla tutte le righe, colonne e diagonali per vedere se ci sono tre simboli uguali.

    >>> scacchiera = crea_scacchiera()
    >>> metti_pedina(scacchiera, 0, 0, 'X')
    True
    >>> metti_pedina(scacchiera, 0, 1, 'X')
    True
    >>> metti_pedina(scacchiera, 0, 2, 'X')
    True
    >>> tris(scacchiera, 'X')
    True
    '''
    # Controlla righe
    for row in scacchiera:
        if all(cell == simbolo for cell in row):
            return True
    # Controlla colonne
    for col in range(3):
        if all(scacchiera[row][col] == simbolo for row in range(3)):
            return True
    # Controlla diagonali
    if all(scacchiera[i][i] == simbolo for i in range(3)):
        return True
    if all(scacchiera[i][2 - i] == simbolo for i in range(3)):
        return True
    return False

def scacchiera_piena(scacchiera):
    '''
    Questa funzione controlla se la scacchiera è piena.
    Ritorna True se non ci sono caselle vuote, altrimenti False.
    '''
    for row in scacchiera:
        if '' in row:
            return False
    return True

import doctest
doctest.testmod(verbose=True)