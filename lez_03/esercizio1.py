def leggi_numero():
    return int(input("Inserisci un numero: "))

def leggi_operazione():
    return input("Inserisci un'operazione (+, -, *, /): ")

def calcola(a, b, operazione):
    if operazione == "+":
        return a + b
    elif operazione == "-":
        return a - b
    elif operazione == "*":
        return a * b
    elif operazione == "/":
        return a / b 

def main():
    '''
    questa funzione crea un ciclo per 
    chiedere operazioni ed eseeguirle 
    finchè il progrmma non viene interrotto
    '''
    while True:
        a = leggi_numero()
        op = leggi_operazione()
        b = leggi_numero()
        risultato = calcola(a, b, op)
        print(a, op, b, '=', risultato)

main()