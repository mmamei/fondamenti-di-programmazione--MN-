ancora = 'sì'
while ancora == 'sì':
	numero1 = float(input("Inserisci il primo numero: "))
	operazione = input("Inserisci l'operazione (+, -, *, /): ")
	numero2 = float(input("Inserisci il secondo numero: "))

	if operazione == "+":
		risultato = numero1 + numero2
		print("Risultato:", risultato)
	elif operazione == "-":
		risultato = numero1 - numero2
		print("Risultato:", risultato)
	elif operazione == "*":
		risultato = numero1 * numero2
		print("Risultato:", risultato)
	elif operazione == "/":
		if numero2 == 0:
			print("Errore: non si può dividere per zero.")
		else:
			risultato = numero1 / numero2
			print("Risultato:", risultato)
	else:
		print("Operazione non valida.")
	ancora = input("Vuoi fare un'altra operazione? (sì/no): ").lower()