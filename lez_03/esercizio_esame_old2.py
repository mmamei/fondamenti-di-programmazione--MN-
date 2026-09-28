def leggi_file(nome_file):
    '''
    Questa funzione legge un file che contiene delle matrici.
    Ogni matrice è racchiusa tra due parentesi graffe {}
    Le righe della matrice sono racchiuse tra parentesi graffe {}
    e i numeri sono separati da virgola.
    Esempio:
    {{1,2,3},{4,5,6},{7,8,9}}
    {{1},{2},{3}}
    {{1,2,3}}
    la funzione ritorna una lista di matrici (liste di liste di interi)
    '''
    liste_di_liste = []
    with open(nome_file, 'r') as file:
        for line in file:
            line = line.strip()
            if not line:
                continue
            if line.startswith('{') and line.endswith('}'):
                line = line[1:-1].strip()  # rimuove le parentesi esterne
                righe = line.split('},{')
                matrice = []
                for riga in righe:
                    riga = riga.strip('{} ')
                    if riga:  # evita righe vuote
                        numeri = [int(x) for x in riga.split(',') if x.isdigit()]
                        matrice.append(numeri)
                liste_di_liste.append(matrice)
    return liste_di_liste   

lista_matrici = leggi_file('data/esame_old2.txt')
for m in lista_matrici:
    print(m)