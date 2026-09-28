from scacchiera import metti_pedina
from gui import  chiedi_mossa

def crea_giocatore(simbolo, computer):
    '''
    Crea un giocatore come dizionario con simbolo e tipo (umano o computer).
    '''
    return {
        "simbolo": simbolo,
        "computer": computer
    }

def gioca(giocatore, scacchiera):
    '''
    questa funzione permette di gestire il turno di un giocatore.
    Se il giocatore è un computer, la mossa viene scelta automaticamente
    a caso, il computer genera due numeri casuali tra 0 e 2 per riga e colonna.
    riprova fino a quando non trova una casella vuota.
    Se il giocatore è umano, la mossa viene chiesta tramite la funzione gui.chiedi_mossa.
    A quel punto la mossa viene inserita nella scacchiera tramite la funzione metti_pedina.
    Se la mossa non è valida, viene chiesto di nuovo.
    '''
    import random
    while True:
        if giocatore["computer"]:
            riga = random.randint(0, 2)
            colonna = random.randint(0, 2)
        else:
            riga, colonna = chiedi_mossa(giocatore)
        if metti_pedina(scacchiera, riga, colonna, giocatore["simbolo"]):
            break   