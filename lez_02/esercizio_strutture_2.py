
import json

def stampa_menu():
    '''
    1. Inserisci Studente
    2. Aggiungi voto a Studente 
    3. Stampa
    4. Calcola media voti Studente 
    5. Esci 
    '''
    print('''
    1. Inserisci Studente
    2. Aggiungi voto a Studente
    3. Stampa
    4. Calcola media voti Studente
    5. Esci
    ''')

def inserisci_studente(classe):
    nome = input("Nome studente e cognome: ")
    if nome in classe:
        print("Studente già esistente.")
    else:
        classe[nome] = []
        print(f"Studente {nome} inserito.")

def aggiungi_voto():
    nome = input("Nome studente e cognome: ")
    if nome not in classe:
        print("Studente non trovato.")
    else:
        try:
            voto = float(input("Inserisci il voto (0-10): "))
            if 0 <= voto <= 10:
                classe[nome].append(voto)
                print(f"Voto {voto} aggiunto a {nome}.")
            else:
                print("Voto non valido. Deve essere tra 0 e 10.")
        except ValueError:
            print("Input non valido. Inserisci un numero.")

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

def main():

    while True:
        stampa_menu()
        scelta = input("Scegli un'opzione (1-5): ")
        if scelta == '1':
            inserisci_studente(classe)
        elif scelta == '2':
            aggiungi_voto()
        elif scelta == '3':
            stampa_classe()
        elif scelta == '4':
            calcola_media()
        elif scelta == '5':
            print("Uscita dal programma.")
            with open("data/classe.json", "w") as f:
                json.dump(classe, f)
            break
        else:
            print("Scelta non valida. Riprova.")

classe = {}
try:
    with open("data/classe.json", "r") as f:
        classe = json.load(f)
except:
    classe = {}

main()
