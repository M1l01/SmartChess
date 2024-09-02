from tkinter import *
import tkinter as tk
from tkinter import Canvas
from tkinter.ttk import *
from PIL import Image, ImageDraw, ImageFont, ImageTk

"""
Paleta de Colores de la aplicación
fondo: #dad9b5
blanco: #ffffff
cafe: #332000
cafe tablero: #4C330C
negro: #000000
"""

class SmartChess:
    #Inicialización de la ventana principal
    def __init__(self, wdInicio, dirFont):
        self.wdInicio = wdInicio
        self.dirFont = dirFont
        #Inicializacion de la Ventana de Inicio
        self.wdInicio.title("Smart Chess")
        self.wdInicio.geometry("1920x1080")
        self.wdInicio.config(bg="#dad9b5")

        self.create_widgets()

    #Creacion de widgets
    def create_widgets(self):
        #Label background Título
        self.lblbgTitle = tk.Label(self.wdInicio, text="", bg="#332000")
        self.lblbgTitle.place(x=0, y=0, width=1920, height=100)

        # Título nueva fuente       
        image = Image.new("RGB", (400,85), color="#332000")
        customFont = ImageFont.truetype(self.dirFont, 48)
        draw = ImageDraw.Draw(image)
        draw.text((30,1), "Smart Chess", font=customFont, fill="#ffffff")
        self.photo = ImageTk.PhotoImage(image)
        self.lblTitle = tk.Label(self.wdInicio, image=self.photo)
        self.lblTitle.place(x=750, y=5)

        # Label Tablero
        self.lblTablero = tk.Label(self.wdInicio, text="", bg="#4C330C")
        self.lblTablero.place(x=460, y=110, width=880, height=880)

        #Cuadricula
        self.cuadricula = Canvas(self.wdInicio, width=800, height=800, highlightthickness=0)
        self.cuadricula.place(x=500, y=150)
        dimCasilla = 100
        for f in range(0,8):
            for c in range(0,8):
                color = "#ffffff" if ((c%2==0) and (f%2==0)) or ((c%2!=0) and (f%2!=0)) else "#000000"
                self.cuadricula.create_rectangle(c*dimCasilla, f*dimCasilla,c*dimCasilla+100, f*dimCasilla+100, fill=color, outline=color)

        #Labels para identificacion de coords
        #LETRAS
        self.lblLetters = tk.Label(self.wdInicio, text="A\t         B\t\t  C\t           D\t\t     E\t             F\t\t     G\t\tH",
                                   bg="#4C330C", fg="#ffffff", font=("Calisto MT", 12, "bold"))
        self.lblLetters.place(x=540, y=960)
        #NÚMEROS
        self.lblNumeros = Canvas(self.wdInicio, width=40, height=800, highlightthickness=0)
        self.lblNumeros.place(x=460, y=150)
        contador = 8
        for fila in range(0,8):
            self.lblNumeros.create_rectangle(0, fila*100, 40, fila*100+100, fill="#4C330C", outline="#4C330C")
            self.lblNumeros.create_text(20, fila*100+50, text=str(contador), fill="#ffffff", font=("Calisto MT", 14, "bold"))
            contador -= 1

if __name__ == "__main__":
    ventana = tk.Tk()
    FontDirectory = "D://MILO//PORTAFOLIO_PROYECTOS//SmartChess//customFont//KOMIKAX_.ttf"
    smartChess = SmartChess(ventana, FontDirectory)
    ventana.mainloop()