from infra import repository, csv_io
from domain import services as S

def run_cli(repo_path="rubrica.json"):
    rubrica = repository.load(repo_path)
    print(f"Contatti caricati: {len(rubrica)}")
    print("Comandi: load, save, add <nome> <tel> [email], list [tag], find <nome>, findall <nome>, del <nome>, tag <nome> <tag>, import <csv>, export <csv>, quit")

    while True:
        try:
            parts = input("> ").strip().split()
        except EOFError:
            print()
            break
        if not parts:
            continue
        cmd = parts[0].lower()

        try:
            if cmd == "load":
                rubrica = repository.load(repo_path)
                print("Dati ricaricati.")
            elif cmd == "save":
                repository.save(rubrica, repo_path)
                print("Dati salvati.")
            elif cmd == "add":
                if len(parts) < 3:
                    print("Uso: add <nome> <tel> [email]")
                    continue
                nome, tel = parts[1], parts[2]
                email = parts[3] if len(parts) > 3 else None
                rubrica = S.aggiungi(rubrica, nome, tel, email=email)
                print("Aggiunto.")
            elif cmd == "list":
                tag = parts[1] if len(parts) > 1 else None
                for n, c in S.lista(rubrica, tag=tag):
                    print(f"- {n}: {c.get('telefono')} <{c.get('email') or ''}> tags={','.join(c.get('tags', []))}")
            elif cmd == "find":
                q = parts[1] if len(parts) > 1 else ""
                c = S.cerca_primo(rubrica, q)
                print(c if c else "Non trovato")
            elif cmd == "findall":
                q = parts[1] if len(parts) > 1 else ""
                res = S.cerca_tutti(rubrica, q)
                for n, c in res:
                    print(f"- {n}: {c.get('telefono')}")
                if not res:
                    print("Nessun risultato")
            elif cmd == "del":
                if len(parts) < 2:
                    print("Uso: del <nome>")
                    continue
                rubrica = S.rimuovi(rubrica, parts[1])
                print("OK")
            elif cmd == "tag":
                if len(parts) < 3:
                    print("Uso: tag <nome> <tag>")
                    continue
                rubrica = S.aggiungi_tag(rubrica, parts[1], parts[2])
                print("Tag aggiunto.")
            elif cmd == "import":
                if len(parts) < 2:
                    print("Uso: import <file.csv>")
                    continue
                dati = csv_io.import_csv(parts[1])
                for n, c in dati.items():
                    rubrica = S.aggiungi(rubrica, n, c["telefono"], c["email"])
                print(f"Importati {len(dati)} contatti.")
            elif cmd == "export":
                if len(parts) < 2:
                    print("Uso: export <file.csv>")
                    continue
                csv_io.export_csv(parts[1], rubrica)
                print("Esportazione completata.")
            elif cmd == "quit":
                break
            else:
                print("Comando sconosciuto.")
        except Exception as e:
            print("[ERRORE]", e)
