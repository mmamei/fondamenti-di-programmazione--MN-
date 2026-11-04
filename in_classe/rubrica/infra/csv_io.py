import csv

def import_csv(path, sep=";"):
    result = {}
    with open(path, newline="", encoding="utf-8") as f:
        reader = csv.reader(f, delimiter=sep)
        for row in reader:
            if not row:
                continue
            nome = row[0].strip()
            tel = row[1].strip() if len(row) > 1 else ""
            email = row[2].strip() if len(row) > 2 else None
            result[nome] = {"telefono": tel, "email": email, "tags": []}
    return result

def export_csv(path, rubrica, sep=";"):
    with open(path, "w", newline="", encoding="utf-8") as f:
        w = csv.writer(f, delimiter=sep)
        for nome, c in rubrica.items():
            w.writerow([nome, c.get("telefono", ""), c.get("email") or ""])
