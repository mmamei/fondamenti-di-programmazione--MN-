
import json

from gestione_studenti import *

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


def main():

    while True:
        stampa_menu()
        scelta = input("Scegli un'opzione (1-5): ")
        if scelta == '1':
            nome = input("Nome studente e cognome: ")
            r = inserisci_studente(classe, nome)
            print(r)
        elif scelta == '2':
            nome = input("Nome studente e cognome: ")
            voto = input("Inserisci il voto (0-10): ")
            r = aggiungi_voto(classe, nome, voto)
            print(r)
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
