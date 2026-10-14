def crea_scacchiera():
    '''
    Crea una scacchiera vuota per il gioco del tris.
    E' una lista di liste 3 * 3 
    Inizialmente contiene solo spazi vuoti ' '.
    '''
    scacchiera = []
    for _ in range(3):
        riga = [' ' for _ in range(3)]
        scacchiera.append(riga)
    return scacchiera

def gioca(scacchiera, simbolo):
    '''
    Permette a un giocatore di fare una mossa.
    Chiede all'utente di inserire le coordinate della cella in cui vuole posizionare il suo simbolo.
    Aggiorna la scacchiera con il simbolo del giocatore.
    '''
    while True:
        try:
            riga = int(input(f"Inserisci la riga (0-2) per {simbolo}: "))
            colonna = int(input(f"Inserisci la colonna (0-2) per {simbolo}: "))
            if 0 <= riga < 3 and 0 <= colonna < 3:
                if scacchiera[riga][colonna] == ' ':
                    scacchiera[riga][colonna] = simbolo
                    break
                else:
                    print("Cella già occupata. Scegli un'altra cella.")
            else:
                print("Coordinate non valide. Inserisci valori tra 0 e 2.")
        except ValueError:
            print("Input non valido. Inserisci numeri interi.")

def gioca_computer(scacchiera, simbolo):
    '''
    Permette al computer di fare una mossa.
    Sceglie casualmente una cella vuota e posiziona il suo simbolo.
    '''
    import random
    while True:
        riga = random.randint(0, 2)
        colonna = random.randint(0, 2)
        if scacchiera[riga][colonna] == ' ':
            scacchiera[riga][colonna] = simbolo
            break

def stampa_scacchiera(scacchiera):
    '''
    Stampa la scacchiera in modo leggibile.
    '''
    for riga in range(3):
        for colonna in range(3):
            print(" "+scacchiera[riga][colonna]+" ", end='')
            if colonna < 2:
                print(' | ', end='')
        print()
        print()

def tris(scacchiera, simbolo):
    '''
    Controlla se il giocatore con il simbolo specificato ha vinto.
    Restituisce True se ha vinto, altrimenti False.
    '''
    # Controlla righe
    for riga in scacchiera:
        vincita_riga = True
        for cella in riga:
            if cella != simbolo:
                vincita_riga = False
                break
        if vincita_riga:
            return True

    # Controlla colonne
    for colonna in range(3):
        vincita_colonna = True
        for riga in range(3):
            if scacchiera[riga][colonna] != simbolo:
                vincita_colonna = False
                break
        if vincita_colonna:
            return True

    # Controlla diagonali
    vincita_diagonale_1 = True
    for i in range(3):
        if scacchiera[i][i] != simbolo:
            vincita_diagonale_1 = False
            break
    if vincita_diagonale_1:
        return True

    vincita_diagonale_2 = True
    for i in range(3):
        if scacchiera[i][2 - i] != simbolo:
            vincita_diagonale_2 = False
            break
    if vincita_diagonale_2:
        return True
    return False

def ce_spazio(scacchiera):
    '''
    Controlla se ci sono ancora spazi vuoti sulla scacchiera.
    Restituisce True se ci sono spazi vuoti, altrimenti False.
    '''
    for riga in scacchiera:
        for cella in riga:
            if cella == ' ':
                return True
    return False

scacchiera = crea_scacchiera()
while True:
    stampa_scacchiera(scacchiera)
    gioca(scacchiera, 'X')
    if tris(scacchiera, 'X'):
        stampa_scacchiera(scacchiera)
        print("Hai vinto X!")
        break
    if not ce_spazio(scacchiera):
        stampa_scacchiera(scacchiera)
        print("Pareggio!")
        break
    gioca_computer(scacchiera, 'O')
    if tris(scacchiera, 'O'):
        stampa_scacchiera(scacchiera)
        print("Il ha vinto O!")
        break
    if not ce_spazio(scacchiera):
        stampa_scacchiera(scacchiera)
        print("Pareggio!")
        break