from biblioteca import *
'''
aggiungi_libro("Il nome della rosa", "Umberto Eco")
aggiungi_libro("1984", "George Orwell")
aggiungi_libro("1984", "George Orwell")
aggiungi_utente("Mario Rossi")
aggiungi_utente("Luigi Bianchi")
aggiungi_utente("Marco Mamei")

id = cerca_utente("Mario Rossi")[0]
ok = presta_libro(id, "1984", "2025-10-30")
id = cerca_utente("Luigi Bianchi")[0]
ok = presta_libro(id, "1984", "2025-10-30")
id = cerca_utente("Marco Mamei")[0]
ok = presta_libro(id, "1984", "2025-10-30") # fallisce
print(ok)

id_user = cerca_utente("Mario Rossi")[0]
id_libro = cerca_libri_in_prestito(id_user, "1984")[0]
restituisci_libro(id_user, id_libro, "2025-11-30")

id = cerca_utente("Marco Mamei")[0]
ok = presta_libro(id, "1984", "2025-11-30") # fallisce
print(ok)
'''

def crea_menu():
    '''
    crea un ciclo di menu per l'utente.
    Mostra il menu con le opzioni disponibili e 
    chiede all'utente di scegliere un'opzione.
    Poi chiama la funzione corrispondente all'opzione scelta.
    Usando quelle definite in biblioteca.py.
    Il menu permette di:
    - Aggiungere un libro
    - Aggiungere un utente
    - Vedere lista dei libri
    - Vedere lista degli utenti
    - Prestare un libro
    - Restituire un libro
    '''
    while True:
        print("\nMenu Biblioteca")
        print("1. Aggiungi un libro")
        print("2. Aggiungi un utente")
        print("3. Vedi lista dei libri disponibili")
        print("4. Vedi lista degli utenti")
        print("5. Presta un libro")
        print("6. Restituisci un libro")
        print("7. Esci")
        
        scelta = input("Scegli un'opzione (1-7): ")
        
        if scelta == '1':
            titolo = input("Inserisci il titolo del libro: ")
            autore = input("Inserisci l'autore del libro: ")
            aggiungi_libro(titolo, autore)
        
        elif scelta == '2':
            nome = input("Inserisci il nome dell'utente: ")
            aggiungi_utente(nome)
        
        elif scelta == '3':
            libri_disponibili = lista_libri_disponibili()
            for libro in libri_disponibili:
                print(libro)

        elif scelta == '4':
            print("Lista degli utenti:")
            for utente in utenti:
                print(f"ID: {utente['id']}, Nome: {utente['nome']}")        
        elif scelta == '5':
            id_user = int(input("Inserisci l'ID dell'utente: "))
            titolo_libro = input("Inserisci il titolo del libro da prestare: ")
            data = input("Inserisci la data del prestito (YYYY-MM-DD): ")
            if presta_libro(id_user, titolo_libro, data):
                print(f"Libro '{titolo_libro}' prestato con successo a {id_user}.")
            else:
                print(f"Impossibile prestare il libro '{titolo_libro}'. Potrebbe essere già in prestito.")
        elif scelta == '6':
            id_user = int(input("Inserisci l'ID dell'utente: "))
            titolo_libro = input("Inserisci il titolo del libro da restituire: ")
            data_restituzione = input("Inserisci la data di restituzione (YYYY-MM-DD): ")
            libri_in_presito = cerca_libri_in_prestito(id_user, titolo_libro)
            if libri_in_presito:
                id_libro = libri_in_presito[0]
                r = restituisci_libro(id_user, id_libro, data_restituzione)
                if r:
                    data_prestito, data_restituzione = r
                    penale = calcola_penale(data_prestito, data_restituzione)
                    print(f"Penale da pagare: {penale} euro.")
                    print(f"Libro '{titolo_libro}' restituito con successo da {id_user}.")
                else:
                    print(f"Errore nella restituzione del libro '{titolo_libro}'.")
        elif scelta == '7':
            print("Uscita dal programma.")
            break

crea_menu()