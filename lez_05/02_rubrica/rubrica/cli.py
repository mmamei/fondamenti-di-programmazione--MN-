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