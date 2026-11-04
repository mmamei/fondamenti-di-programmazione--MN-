from guizero import App, Text, PushButton

def change_message():
    #print('ciao')
    message.value = "You pressed the button!"

app = App(title="Hello world")

message = Text(app, text="Welcome to the Hello world app!")

button = PushButton(app, text="Press me", command=change_message)

app.display()

print("App finished")