def mostra_scacchiera(scacchiera):
    for row in scacchiera:
        print(' | '.join(cell if cell else ' ' for cell in row))
        print('-' * 9)
    return True

def chiedi_mossa(giocatore):
    riga = int(input(f'Giocatore {giocatore["simbolo"]}, inserisci la riga (0-2): '))
    colonna = int(input(f'Giocatore {giocatore["simbolo"]}, inserisci la colonna (0-2): '))
    return (riga, colonna)    