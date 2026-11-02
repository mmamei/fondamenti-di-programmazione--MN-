'''
I libri vengono memorizzati da un dizionario che ha come chiave un ID del libro
e come valori un secondo dizionario che contiene le chiavi: titolo, autore e una variabile booleana che dice se il libro è prestato in questo momento

Gli utenti della biblioteca sono in un dizionario con chiave ID dell'utente e come valori un dizionario con nome, cognome e anno di nascita

I prestiti sono memorizzati in un dizionario con chiave IdUtente-IdLibro e come valori
la data del prestito (come stringa)
'''

libri = {}
utenti = {}
prestiti = {}

def resetta_biblioteca():
    global libri, utenti, prestiti
    libri = {}
    utenti = {}
    prestiti = {}

def aggiungi_libro(titolo, autore):
    '''
    Aggiunge un libro al dizionario dei libri.
    Crea un ID progressivo univoco per il libro
    Titolo e autore sono passati come parametri
    Inizialmente il libro non è in prestito.
    Restituisce l'id del libro creato.
    '''
    id_libro = len(libri) + 1
    libri[id_libro] = {"titolo": titolo, "autore": autore, "prestato": False}
    return id_libro


def aggiungi_utente(nome, cognome, anno):
    '''
    Aggiunge un utente al dizionario degli utenti.
    Crea un ID progressivo univoco per l'utente
    Salva le informazioni nel dizionario
    Restituisce l'ID dell'utente creato
    '''
    id_utente = len(utenti) + 1
    utenti[id_utente] = {"nome": nome, "cognome": cognome, "anno": anno}
    return id_utente


def cerca_libro(titolo):
    '''
    Cerca i libri con titoli uguali a quello passato e restituisce una lista degli id dei titolo corrispondenti
    '''
    return [id for id, info in libri.items() if info["titolo"] == titolo]   

def cerca_utente(nome, cognome):
    '''
    Cerca gli utenti con nome e cognome e ritorna la lista degli id degli utenti con quel nome e cognome
    '''
    return [id for id, info in utenti.items() if info["nome"] == nome and info["cognome"] == cognome]




import doctest
doctest.testmod(verbose=False)

resetta_biblioteca()

id = aggiungi_utente("Marco","Mamei",1976)
print(utenti)
print(utenti[id]['cognome'])

id1 = aggiungi_libro("La Divina Commedia", "Dante Alighieri")
id2 = aggiungi_libro("La Divina Commedia", "Dante Alighieri")
id3 = aggiungi_libro("La Coscienza di Zeno", "Italo Svevo")
print(libri)
x = cerca_libro("La Divina Commedia")
print(x == [id1, id2])
