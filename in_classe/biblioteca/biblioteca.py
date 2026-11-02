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


def presta_libro(id_utente, id_libro, data):
    '''
    Registra il prestito di un libro da parte di un utente.
    Controlla che l'utente e il libro esistano e che il libro non sia già prestato.
    Se tutto è corretto, registra il prestito nel dizionario dei prestiti e aggiorna lo stato del libro a prestato.
    Restituisce True se il prestito è stato registrato con successo, False altrimenti.
    '''
    if id_utente not in utenti:
        return False
    if id_libro not in libri:
        return False
    if libri[id_libro]["prestato"]:
        return False
    prestiti[f"{id_utente}-{id_libro}"] = data
    libri[id_libro]["prestato"] = True
    return True

def calcola_penale(data_prestito, data_restituzione):
    '''
    Calcola la penale per un prestito in base alla data di prestito e alla data di restituzione.
    La penale è di 1 euro al giorno per ogni giorno oltre i 30 giorni dal prestito.
    Restituisce l'importo della penale.
    '''
    from datetime import datetime
    formato_data = "%Y-%m-%d"
    data_prestito_dt = datetime.strptime(data_prestito, formato_data)
    data_restituzione_dt = datetime.strptime(data_restituzione, formato_data)
    giorni_trascorsi = (data_restituzione_dt - data_prestito_dt).days
    penale = max(0, giorni_trascorsi - 30)  # 1 euro al giorno oltre i 30 giorni
    return penale   

def restituisci_libro(id_utente, id_libro):
    '''
    Registra la restituzione di un libro da parte di un utente.
    Controlla che il prestito esista.
    Se tutto è corretto, rimuove il prestito dal dizionario dei prestiti e aggiorna lo stato del libro a non prestato.
    Restituisce True se la restituzione è stata registrata con successo, False altrimenti.
    '''
    key = f"{id_utente}-{id_libro}"
    if key not in prestiti:
        return False
    del prestiti[key]
    libri[id_libro]["prestato"] = False
    return True


if __name__ == "__main__":

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
