
def insersci_numero():
    '''
    questa funzione chiede un numero come input al giocatore
    e restituisce il numero inserito
    '''
    numero = int(input("Inserisci un numero: "))
    return numero

def disegna_quadrato_asterisco(lato):
    '''
    questa funzione disegna un quadrato di asterischi
    di lato "lato"
    usa for i e for j per disegnare il quadrato
    '''
    for i in range(lato):
        for j in range(lato):
            if i == j:
                print("*", end="  ")
            else:
                print(".", end="  ")
        print()  # vai a capo dopo ogni riga


lato = insersci_numero()
disegna_quadrato_asterisco(lato)