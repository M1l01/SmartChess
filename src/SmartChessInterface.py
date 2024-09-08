from tkinter import *
import tkinter as tk
from tkinter import Canvas, PhotoImage
from tkinter.ttk import *
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont, ImageTk
from common.utils import ImgLabel, Coords
from animations import Animations
import json

"""
Paleta de Colores de la aplicación
fondo: #dad9b5

tablero: #100803
Azul Oscuro: #030428
Casilla Azul: #0d4a6a 
Casilla Gris: #9e9fa2
"""

class SmartChess:
#    """ Inicialización de la ventana principal """
    def __init__(self, screen, MatrixDetectionChess):
        #Inicializacion de la Ventana de Inicio
        self.screen = screen
        self.screen.title("Smart Chess")
        #self.screen.overrideredirect(True)
        self.screen.geometry("1920x1080")
        self.screen.config(bg="#5c5c5c")

        self.cache = {}

        self.MatrixDetectionChess = MatrixDetectionChess
        self.MatrizComprobacionInicio = [
            #A B C D E F G H
            [1,1,1,1,1,1,1,1], #8
            [1,1,1,1,1,1,1,1], #7
            [0,0,0,0,0,0,0,0], #6
            [0,0,0,0,0,0,0,0], #5
            [0,0,0,0,0,0,0,0], #4
            [0,0,0,0,0,0,0,0], #3
            [1,1,1,1,1,1,1,1], #2
            [1,1,1,1,1,1,1,1]  #1
        ]

        self.isWhitetime = True # Control de Turno
        self.isMoveComplete = False

        #       """Importar Datos de las Piezas"""
        self.piezas = self.cargar_datos_piezas()

        #       """Variables Globales"""
        # Menu Inicio
        self.lblMenu = tk.Label(self.screen)
        self.lblLogo = tk.Label(self.screen)
        self.lblJuegaAjedrez = tk.Label(self.screen)
        self.btnJuegoPresencial = tk.Button(self.screen)
        self.btnJuegoVirtual = tk.Button(self.screen)

        # Registro de Partida
        self.cuadroInterno = tk.Label(self.screen)
        self.lblLineaVertical = tk.Label(self.screen)
        self.lblLineaHorizontal = tk.Label(self.screen)
        self.lblTitleRegistro = tk.Label(self.screen)
        self.lblTeamWhite = tk.Label(self.screen)
        self.lblTeamBlack = tk.Label(self.screen)

        # Tablero
        self.cuadricula = Canvas()

        #   """Create Widgets"""
        self.crear_widgets()

    def cargar_datos_piezas(self):
        try:
            with open('..//SmartChess//src//piezas.json', 'r') as archivo:
                piezas = json.load(archivo)
            return piezas
        except FileNotFoundError:
            return {"Pieza": []}

    def crear_widgets(self):
        self.Title()                    # Title
        self.Tablero()                  # Tablero
        self.menu_juega_ajedrez()       # Menú de Opciones de Juego

    def Title(self):
        #Label background Título
        self.lblbgTitle = tk.Label(self.screen, text="", bg="#030428")
        self.lblbgTitle.place(x=0, y=0, width=1920, height=100)

        # Título nueva fuente       
        image = Image.new("RGB", (400,85), color="#030428")
        dirFont = "..//SmartChess//customFont//KOMIKAX_.ttf"
        customFont = ImageFont.truetype(dirFont, 48)
        draw = ImageDraw.Draw(image)
        draw.text((30,1), "Smart Chess", font=customFont, fill="#ffffff")
        self.photo = ImageTk.PhotoImage(image)
        lblTitle = tk.Label(self.screen, image=self.photo)
        lblTitle.place(x=750, y=5)
    
    def Tablero(self):
        lblTablero = tk.Label(self.screen, text="", bg="#100803")
        lblTablero.place(x=260, y=110, width=880, height=880)

        #Cuadricula
        self.cuadricula = Canvas(self.screen, width=800, height=800, highlightthickness=2)
        self.cuadricula.place(x=300, y=150)
        dimCasilla = 100
        for f in range(0,8):
            for c in range(0,8):
                color = "#9e9fa2" if ((c%2==0) and (f%2==0)) or ((c%2!=0) and (f%2!=0)) else "#0d4a6a"
                self.cuadricula.create_rectangle(c*dimCasilla, f*dimCasilla,c*dimCasilla+100,
                                                 f*dimCasilla+100, fill=color, outline=color)
    
        #Labels para identificacion de coords
        self.Letras_cuadricula()
        self.Numeros_cuadricula()
        
    def Letras_cuadricula(self):
        #Letras
        lblLetters = tk.Label(self.screen,
                              text="A\t   B\t      C\t         D\t\t E\t    F\t       G\t         H",
                              bg="#100803", fg="#ffffff", font=("Comic Sans MS", 12, "bold"))
        lblLetters.place(x=340, y=960)

    def Numeros_cuadricula(self):
        #Números
        lblNumeros = Canvas(self.screen, width=40, height=800, highlightthickness=0)
        lblNumeros.place(x=260, y=150)
        contador = 8
        for fila in range(0,8):
            lblNumeros.create_rectangle(0, fila*100, 40, fila*100+100, fill="#100803", outline="#100803")
            lblNumeros.create_text(20, fila*100+50, text=str(contador), fill="#ffffff",
                                        font=("Comic Sans MS", 14, "bold"))
            contador -= 1

    def menu_juega_ajedrez(self):

        self.lblMenu.config(text="", bg="#232427")
        self.lblMenu.place(x=1200, y=110, width=650, height=880)

        logoImg = ImgLabel("..//SmartChess//src//images//logo.png", (250,250)).pngLabel((35,36,39,255))
        self.lblLogo.config(image=logoImg, bg="#232427", bd=0)
        self.lblLogo.image=logoImg
        self.lblLogo.place(x=1400, y=270)

        self.lblJuegaAjedrez.config(text="Juega al Ajedrez", bg="#232427",
                                        fg="#ffffff", font=("Comic Sans MS", 48, "bold"))
        self.lblJuegaAjedrez.place(x=1260, y=180)
        
        # Botones
        self.btnJuegoPresencial.config(text="Juego en Tablero",command=self.Juego_Presencial, activebackground="#030428", activeforeground="#767676",
                                       bg="#030428", fg="white", cursor="hand2", font=("Comic Sans MS", 26, "bold"), bd=0)
        self.btnJuegoPresencial.place(x=1325, y=750, width=400, height=90)

        self.btnJuegoVirtual.config(text="Juego Virtual", command=self.Inicio_Juego_Virtual, bg="#030428", fg="white", activebackground="#030428", activeforeground="#767676",
                                         cursor="hand2", font=("Comic Sans MS", 26, "bold"), bd=0)
        self.btnJuegoVirtual.place(x=1325, y=550, width=400, height=90)

    def Intruccion_colocar_Piezas(self, screen):
        lblInfoTxt = tk.Label(screen, text="Coloque las piezas\npara iniciar la partida", bg="#232427",
                                fg="#ffffff", font=("Comic Sans MS", 20, "bold"))
        lblInfoTxt.place(x=20, y=20, width=350, height=80)

        InfoImg = ImgLabel("..//SmartChess//src//images//tablero.jpg",(300,300)).jpgLabel()
        lblInfoImg = tk.Label(screen, image=InfoImg, background="#ff0000")
        lblInfoImg.image = InfoImg
        lblInfoImg.place(x=50, y=125)

    def lbl_Pieza(self, dirImg, coord):
        try:
            coordenadas = Coords()
            pos = coordenadas.optencion_coordenadas(coord)
            [bgcolor, bgcolorrgba] = ["#dad9b5", (158, 159, 162, 255)] if (((pos[0] + pos[1] - 60)/100)%2 == 0) else ["#0d4a6a", (13, 74, 106, 255)]
            cache_key = (dirImg, (90,90), bgcolorrgba) #Uso de cache para mejorar el rendimiento del programa
            if cache_key not in self.cache:
                try:
                    image = Image.open(dirImg)
                    imageResized = image.resize((90,90))
                    fondo = Image.new("RGBA", imageResized.size, bgcolorrgba)
                    imageResized = imageResized.convert("RGBA")
                    imageComposed = Image.alpha_composite(fondo, imageResized)
                    imageRGB = imageComposed.convert("RGB")
                    imageTK = ImageTk.PhotoImage(imageRGB)
                    self.cache[cache_key] = imageTK

                except Exception as e:
                    print(f"Error al cargar la imagen: {e}")
                    return None
            
            lblPieza = tk.Label(self.screen, image=self.cache[cache_key], bg=bgcolor, bd=0)
            lblPieza.image = self.cache[cache_key]
            lblPieza.place(x=pos[0], y=pos[1])

            return lblPieza
        
        except Exception as e:
            print(f"Error: {e}")
        
        return None
    
    def colocar_Piezas_Inicio(self):
        listaPiezas = []
        for _, pieza in self.piezas.items():
            lblpieza = self.lbl_Pieza(pieza["directorio"], pieza["coordenada"])
            listaPiezas.append((lblpieza, pieza))
            # print((lblpieza, pieza))
        return listaPiezas
    
    def animacion_inicio_juego(self):
        #       """Configuración de Screen 3"""
        screen3 = Toplevel(self.screen)
        screen3.overrideredirect(True)
        screen3.geometry("450x250")
        screen3.config(bg="#232427")

        #Label Inicio de Partida
        lblInicioPartida = tk.Label(screen3, text="Inicio\nde\nPartida", bg="#030428", fg="#ffffff",
                                    font=("Comic Sans MS", 40, "bold"))
        lblInicioPartida.place(x=10, y=10, width=430, height=230)
        
        #Animaciones
        animacionScreen3 = Animations(screen3)
        animacionScreen3.desvanecimiento_horizontal(posInicialX=383,posY=456,geometryX=450,geometryY=250,posFinalX=783,step=0.02)
    
    def Interface_Registro_Partida(self):
        self.lblMenu.config(bg="#100803")

        self.cuadroInterno.config(text="", bg="#0d4a6a")
        self.cuadroInterno.place(x=1220, y=130, width=610, height=840)

        self.lblLineaHorizontal = tk.Label(self.screen, text="", bg="white")
        self.lblLineaHorizontal.place(x=1280, y=300, width=500, height=3)

        self.lblLineaVertical = tk.Label(self.screen, text="", bg="white")
        self.lblLineaVertical.place(x=1529, y=240, width=3, height=700)

        self.lblTitleRegistro.config(text="REGISTRO DE MOVIMIENTOS", bg="#0d4a6a", fg="#ffffff",
                                     font=("Comic Sans MS", 24, "bold"))
        self.lblTitleRegistro.place(x=1280, y=145)

        self.lblTeamWhite.config(text="Team White", bg="#0d4a6a", fg="#ffffff",
                                 font=("Comic Sans MS", 18, "bold"))
        self.lblTeamWhite.place(x=1320, y=250)

        self.lblTeamBlack.config(text="Team Black", bg="#0d4a6a", fg="#ffffff",
                                 font=("Comic Sans MS", 18, "bold"))
        self.lblTeamBlack.place(x=1580, y=250)
    
    #                               """Juego Presencial"""  
    def Juego_Presencial(self):
        #Crear ventana de Info
        screen2 = Toplevel(self.screen)
        screen2.title("Ajuste Parámetros")
        screen2.geometry("400x480+500+300")
        screen2.config(bg="#232427")

        if(self.MatrixDetectionChess == self.MatrizComprobacionInicio):
            self.colocar_Piezas_Inicio()    #Colocamos las piezas en posición Inicial
            screen2.destroy()   #Cerramos ventana de Info

            #Ventana de Inicio de Juego
            self.Inicio_Juego_Presencial()
        else:
            self.Intruccion_colocar_Piezas(screen2)

    def Inicio_Juego_Presencial(self):
        self.animacion_inicio_juego()

    #                               """Juego Virtual"""
    def Inicio_Juego_Virtual(self):
        piezas = self.colocar_Piezas_Inicio()
        
        #Detrucción de Menu de Inicio
        self.lblLogo.destroy()
        self.lblJuegaAjedrez.destroy()
        self.btnJuegoPresencial.destroy()
        self.btnJuegoVirtual.destroy()

        # Registro de Partida
        self.Interface_Registro_Partida()

        iteradorPiezas = 0
        self.deteccion_entrada_piezas(piezas, iteradorPiezas)
        
        # Animación de Inicio de Juego
        self.animacion_inicio_juego()
    
    def Entrada_Pieza(self, event):
        event.widget.config(cursor="hand2")

    def deteccion_entrada_piezas(self, piezas, idx):
        tipo = piezas[idx][1]["tipo"]
        coordenada = piezas[idx][1]["coordenada"]
        team = piezas[idx][1]["team"]
        estado = piezas[idx][1]["estado"]

        piezas[idx][0].bind("<Enter>", lambda event: self.Entrada_Pieza(event))
        piezas[idx][0].bind("<Button-1>", lambda event: self.movimiento_piezas(event, tipo, coordenada, team, estado))
        
        idx += 1
        
        if(self.isWhitetime):
            print("Turno Blancas")
            for i in range(16,32):
                piezas[i][0].unbind("<Button-1>")

            if (idx > len(piezas)/2 - 1):
                idx = 0
        else:
            print("Turno Negras")
            for j in range(0, 16):
                piezas[j][0].unbind("<Button-1>")

            if(idx > len(piezas) - 1):
                idx = int(len(piezas)/2)
        
        self.screen.after(50, self.deteccion_entrada_piezas, piezas, idx)
        
    def movimiento_piezas(self, event, tipo, coordenada, team, estado):
        #               """Movimiento de las Piezas"""
        match tipo:
            case "peon":              
                print("Es un peon")
            case "torre":
                print("Es una torre")
            case "caballo":
                print("Es un caballo")
            case "alfil":
                print("Es un alfil")
            case "dama":
                print("Es una dama")
            case "rey":
                print("Es un rey")
            case _:
                print("No es una pieza")

if __name__ == "__main__":
    screen = tk.Tk()
    #Matriz de Deteccion en inicio de Partida
    MatrizDetection = [
        #A B C D E F G H
        [1,1,1,1,1,1,1,1], #8
        [1,1,1,1,1,1,1,1], #7
        [0,0,0,0,0,0,0,0], #6
        [0,0,0,0,0,0,0,0], #5
        [0,0,0,0,0,0,0,0], #4
        [0,0,0,0,0,0,0,0], #3
        [1,1,1,1,1,1,1,1], #2
        [1,1,1,1,1,1,1,1]  #1
    ]
    smartChess = SmartChess(screen, MatrizDetection)
    screen.mainloop()