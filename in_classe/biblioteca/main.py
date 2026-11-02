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

def aggiungi_libro(titolo, autore):
    '''
    Aggiunge un libro al dizionario dei libri.
    Crea un ID progressivo univoco per il libro
    Titolo e autore sono passati come parametri
    Inizialmente il libro non è in prestito.
    Restituisce l'id del libro creato.

    >>>  id = aggiungi_libro("La Divina Commedia", "Dante Alighieri")
    >>>  libri[id]['titolo']
    La Divina Commedia
    '''
    id_libro = len(libri) + 1
    libri[id_libro] = {"titolo": titolo, "autore": autore, "prestato": False}
    return id_libro
