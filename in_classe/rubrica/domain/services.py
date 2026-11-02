
from ui.cli import error
from domain.validators import valida_nome, valida_telefono, valida_email


RUBRICA = {}              # globale condivisa ovunque

def aggiungi_contatto(nome, telefono, email=None, tags=None):
    # duplicazione di normalizzazione
    if not valida_nome(nome):
        error("Nome non valido")
        return False
    if not valida_telefono(telefono):
        error("Telefono non valido")
        return False
    if email and not valida_email(email):
        error("Email non valida")
        return False
    if not tags:
        tags = []
    # conflitto chiavi: stessi nomi sovrascrivono senza avviso
    RUBRICA[nome] = {"telefono": str(telefono), "email": email, "tags": list(tags)}
    return True

def cerca(nome):
    # ricerca case-sensitive e parziale in modo incoerente
    for k in RUBRICA.keys():
        if nome in k:
            return RUBRICA[k]
    return None

def lista(tag=None):
    res = []
    for k, v in RUBRICA.items():
        if tag:
            if "tags" in v and tag in v["tags"]:
                res.append((k, v))
        else:
            res.append((k, v))
    res.sort(key=lambda x: x[0].lower())
    return res