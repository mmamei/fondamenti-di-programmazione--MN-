
def insersci_numero():
    '''
    questa funzione chiede un numero come input al giocatore
    e restituisce il numero inserito
    '''
    while True:
        try:
            numero = int(input("Inserisci un numero: "))
            return numero
        except:
            print('Input non valido')
    


def genera_numero_casuale(min_int=1, max_int=100):
    '''
    questa funzione genera un numero casuale tra 1 e 100
    e lo restituisce
    '''
    import random
    numero_casuale = random.randint(min_int, max_int)
    return numero_casuale


def valuta_numero(n, numero_casuale):
    '''
    questa funzione valuta il numero inserito dal giocatore
    confrontandolo con il numero casuale generato
    e restituisce una stringa che indica se il numero è
    troppo basso, troppo alto o corretto
    '''
    if n < numero_casuale:
        return "Troppo basso"
    elif n > numero_casuale:
        return "Troppo alto"
    else:
        return "Corretto"


def gioca():
    '''
    questa funzione gestisce il gioco, il giocatore ha
    10 tentativi per indovinare il numero casuale.
    Se indovina, vince; altrimenti, perde.
    Stampa vinci se vinci, altrimenti stampa perdi
    '''
    numero_casuale = genera_numero_casuale()
    # print(numero_casuale) # per test, rimuovere in produzione
    tentativi = 6
    for i in range(tentativi):
        n = insersci_numero()
        risultato = valuta_numero(n, numero_casuale)
        print(risultato)
        if risultato == "Corretto":
            print("Hai vinto!")
            return
    print("Hai perso! Il numero era:", numero_casuale)  

gioca()