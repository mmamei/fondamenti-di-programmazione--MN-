import json
from pathlib import Path


def stringa_js(testo):
    testo_json = json.dumps(testo, ensure_ascii=True)
    return "'" + testo_json[1:-1].replace("'", "\\'") + "'"


file_json = Path(__file__).with_name("data.json")

with file_json.open(encoding="utf-8") as file:
    dati = json.load(file)

luoghi_visitati = []

for elemento in dati["timelineObjects"]:
    if "placeVisit" in elemento:
        luogo = elemento["placeVisit"]["location"]
        luoghi_visitati.append(
            {
                "latitudine": luogo["latitudeE7"] / 10**7,
                "longitudine": luogo["longitudeE7"] / 10**7,
                "nome": luogo["name"],
            }
        )

codice_marker = "\n".join(
    "new maplibregl.Marker().setLngLat"
    f"([{luogo['longitudine']}, {luogo['latitudine']}])"
    ".setPopup(new maplibregl.Popup().setText"
    f"({stringa_js(luogo['nome'])})).addTo(map);"
    for luogo in luoghi_visitati
)

cartella = Path(__file__).parent
file_template = cartella / "leaflet.tmpl"
file_output = cartella / "output.html"

template = file_template.read_text(encoding="utf-8")
segnaposto = "{{PLACEMARKS}}"

if template.count(segnaposto) != 1:
    raise ValueError(f"Il template deve contenere un solo segnaposto {segnaposto}")

file_output.write_text(
    template.replace(segnaposto, codice_marker),
    encoding="utf-8",
)