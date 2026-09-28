

def leggi_file(nome_file):
    '''
    Questa funzione legge un file fatto in questo modo:
    Ci sono dei gruppi di liste. Ogni lista ha una riga con scritto
    Nome, :, e il nome del gruppo che contiene la lista
    e una riga con scritto Valori, :, e una lista di numeri separati da virgola
    Esempio:
    Nome:A
    Valori:1,2,3,4
    Nome:A
    Valori:5,6,7,8
    Nome:B
    Valori:1,2,3
    Ci possono essere linee vuote da non considerare
    La funzione deve restituire un dizionario che associa il nome 
    del gruppo a una lista di liste di numeri.
    '''
    dizionario = {}
    with open(nome_file, 'r') as file:
        nome = None
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith('Nome:'):
                nome = line.split(':')[1].strip()
                if nome not in dizionario:
                    dizionario[nome] = []
            elif line.startswith('Valori:') and nome is not None:
                valori_str = line.split(':')[1].strip()
                valori = [int(x) for x in valori_str.split(',') if x.isdigit()]
                dizionario[nome].append(valori)
    return dizionario

def palindromo(lista):
    '''
    Questa funzione riceve una lista di numeri e restituisce True se la lista
    è palindroma, cioè se si legge uguale da sinistra a destra e da destra a sinistra
    Esempi:
    palindromo([1,2,3,2,1]) -> True
    palindromo([1,2,3,4,5]) -> False
    palindromo([]) -> True
    palindromo([1]) -> True
    '''
    return lista == lista[::-1]

def trova_vettori_palindromi(dizionario):
    '''
    Questa funzione riceve un dizionario come quello restituito da leggi_file
    per ogni vettore presente, indipendentemente dal gruppo di appartenenza
    stampa se il vettore è palindromo o no
    '''
    for nome, liste in dizionario.items():
        for lst in liste:
            if palindromo(lst):
                print(f"Il vettore {lst} è palindromo.")
            else:
                print(f"Il vettore {lst} non è palindromo.")


def stampa_gruppi_con_vettori_pari(dizionario):
    '''
    Questa funzione riceve un dizionario come quello restituito da leggi_file
    e stampa i nomi dei gruppi che contengono almeno un vettore con tutti i numeri pari
    '''
    for nome, liste in dizionario.items():
        for lst in liste:
            if all([x % 2 == 0 for x in lst]):
                print(f"Il gruppo {nome} contiene il vettore con tutti i numeri pari: {lst}")
                break


dizionario = leggi_file('data/esame_old.txt')
print(dizionario)
print('1. Vettori palindromi')
trova_vettori_palindromi(dizionario)
print('2. Gruppi con vettori tutti pari')
stampa_gruppi_con_vettori_pari(dizionario)