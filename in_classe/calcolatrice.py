

def calcola(numero1, numero2, operazione):
	if operazione == "+":
			risultato = numero1 + numero2
			return str(risultato)
			#print("Risultato:", risultato)
	elif operazione == "-":
			risultato = numero1 - numero2
			return str(risultato)
	elif operazione == "*":
			risultato = numero1 * numero2
			return str(risultato)
	elif operazione == "/":
			if numero2 == 0:
				return "Errore: non si può dividere per zero."
			else:
				risultato = numero1 / numero2
				return str(risultato)
	else:
			return "Operazione non valida."

	
if __name__ == '__main__':
	ancora = 'sì'
	while ancora == 'sì':
		numero1 = float(input("Inserisci il primo numero: "))
		operazione = input("Inserisci l'operazione (+, -, *, /): ")
		numero2 = float(input("Inserisci il secondo numero: "))
		print(calcola(numero1, numero2, operazione))
		ancora = input("Vuoi fare un'altra operazione? (sì/no): ").lower()