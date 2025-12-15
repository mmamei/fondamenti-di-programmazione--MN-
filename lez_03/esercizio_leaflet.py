import json
from modulo_leaflet import *

def main():
    template = leggi_template('lez_3/leaflet/leaflet.template')
    #locations = genera_quadrato()
    dati = leggi_dati_json('lez_3/leaflet/data.json')
    locations = place_visit(dati)
    placemarks = genera_placemarks(locations)
    mappa = sostituisci_placemarks(template, placemarks)
    salva_mappa('lez_3/leaflet/output.html', mappa)


main()
