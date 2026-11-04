import json

def load(path="rubrica.json"):
    try:
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
        norm = {}
        for nome, d in data.items():
            norm[nome] = {
                "telefono": d.get("telefono", ""),
                "email": d.get("email"),
                "tags": list(d.get("tags", [])),
            }
        return norm
    except FileNotFoundError:
        return {}

def save(rubrica, path="rubrica.json"):
    with open(path, "w", encoding="utf-8") as f:
        json.dump(rubrica, f, ensure_ascii=False, indent=2)
