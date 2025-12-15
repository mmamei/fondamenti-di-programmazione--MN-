import studente

s = studente.studente("Mario", 20)
studente.aggiungi_voto(s, 28)
studente.aggiungi_voto(s, 30)
media = studente.calcola_media_voti(s)
print(f"La media dei voti di {s['nome']} è {media}")
