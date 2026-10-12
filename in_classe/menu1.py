studenti = {}

while True:
	print("\n--- Gestione studenti ---")
	print("1. Inserisci studente")
	print("2. Cancella studente")
	print("3. Aggiungi voto")
	print("4. Stampa tutto")
	print("5. Calcola media studente")
	print("6. Esci")

	scelta = input("Scegli un'operazione: ")

	if scelta == "1":
		nome = input("Nome dello studente: ").strip()
		if nome:
			studenti[nome] = []
			print(f"Studente {nome} inserito con media iniziale 0.")
		else:
			print("Il nome non può essere vuoto.")

	elif scelta == "2":
		nome = input("Nome dello studente da cancellare: ").strip()
		if nome in studenti:
			del studenti[nome]
			print(f"Studente {nome} cancellato.")
		else:
			print("Studente non trovato.")

	elif scelta == "3":
		nome = input("Nome dello studente: ").strip()
		if nome not in studenti:
			print("Studente non trovato.")
		else:
			try:
				voto = int(input("Nuovo Voto: "))
				studenti[nome].append(voto)
				print("Voto aggiunto")
			except ValueError:
				print("Il voto deve essere un numero.")

	elif scelta == "4":
		if studenti:
			for nome, media in studenti.items():
				print(nome, media)
		else:
			print("Non ci sono studenti da stampare.")
			
	elif scelta == '5':
		nome = input("Nome dello studente: ").strip()
		if nome not in studenti:
			print("Studente non trovato.")
		else:
			if len(studenti[nome]) == 0:
				print('Lo Studente non ha ancora voti')
			else:
				print('La media è', sum(studenti[nome]) / len(studenti[nome]))
				

	elif scelta == "6":
		print("Arrivederci!")
		break

	else:
		print("Scelta non valida. Inserisci un numero da 1 a 5.")
