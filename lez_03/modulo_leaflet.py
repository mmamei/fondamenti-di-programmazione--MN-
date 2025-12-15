def leggi_template(file_path):
    with open(file_path, 'r') as file:
        return file.read()

def sostituisci_placemarks(template, placemarks):
    return template.replace("{{PLACEMARKS}}", placemarks)

def genera_placemarks(locations):
    placemarks = ""
    for loc in locations:
        placemarks += f'L.marker([{loc[0]}, {loc[1]}]).addTo(map).bindPopup("{loc[2]}")\n'
    return placemarks   

def salva_mappa(file_path, mappa):
    with open(file_path, 'w') as file:
        file.write(mappa)

def genera_quadrato(lat = 44.63276, lon = 10.871231, n=10, step=0.01):
    locations = []
    for _ in range(n):
        locations.append((lat, lon, f"Ciao"))
        lat += step
    for _ in range(n):
        locations.append((lat, lon, f"Ciao"))
        lon += step
    for _ in range(n):
        locations.append((lat, lon, f"Ciao"))
        lat -= step
    for _ in range(n):
        locations.append((lat, lon, f"Ciao"))
        lon -= step
    return locations

import json

def leggi_dati_json(file_path):
    with open(file_path, 'r') as f:
        dati = json.load(f)
    return dati

def place_visit(dati):
    '''
    dati è fatto così:
    dati = {
        "timelineObjects": [....]
    }
    nella lista timelineObjects ci sono dizionari.
    Alcuni contengono la chiave "placeVisit".
    Voglio creare una lista prendendo solo i dizionari che contengono "placeVisit".
    La lista deve contenere delle tuple nel formato
    (latitudine, longitudine, nome)

    '''
    return [(obj['placeVisit']['location']['latitudeE7'] / 1E7,
             obj['placeVisit']['location']['longitudeE7'] / 1E7,
             obj['placeVisit']['location']['name'].replace("\"", "") ) for obj in dati['timelineObjects'] if 'placeVisit' in obj]
