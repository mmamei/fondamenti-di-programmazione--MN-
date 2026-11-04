import re

EMAIL_RE = re.compile(r".+@.+\..+")
TEL_RE = re.compile(r"^\+?\d[\d\s\-]{4,}$")

def valida_nome(nome: str) -> bool:
    """
    >>> valida_nome("Alice")
    True
    >>> valida_nome("   ")
    False
    """
    return isinstance(nome, str) and nome.strip() != ""

def valida_telefono(tel: str) -> bool:
    """
    >>> valida_telefono("+39 333-555-777")
    True
    >>> valida_telefono("abc")
    False
    """
    return bool(TEL_RE.match(str(tel)))

def valida_email(email: str | None) -> bool:
    """
    >>> valida_email(None)
    True
    >>> valida_email("alice@example.com")
    True
    >>> valida_email("bad@")
    False
    """
    return True if email is None else bool(EMAIL_RE.match(str(email)))

import doctest
doctest.testmod(verbose=True)