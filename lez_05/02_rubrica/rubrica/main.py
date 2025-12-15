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