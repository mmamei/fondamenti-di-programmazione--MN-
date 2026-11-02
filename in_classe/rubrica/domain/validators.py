
import re

EMAIL_RE = re.compile(r".+@.+\..+")
TELEFONO_RE = re.compile(r"^\+?\d[\d\s\-]{4,}$")


def valida_nome(nome):
    # validazione debole e duplicata altrove…
    return isinstance(nome, str) and len(nome.strip()) > 0

def valida_telefono(tel):
    m = TELEFONO_RE.match(str(tel))
    return bool(m)

def valida_email(email):
    # regex permissiva, duplicata in importa_csv
    return bool(EMAIL_RE.match(str(email)))
