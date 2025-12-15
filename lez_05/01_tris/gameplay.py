
from giocatore import *
from scacchiera import *
from gui import *


def crea_partita(computer1, computer2):
    '''
    Crea un dizionario per rappresentare una partita.
    Il dizionario conterrà i due giocatori e la scacchiera.
    computer1 e computer2 sono variabili booleane che indicano se i giocatori sono computer o umani.
    il giocatore1 gioca con la 'X'
    il giocatore2 gioca con il 'O'
    '''
    return {
        "giocatore1": crea_giocatore("X", computer1),
        "giocatore2": crea_giocatore("O", computer2),
        "scacchiera": crea_scacchiera()
    }

def play(partita):
    '''
    Questa funzione gestisce il flusso di una partita di tris.
    Alterna i turni tra i due giocatori fino a quando uno vince o la scacchiera è piena.
    Dopo ogni mossa, mostra la scacchiera aggiornata.
    Alla fine, dichiara il vincitore o se la partita è finita in pareggio.
    '''
    scacchiera = partita["scacchiera"]
    giocatore1 = partita["giocatore1"]
    giocatore2 = partita["giocatore2"]
    turno = 0  # 0 per giocatore1, 1 per giocatore2

    while True:
        mostra_scacchiera(scacchiera)
        if turno == 0:
            gioca(giocatore1, scacchiera)
            if tris(scacchiera, giocatore1["simbolo"]):
                mostra_scacchiera(scacchiera)
                print(f'Giocatore {giocatore1["simbolo"]} ha vinto!')
                break
        else:
            gioca(giocatore2, scacchiera)
            if tris(scacchiera, giocatore2["simbolo"]):
                mostra_scacchiera(scacchiera)
                print(f'Giocatore {giocatore2["simbolo"]} ha vinto!')
                break
        if scacchiera_piena(scacchiera):
            mostra_scacchiera(scacchiera)
            print('La partita è finita in pareggio!')
            break
        turno = 1 - turno  # Cambia turno
