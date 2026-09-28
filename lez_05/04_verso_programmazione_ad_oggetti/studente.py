
def crea_studente(nome, eta):
    return {"nome": nome, "eta": eta, "voti": []}

def aggiungi_voto(studente, voto): 
    studente["voti"].append(voto)

def calcola_media_voti(studente):
    if not studente["voti"]:
        return 0
    return sum(studente["voti"]) / len(studente["voti"])

'''
NOTA. Quando farete la programmazione ad oggetti, il parametri studente che compare in tutte le funzioni
sarà chiamato self per convenzione. 
In qesto modo quando leggo il codice delle funzioni 
self["voti"].append(voto)
suona come :
ai "miei" voti, aggiungi questo voto
mettendosi "nei panni" di quello specifico studente.
'''


