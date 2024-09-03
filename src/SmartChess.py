from tkinter import *
import tkinter as tk
from tkinter import Canvas, PhotoImage
from tkinter.ttk import *
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont, ImageTk

"""
Paleta de Colores de la aplicación
fondo: #dad9b5
blanco: #ffffff
cafe oscuro: #251700
cafe tablero: #4C330C
tablero claras: #ecd9a6
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
        self.wdInicio.config(bg="#5c5c5c")

        #Create Widgets
        self.LabelTitle()           #Label Title
        self.LabelTablero()         #Label Tablero
        self.MenuJuegaAjedrez()     #Label Menu
        self.ColocarPiezas()        #Colocar Imgs

    def LabelTitle(self):
        #Label background Título
        self.lblbgTitle = tk.Label(self.wdInicio, text="", bg="#030428")
        self.lblbgTitle.place(x=0, y=0, width=1920, height=100)

        # Título nueva fuente       
        image = Image.new("RGB", (400,85), color="#030428")
        customFont = ImageFont.truetype(self.dirFont, 48)
        draw = ImageDraw.Draw(image)
        draw.text((30,1), "Smart Chess", font=customFont, fill="#ffffff")
        self.photo = ImageTk.PhotoImage(image)
        self.lblTitle = tk.Label(self.wdInicio, image=self.photo)
        self.lblTitle.place(x=750, y=5)
    
    def LabelTablero(self):
        self.lblTablero = tk.Label(self.wdInicio, text="", bg="#100803")
        self.lblTablero.place(x=260, y=110, width=880, height=880)

        #Cuadricula
        self.cuadricula = Canvas(self.wdInicio, width=800, height=800, highlightthickness=2)
        self.cuadricula.place(x=300, y=150)
        dimCasilla = 100
        for f in range(0,8):
            for c in range(0,8):
                color = "#505050" if ((c%2==0) and (f%2==0)) or ((c%2!=0) and (f%2!=0)) else "#030428"
                self.cuadricula.create_rectangle(c*dimCasilla, f*dimCasilla,c*dimCasilla+100,
                                                 f*dimCasilla+100, fill=color, outline=color)

        #Labels para identificacion de coords
        #LETRAS
        self.lblLetters = tk.Label(self.wdInicio,
                                   text="A\t   B\t      C\t         D\t\t E\t    F\t       G\t         H",
                                   bg="#100803", fg="#ffffff", font=("Comic Sans MS", 12, "bold"))
        self.lblLetters.place(x=340, y=960)
        #NÚMEROS
        self.lblNumeros = Canvas(self.wdInicio, width=40, height=800, highlightthickness=0)
        self.lblNumeros.place(x=260, y=150)
        contador = 8
        for fila in range(0,8):
            self.lblNumeros.create_rectangle(0, fila*100, 40, fila*100+100, fill="#100803", outline="#100803")
            self.lblNumeros.create_text(20, fila*100+50, text=str(contador), fill="#ffffff",
                                        font=("Comic Sans MS", 14, "bold"))
            contador -= 1

    def MenuJuegaAjedrez(self):
        self.lblpest = tk.Label(self.wdInicio, text="", bg="#232427")
        self.lblpest.place(x=1200, y=110, width=650, height=880)

        logo = self.pngLabel("..//SmartChess//src//images//logo.png",
                             (35,36,39,255), (250,250))
        self.lblLogo = tk.Label(self.wdInicio, image=logo, bg="#232427", bd=0)
        self.lblLogo.image = logo
        self.lblLogo.place(x=1400, y=270)

        self.lblJuegaAjedrez = tk.Label(self.wdInicio, text="Juega al Ajedrez", bg="#232427",
                                        fg="#ffffff", font=("Comic Sans MS", 48, "bold"))
        self.lblJuegaAjedrez.place(x=1260, y=180)

        self.btnJuegoVirtual = tk.Button(self.wdInicio, text="Juego Virtual", bg="#030428", fg="white",
                                         cursor="hand2", font=("Comic Sans MS", 26, "bold"), bd=0)
        self.btnJuegoVirtual.place(x=1325, y=550, width=400, height=90)

        self.btnJuegoPresencial = tk.Button(self.wdInicio, text="Juego Presencial", bg="#030428", fg="white",
                                            cursor="hand2", font=("Comic Sans MS", 26, "bold"), bd=0)
        self.btnJuegoPresencial.place(x=1325, y=750, width=400, height=90)

    def ColocarPiezas(self):
        #Accion de Click sobre dama Blanca
        def on_label_click(event):
            event.widget.config(cursor="hand2")

        #Imagenes
        damaWhite = self.pngLabel("..//SmartChess//src//images//dama_blanca.png",
                                   (236, 217, 166, 255), (90,90))

        self.lblDamaWhite = tk.Label(self.wdInicio, image=damaWhite, bg="#dad9b5", bd=0)
        self.lblDamaWhite.image = damaWhite
        self.lblDamaWhite.place(x=20, y=110)
        self.lblDamaWhite.bind("<Enter>", on_label_click)
    
    def pngLabel(self, dirImg, colorFondo, newsize):
        image = Image.open(dirImg)
        image = image.resize(newsize)
        fondo = Image.new("RGBA", image.size, colorFondo)
        image = image.convert("RGBA")
        image = Image.alpha_composite(fondo, image)
        image = image.convert("RGB")
        image = ImageTk.PhotoImage(image)
        return image
        
if __name__ == "__main__":
    ventana = tk.Tk()
    FontDirectory = "D://MILO//PORTAFOLIO_PROYECTOS//SmartChess//customFont//KOMIKAX_.ttf"
    smartChess = SmartChess(ventana, FontDirectory)
    ventana.mainloop()