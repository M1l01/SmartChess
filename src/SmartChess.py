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
        self.wdInicio.config(bg="#dad9b5")

        #Create Widgets
        self.LabelTitle()           #Label Title
        self.LabelTablero()         #Label Tablero
        self.MenuSmartChess()       #Label Menu
        self.ColocarImgs()          #Colocar Imgs

    def LabelTitle(self):
        #Label background Título
        self.lblbgTitle = tk.Label(self.wdInicio, text="", bg="#251700")
        self.lblbgTitle.place(x=0, y=0, width=1920, height=100)

        # Título nueva fuente       
        image = Image.new("RGB", (400,85), color="#251700")
        customFont = ImageFont.truetype(self.dirFont, 48)
        draw = ImageDraw.Draw(image)
        draw.text((30,1), "Smart Chess", font=customFont, fill="#ffffff")
        self.photo = ImageTk.PhotoImage(image)
        self.lblTitle = tk.Label(self.wdInicio, image=self.photo)
        self.lblTitle.place(x=750, y=5)
    
    def LabelTablero(self):
        self.lblTablero = tk.Label(self.wdInicio, text="", bg="#332000")
        self.lblTablero.place(x=260, y=110, width=880, height=880)

        #Cuadricula
        self.cuadricula = Canvas(self.wdInicio, width=800, height=800, highlightthickness=2)
        self.cuadricula.place(x=300, y=150)
        dimCasilla = 100
        for f in range(0,8):
            for c in range(0,8):
                color = "#ecd9a6" if ((c%2==0) and (f%2==0)) or ((c%2!=0) and (f%2!=0)) else "#332000"
                self.cuadricula.create_rectangle(c*dimCasilla, f*dimCasilla,c*dimCasilla+100,
                                                 f*dimCasilla+100, fill=color, outline=color)

        #Labels para identificacion de coords
        #LETRAS
        self.lblLetters = tk.Label(self.wdInicio,
                                   text="A\t    B\t        C\t            D\t\tE\t     F\t        G\t            H",
                                   bg="#332000", fg="#ffffff", font=("Calisto MT", 14, "bold"))
        self.lblLetters.place(x=340, y=960)
        #NÚMEROS
        self.lblNumeros = Canvas(self.wdInicio, width=40, height=800, highlightthickness=0)
        self.lblNumeros.place(x=260, y=150)
        contador = 8
        for fila in range(0,8):
            self.lblNumeros.create_rectangle(0, fila*100, 40, fila*100+100, fill="#332000", outline="#332000")
            self.lblNumeros.create_text(20, fila*100+50, text=str(contador), fill="#ffffff",
                                        font=("Calisto MT", 14, "bold"))
            contador -= 1

    def MenuSmartChess(self):
        #Label Pestañas
        lblpest = tk.Label(self.wdInicio, text="", bg="#251700")
        lblpest.place(x=1200, y=110, width=650, height=880)

    def ColocarImgs(self):
        #Accion de Click sobre dama Blanca
        def on_label_click(event):
            print("Se presionó sobre la dama Blanca", event.x, event.y)
            print(type(event))

        #Imagenes
        damaWhite = Image.open("..//SmartChess//src//images//dama_blanca.png")
        damaWhite = damaWhite.resize((90,90))
        fondo_blanco = Image.new("RGBA", damaWhite.size, (218, 217, 181, 255))
        damaWhite = damaWhite.convert("RGBA")
        damaWhite = Image.alpha_composite(fondo_blanco, damaWhite)
        damaWhite = damaWhite.convert("RGB")
        damaWhite = ImageTk.PhotoImage(damaWhite)
        lblDamaWhite = tk.Label(self.wdInicio, image=damaWhite, bg="#dad9b5")
        lblDamaWhite.image = damaWhite
        lblDamaWhite.place(x=20, y=110)
        lblDamaWhite.bind("<Button-1>", on_label_click)


        
if __name__ == "__main__":
    ventana = tk.Tk()
    FontDirectory = "D://MILO//PORTAFOLIO_PROYECTOS//SmartChess//customFont//KOMIKAX_.ttf"
    smartChess = SmartChess(ventana, FontDirectory)
    ventana.mainloop()