def leggi_numero():
    return int(input("Inserisci un numero: "))

def somma_numeri(n):
    '''
    leggi n numeri e calcola la loro somma
    '''
    somma = 0
    for i in range(n):
        somma += leggi_numero()
    return somma

n = leggi_numero()
risultato = somma_numeri(n)
print("La somma dei", n, "numeri è:", risultato)