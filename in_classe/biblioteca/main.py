from datetime import datetime

import biblioteca


def stampa_menu():
    print("\n--- Biblioteca ---")
    print("1. Aggiungi libro")
    print("2. Aggiungi utente")
    print("3. Cerca libro")
    print("4. Cerca utente")
    print("5. Presta libro")
    print("6. Restituisci libro")
    print("7. Lista libri")
    print("8. Lista utenti")
    print("9. Esci")


def leggi_intero(messaggio):
    try:
        return int(input(messaggio))
    except ValueError:
        print("Inserisci un numero intero.")
        return None


def aggiungi_libro():
    titolo = input("Titolo: ").strip()
    autore = input("Autore: ").strip()
    id_libro = biblioteca.aggiungi_libro(titolo, autore)
    print(f"Libro aggiunto con ID {id_libro}.")


def aggiungi_utente():
    nome = input("Nome: ").strip()
    cognome = input("Cognome: ").strip()
    anno = leggi_intero("Anno di nascita: ")
    if anno is None:
        return
    id_utente = biblioteca.aggiungi_utente(nome, cognome, anno)
    print(f"Utente aggiunto con ID {id_utente}.")


def cerca_libro():
    titolo = input("Titolo da cercare: ").strip()
    id_libri = biblioteca.cerca_libro(titolo)
    if not id_libri:
        print("Nessun libro trovato.")
        return
    for id_libro in id_libri:
        libro = biblioteca.libri[id_libro]
        stato = "in prestito" if libro["prestato"] else "disponibile"
        print(f"ID {id_libro}: {libro['titolo']} - {libro['autore']} ({stato})")


def cerca_utente():
    nome = input("Nome da cercare: ").strip()
    cognome = input("Cognome da cercare: ").strip()
    id_utenti = biblioteca.cerca_utente(nome, cognome)
    if not id_utenti:
        print("Nessun utente trovato.")
        return
    for id_utente in id_utenti:
        utente = biblioteca.utenti[id_utente]
        print(
            f"ID {id_utente}: {utente['nome']} {utente['cognome']}, "
            f"nato nel {utente['anno']}"
        )


def presta_libro():
    id_utente = leggi_intero("ID utente: ")
    id_libro = leggi_intero("ID libro: ")
    if id_utente is None or id_libro is None:
        return

    data = input("Data del prestito (AAAA-MM-GG): ").strip()
    try:
        datetime.strptime(data, "%Y-%m-%d")
    except ValueError:
        print("Data non valida: usa il formato AAAA-MM-GG.")
        return

    if biblioteca.presta_libro(id_utente, id_libro, data):
        print("Prestito registrato.")
    else:
        print("Prestito non possibile: controlla gli ID e la disponibilità del libro.")


def restituisci_libro():
    id_utente = leggi_intero("ID utente: ")
    id_libro = leggi_intero("ID libro: ")
    if id_utente is None or id_libro is None:
        return

    data_restituzione = input("Data di restituzione (AAAA-MM-GG): ").strip()
    try:
        datetime.strptime(data_restituzione, "%Y-%m-%d")
    except ValueError:
        print("Data non valida: usa il formato AAAA-MM-GG.")
        return

    chiave_prestito = f"{id_utente}-{id_libro}"
    if chiave_prestito not in biblioteca.prestiti:
        print("Restituzione non possibile: prestito non trovato.")
        return

    data_prestito = biblioteca.prestiti[chiave_prestito]
    if biblioteca.restituisci_libro(id_utente, id_libro):
        print("Restituzione registrata.")
        penale = biblioteca.calcola_penale(data_prestito, data_restituzione)
        if penale:
            print(f"Penale: {penale} euro.")
        else:
            print("Nessuna penale.")
    else:
        print("Restituzione non possibile: prestito non trovato.")


def lista_libri():
    if not biblioteca.libri:
        print("Non ci sono libri in biblioteca.")
        return
    for id_libro, libro in biblioteca.libri.items():
        stato = "in prestito" if libro["prestato"] else "disponibile"
        print(f"ID {id_libro}: {libro['titolo']} - {libro['autore']} ({stato})")


def lista_utenti():
    if not biblioteca.utenti:
        print("Non ci sono utenti registrati.")
        return
    for id_utente, utente in biblioteca.utenti.items():
        print(
            f"ID {id_utente}: {utente['nome']} {utente['cognome']}, "
            f"nato nel {utente['anno']}"
        )


def main():
    while True:
        stampa_menu()
        scelta = input("Scegli un'opzione: ").strip()

        if scelta == "1":
            aggiungi_libro()
        elif scelta == "2":
            aggiungi_utente()
        elif scelta == "3":
            cerca_libro()
        elif scelta == "4":
            cerca_utente()
        elif scelta == "5":
            presta_libro()
        elif scelta == "6":
            restituisci_libro()
        elif scelta == "7":
            lista_libri()
        elif scelta == "8":
            lista_utenti()
        elif scelta == "9":
            print("Arrivederci.")
            break
        else:
            print("Scelta non valida. Inserisci un numero da 1 a 9.")


if __name__ == "__main__":
    main()
