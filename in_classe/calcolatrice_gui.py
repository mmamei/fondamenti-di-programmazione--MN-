from guizero import App, Text, PushButton, TextBox
from calcolatrice import calcola

def f():
    x = int(n1.value)
    y = int(n2.value)
    z = op.value
    output.value = calcola(x,y,z)

app = App(title="Calcolatrice")

Text(app, text="Numero 1")
n1 = TextBox(app)
Text(app, text="Numero 2")
n2 = TextBox(app)
Text(app, text="Operazione")
op = TextBox(app)
PushButton(app, text = 'Esegui', command=f)
output = Text(app, text="Risultato")

app.display()
