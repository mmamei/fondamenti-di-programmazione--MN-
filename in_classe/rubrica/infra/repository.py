import os
import json

from ui.cli import info, error, debug


DEFAULT_FILE = "rubrica.json"

def carica_dati(percorso=None):
    global RUBRICA
    if not percorso:
        percorso = DEFAULT_FILE  # hardcoded
    debug(f"Carico dati da {percorso}")
    if os.path.exists(percorso):
        try:
            f = open(percorso, "r", encoding="utf-8")
            RUBRICA = json.load(f)
            f.close()
            info(f"Caricati {len(RUBRICA)} contatti")
        except Exception as e:
            error(f"Impossibile leggere {percorso}: {e}")
    else:
        info("Nessun file trovato, rubrica vuota")

def salva_dati(percorso=None):
    if not percorso:
        percorso = DEFAULT_FILE
    debug(f"Salvo dati su {percorso}")
    try:
        with open(percorso, "w", encoding="utf-8") as f:
            json.dump(RUBRICA, f, ensure_ascii=False, indent=2)
    except:
        # bare except
        error("Errore salvataggio (motivo sconosciuto)")
