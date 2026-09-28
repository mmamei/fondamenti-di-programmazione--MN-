
biblioteca = []
utenti = []
prestiti = []

def aggiungi_libro(titolo, autore):
    '''
    La funzione riceve il titolo e l'autore di un libro e lo aggiunge alla biblioteca.
    La biblioteca è realizzata come una lista di dizionari.
    Ogni dizionario contiene: id, titolo e autore, in prestito (booleano).
    L'id è assegnato automaticamente.
    in_presito è messo a False
    '''
    libro = {
        'id': len(biblioteca) + 1,
        'titolo': titolo,
        'autore': autore,
        'in_prestito': False
    }
    biblioteca.append(libro)

def aggiungi_utente(nome):
    '''
    La funzione riceve il nome di un utente e lo aggiunge agli utenti della biblioteca.
    Gli utenti sono realizzati come una lista di dizionari.
    Ogni dizionario contiene: id, nome.
    L'id è assegnato automaticamente.
    '''
    utente = {
        'id': len(utenti) + 1,
        'nome': nome
    }
    utenti.append(utente)

def cerca_utente(nome):
    '''
    La funzione riceve il nome di un utente e restituisce la lista degli id
    degli utenti con quel nome.
    '''
    return [utente['id'] for utente in utenti if utente['nome'] == nome]

def cerca_libro(titolo):
    '''
    La funzione riceve il titolo di un libro e restituisce la lista degli id
    dei libri con quel titolo.
    '''
    return [libro['id'] for libro in biblioteca if libro['titolo'] == titolo]

def aggiungi_prestito(id_utente, id_libro, data_prestito):
    '''
    La funzione riceve l'id di un utente e l'id di un libro e registra
    un prestito se il libro non è già in prestito.
    Restituisce True se il prestito è stato registrato, False altrimenti.
    '''
    for libro in biblioteca:
        if libro['id'] == id_libro:
            if not libro['in_prestito']:
                libro['in_prestito'] = True
                prestito = {
                    'id_utente': id_utente,
                    'id_libro': id_libro,
                    'data_prestito': data_prestito
                }
                prestiti.append(prestito)
                return True
            else:
                return False
    return False

def presta_libro(id_user, titolo_libro, data):
    '''
    La funzione riceve l'id di un utente, il titolo di un libro e la data del prestito.
    Registra un prestito se il libro non è già in prestito.
    Restituisce True se il prestito è stato registrato, False altrimenti.
    '''
    libri_trovati = cerca_libro(titolo_libro)
    for id_libro in libri_trovati:
        if aggiungi_prestito(id_user, id_libro, data):
            return True
    return False


def cerca_prestito(id_user, id_libro):
    '''
    La funzione riceve l'id di un utente e l'id di un libro e restituisce
    il dizionario del prestito se esiste, None altrimenti.
    '''
    for prestito in prestiti:
        if prestito['id_utente'] == id_user and prestito['id_libro'] == id_libro:
            return prestito
    return None


def lista_libri_disponibili():
    '''
    restituisce la lista dei titoli dei libri non in prestito.
    '''
    return [libro['titolo'] for libro in biblioteca if not libro['in_prestito']]


def calcola_penale(data_prestito, data_restituzione):
    '''
    La funzione riceve la data del prestito e la data di restituzione.
    Calcola la penale in base ai giorni di ritardo.
    Restituisce la penale (0 se non c'è ritardo).
    '''
    from datetime import datetime, timedelta

    formato_data = "%Y-%m-%d"
    data_prestito_dt = datetime.strptime(data_prestito, formato_data)
    data_restituzione_dt = datetime.strptime(data_restituzione, formato_data)

    giorni_permitted = 30
    data_scadenza = data_prestito_dt + timedelta(days=giorni_permitted)

    if data_restituzione_dt > data_scadenza:
        giorni_ritardo = (data_restituzione_dt - data_scadenza).days
        penale = giorni_ritardo * 0.50  # 0.50 euro al giorno di ritardo
        return penale
    else:
        return 0.0

def restituisci_libro(id_user, id_libro, data_restituzione):
    '''
    La funzione riceve l'id di un utente e l'id di un libro e la data di restituzione.
    Controlla se effettivamente l'utente ha in prestito quel libro.
    Se sì, aggiorna lo stato del libro a non in prestito e rimuove il prestito.
    Restituisce le date del prestito e della restituzione se il libro è stato restituito, False altrimenti.
    '''
    prestito = cerca_prestito(id_user, id_libro)
    if prestito:
        for libro in biblioteca:
            if libro['id'] == id_libro:
                libro['in_prestito'] = False
                date = (prestito['data_prestito'], data_restituzione)
                prestiti.remove(prestito)
                return date
    return False


def cerca_libri_in_prestito(id_user, titolo):
    '''
    La funzione riceve l'id di un utente e il titolo di un libro.
    Ritorna la lista degli id dei libri con quel titolo che
    l'utente ha in prestito.
    '''
    libri_in_prestito = []
    for prestito in prestiti:
        if prestito['id_utente'] == id_user:
            for libro in biblioteca:
                if libro['id'] == prestito['id_libro'] and libro['titolo'] == titolo:
                    libri_in_prestito.append(libro['id'])

    return libri_in_prestito
