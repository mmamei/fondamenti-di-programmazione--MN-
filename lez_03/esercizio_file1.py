
def leggi_file(file_path):
    '''
    legge il file passato come parametro.
    Il file ha questo formato:
    Marco,30
    Matteo,28
    Marco,23
    Roberta,29
    Voglio creare un dizionario che associa i nomi ai voti.
    Attenzione che il nomi si possono ripetere su più linee
    '''
    dizionario = {}
    with open(file_path, 'r') as file:
        for line in file:
            nome, voto = line.strip().split(',')
            voto = int(voto)
            if nome in dizionario:
                dizionario[nome].append(voto)
            else:
                dizionario[nome] = [voto]
    return dizionario

def stampa_media(dizionario):
    for nome, voti in dizionario.items():
        media = sum(voti) / len(voti)
        print(f'{nome}: {media:.2f}')

dizionario = leggi_file('data/test1.txt')
stampa_media(dizionario)