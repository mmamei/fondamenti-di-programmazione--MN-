from . import validators as V

# Lo "stato" è semplicemente un dict: { nome: {"telefono":..., "email":..., "tags":[...]} }

def aggiungi(rubrica, nome, tel, email=None, tags=()):
    """
    Ritorna una nuova rubrica aggiornata (immutability-friendly).
    >>> r = {}
    >>> r2 = aggiungi(r, "Alice", "12345", "a@b.com", tags=["amici"])
    >>> "Alice" in r2 and "Alice" not in r
    True
    """
    if not V.valida_nome(nome): 
        raise ValueError("Nome non valido")
    if not V.valida_telefono(tel): 
        raise ValueError("Telefono non valido")
    if not V.valida_email(email):
        raise ValueError("Email non valida")

    nuovo = dict(rubrica)
    nuovo[nome] = {"telefono": str(tel), "email": email, "tags": list(tags)}
    return nuovo

def cerca_primo(rubrica, query):
    """
    Ricerca case-insensitive del primo match.
    >>> r = {"Alice": {"telefono":"1","email":None,"tags":[]}, "Bob": {"telefono":"2","email":None,"tags":[]}}
    >>> cerca_primo(r, "ali")["telefono"]
    '1'
    >>> cerca_primo(r, "x") is None
    True
    """
    q = query.lower()
    for nome, c in rubrica.items():
        if q in nome.lower():
            return c
    return None

def cerca_tutti(rubrica, query):
    """
    Restituisce una lista di (nome, contatto) ordinata.
    >>> r = {"Alice": {"telefono":"1","email":None,"tags":[]}, "Alina":{"telefono":"3","email":None,"tags":[]}, "Bob":{"telefono":"2","email":None,"tags":[]}}
    >>> [n for n,_ in cerca_tutti(r, "ali")]
    ['Alice', 'Alina']
    """
    q = query.lower()
    trovati = [(n, c) for n, c in rubrica.items() if q in n.lower()]
    return sorted(trovati, key=lambda x: x[0].lower())

def lista(rubrica, tag=None):
    """
    >>> r = {"Alice":{"telefono":"1","email":None,"tags":["amici"]}, "Bob":{"telefono":"2","email":None,"tags":[]}}
    >>> [n for n,_ in lista(r)]
    ['Alice', 'Bob']
    >>> [n for n,_ in lista(r, tag="amici")]
    ['Alice']
    """
    items = list(rubrica.items())
    if tag:
        items = [(n, c) for n, c in items if tag in c.get("tags", [])]
    return sorted(items, key=lambda x: x[0].lower())

def rimuovi(rubrica, nome):
    """
    >>> r = {"Alice":{"telefono":"1","email":None,"tags":[]}}
    >>> r2 = rimuovi(r, "Alice")
    >>> "Alice" in r, "Alice" in r2
    (True, False)
    """
    nuovo = dict(rubrica)
    nuovo.pop(nome, None)
    return nuovo

def aggiungi_tag(rubrica, nome, tag):
    """
    >>> r = {"Alice":{"telefono":"1","email":None,"tags":[]}}
    >>> r2 = aggiungi_tag(r, "Alice", "amici")
    >>> r2["Alice"]["tags"]
    ['amici']
    """
    if nome not in rubrica:
        raise KeyError("Contatto inesistente")
    nuovo = dict(rubrica)
    c = dict(nuovo[nome])  # copia shallow
    tags = list(c.get("tags", []))
    if tag not in tags:
        tags.append(tag)
    c["tags"] = tags
    nuovo[nome] = c
    return nuovo


import doctest
doctest.testmod(verbose=True)