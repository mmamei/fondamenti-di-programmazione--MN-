def inserisci_studente(classe, nome):
    if nome in classe:
        return "Studente già esistente."
    else:
        classe[nome] = []
        return f"Studente {nome} inserito."


def aggiungi_voto(classe, nome, voto):
    if nome not in classe:
        return "Studente non trovato."
    else:
        try:
            voto = float(voto)
            if 0 <= voto <= 10:
                classe[nome].append(voto)
                return f"Voto {voto} aggiunto a {nome}."
            else:
                return "Voto non valido. Deve essere tra 0 e 10."
        except ValueError:
            return "Input non valido. Inserisci un numero."

def stampa_classe():
    if not classe:
        print("Nessuno studente nella classe.")
    else:
        for nome, voti in classe.items():
            print(f"{nome}: Voti: {voti}")


def calcola_media():
    nome = input("Nome studente e cognome: ")
    if nome not in classe:
        print("Studente non trovato.")
    else:
        voti = classe[nome]
        if not voti:
            print(f"{nome} non ha voti.")
        else:
            media = sum(voti) / len(voti)
            print(f"Media voti di {nome}: {media:.2f}")
