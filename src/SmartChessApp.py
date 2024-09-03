from cliente_esp32 import ESP32Client
from SmartChessInterface import SmartChess
import tkinter as tk

#Parametros de comunicación con la ESP32
host = "192.168.100.172"
port = 3333
SmartChessClient = ESP32Client(host, port)

PrincipalScreen = tk.Tk()

SmartChessClient.connect()
message = "Hola"
SmartChessClient.send_msg(message)
msgRecibido = SmartChessClient.recibir_msg()
print(msgRecibido)
SmartChessClient.close()

SmartChessApp = SmartChess(PrincipalScreen)

PrincipalScreen.mainloop()


