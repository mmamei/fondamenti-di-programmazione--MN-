# app_monolitica.py
# ATTENZIONE: questo file è volutamente caotico per scopi didattici!

import csv, json, os, re, sys, time, random



LAST_IMPORT = None
CSV_SEP = ";"             # hardcoded

from ui.cli import debug, info, error
from infra.repository import carica_dati, salva_dati
from domain.services import RUBRICA, aggiungi_contatto, cerca, lista
from domain.validators import valida_nome, valida_telefono, valida_email, TELEFONO_RE, EMAIL_RE    


def importa_csv(path):
    global LAST_IMPORT
    debug(f"Importo CSV da {path}")
    if not os.path.exists(path):
        error("CSV non trovato")
        return 0
    cnt = 0
    try:
        with open(path, newline="", encoding="utf-8") as f:
            reader = csv.reader(f, delimiter=CSV_SEP)
            for row in reader:
                # duplicazione della validazione...
                try:
                    nome = row[0].strip()
                    tel = row[1].strip()
                    email = row[2].strip() if len(row) > 2 else None
                    if not nome:
                        continue
                    if not TELEFONO_RE.match(tel):
                        continue
                    if email and not EMAIL_RE.match(email):
                        continue
                    if nome in RUBRICA:  # sovrascrive senza warning coerente
                        info(f"Sovrascrivo contatto esistente: {nome}")
                    RUBRICA[nome] = {"telefono": tel, "email": email, "tags": []}
                    cnt += 1
                except:
                    pass  # silenzio tomba
    except Exception as e:
        error(f"Errore durante import: {e}")
    LAST_IMPORT = time.time()
    info(f"Importati {cnt} contatti")
    return cnt

def esporta_csv(path):
    try:
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.writer(f, delimiter=CSV_SEP)
            for nome, d in RUBRICA.items():
                w.writerow([nome, d.get("telefono",""), d.get("email","")])
        info(f"Esportati {len(RUBRICA)} contatti su {path}")
    except Exception as e:
        error(f"Export fallito: {e}")

def rimuovi(nome):
    try:
        del RUBRICA[nome]
        return True
    except KeyError:
        error("Contatto non trovato (forse mai esistito)")
        return False

def aggiungi_tag(nome, tag):
    if nome in RUBRICA:
        RUBRICA[nome].setdefault("tags", [])
        if tag not in RUBRICA[nome]["tags"]:
            RUBRICA[nome]["tags"].append(tag)
        else:
            info("Tag già presente (forse)")
    else:
        error("Nome non esistente, impossibile aggiungere tag")

def prompt():
    print("Comandi: load [file], save [file], add <nome> <tel> [email], list [tag], find <nome>, del <nome>, tag <nome> <tag>, import <csv>, export <csv>, quit")
    while True:
        try:
            r = input("> ").strip()
        except EOFError:
            break
        if not r:
            continue
        parts = r.split()
        cmd = parts[0].lower()
        if cmd == "load":
            carica_dati(parts[1] if len(parts)>1 else None)
        elif cmd == "save":
            salva_dati(parts[1] if len(parts)>1 else None)
        elif cmd == "add":
            if len(parts) < 3:
                error("Uso: add <nome> <tel> [email]")
            else:
                nome = parts[1]
                tel = parts[2]
                email = parts[3] if len(parts)>3 else None
                ok = aggiungi_contatto(nome, tel, email=email)
                if ok: info("Aggiunto")
        elif cmd == "list":
            tag = parts[1] if len(parts)>1 else None
            for n, d in lista(tag=tag):
                print(f"- {n}: {d.get('telefono')}  <{d.get('email')}>  tags={','.join(d.get('tags',[]))}")
        elif cmd == "find":
            if len(parts)<2:
                error("Uso: find <nome-parziale>")
            else:
                res = cerca(parts[1])
                print(res if res else "Non trovato")
        elif cmd == "del":
            if len(parts)<2:
                error("Uso: del <nome>")
            else:
                if rimuovi(parts[1]):
                    info("Rimosso")
        elif cmd == "tag":
            if len(parts)<3:
                error("Uso: tag <nome> <tag>")
            else:
                aggiungi_tag(parts[1], parts[2])
        elif cmd == "import":
            if len(parts)<2:
                error("Uso: import <file.csv>")
            else:
                importa_csv(parts[1])
        elif cmd == "export":
            esporta_csv(parts[1] if len(parts)>1 else "rubrica_export.csv")
        elif cmd == "quit":
            break
        else:
            error("Comando sconosciuto. (Forse)")
    print("Ciao!")

def _demo_seed():
    # funzione “nascosta” che scrive nello stato globale
    for n, t, e in [
        ("Alice", "12345", "alice@example.com"),
        ("Bob", "+39 333 555-777", None),
        ("AL", "not-a-phone", "bad"),
    ]:
        try:
            aggiungi_contatto(n, t, e)
        except:
            pass

if __name__ == "__main__":
    carica_dati()     # carica da DEFAULT_FILE senza chiederlo
    _demo_seed()      # side-effect inatteso
    if len(sys.argv) > 1 and sys.argv[1] == "--batch-add":
        # modalità batch opaca e non documentata
        for i in range(2, len(sys.argv), 3):
            try:
                aggiungi_contatto(sys.argv[i], sys.argv[i+1], sys.argv[i+2])
            except:
                pass
        salva_dati()
    else:
        prompt()
        salva_dati()
