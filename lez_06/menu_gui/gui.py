from gestione_studenti import inserisci_studente, aggiungi_voto

def main():
    '''
    Crea un'intefrfaccia grafica con guizero.
    C'è un titolo con scritto "Studenti"
    Nella riga successiva c'è un campo di testo
    per inserie il nome dello studenrte
    e a fianco un pulsante "Inserisci Studente"
    Sotto c'è un grande campo di testo per mostrare i risultati
    '''
    from guizero import App, Text, PushButton, TextBox

    def inserisci_studente_gui():
        nome = nome_input.value
        r = inserisci_studente(classe, nome)
        risultati.value += r + "\n"
    
    def inserisci_voto_gui():
        nome = nome_input.value
        voto = voto_input.value
        r = aggiungi_voto(classe, nome, voto)
        risultati.value += r + "\n"

    app = App(title="Studenti", layout="grid")
    titolo = Text(app, text="Studenti", size=20, grid=[0,0,2,1])
    
    nome_input = TextBox(app, width=30, grid=[0,1])
    inserisci_button = PushButton(app, text="Inserisci Studente", command=inserisci_studente_gui, grid=[1,1])
    
    voto_input = TextBox(app, width=30, grid=[0,2])
    inserisci_button = PushButton(app, text="Inserisci Voto", command=inserisci_voto_gui, grid=[1,2])


    
    risultati = TextBox(app, width=50, height=15, multiline=True, grid=[0,3,2,1])
    

    app.display()

classe = {}
main()