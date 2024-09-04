from tkinter import *
import tkinter as tk
from tkinter import Canvas, PhotoImage
from tkinter.ttk import *
from tkinter import ttk
from PIL import Image, ImageDraw, ImageFont, ImageTk
from common.utils import ImgLabel
from animations import Animations

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

        #Create Widgets
        self.crear_widgets()

    def crear_widgets(self):
        self.Title()                    # Title
        self.Tablero()                  # Tablero
        self.menu_juega_ajedrez()       # Menú de Opciones de Juego
        self.colocar_Piezas_Inicio()    #Colocamos las piezas en posición Inicial

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
        cuadricula = Canvas(self.screen, width=800, height=800, highlightthickness=2)
        cuadricula.place(x=300, y=150)
        dimCasilla = 100
        for f in range(0,8):
            for c in range(0,8):
                color = "#9e9fa2" if ((c%2==0) and (f%2==0)) or ((c%2!=0) and (f%2!=0)) else "#0d4a6a"
                cuadricula.create_rectangle(c*dimCasilla, f*dimCasilla,c*dimCasilla+100,
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

        lblPest = tk.Label(self.screen, text="", bg="#232427")
        lblPest.place(x=1200, y=110, width=650, height=880)

        logoImg = ImgLabel("..//SmartChess//src//images//logo.png", (250,250)).pngLabel((35,36,39,255))
        lblLogo = tk.Label(self.screen, image=logoImg, bg="#232427", bd=0)
        lblLogo.image=logoImg
        lblLogo.place(x=1400, y=270)

        lblJuegaAjedrez = tk.Label(self.screen, text="Juega al Ajedrez", bg="#232427",
                                        fg="#ffffff", font=("Comic Sans MS", 48, "bold"))
        lblJuegaAjedrez.place(x=1260, y=180)
        
        #Botones

        btnJuegoPresencial = tk.Button(self.screen, text="Juego Presencial",command=self.Juego_Presencial,
                                       bg="#030428", fg="white", cursor="hand2", font=("Comic Sans MS", 26, "bold"), bd=0)
        btnJuegoPresencial.place(x=1325, y=750, width=400, height=90)

        btnJuegoVirtual = tk.Button(self.screen, text="Juego Virtual", bg="#030428", fg="white",
                                         cursor="hand2", font=("Comic Sans MS", 26, "bold"), bd=0)
        btnJuegoVirtual.place(x=1325, y=550, width=400, height=90)

    #                               """Juego Presencial"""  
    def Juego_Presencial(self):
        #Crear ventana de Info
        screen2 = Toplevel(self.screen)
        screen2.title("Ajuste Parámetros")
        screen2.geometry("400x480")
        screen2.config(bg="#232427")

        if(self.MatrixDetectionChess == self.MatrizComprobacionInicio):
            screen2.destroy()   #Cerramos ventana de Info

            #Ventana de Inicio de Juego
            self.Inicio_Juego()

        else:
            self.Intruccion_colocar_Piezas(screen2)

    def Inicio_Juego(self):
        screen3 = Toplevel(self.screen)
        screen3.overrideredirect(True)
        screen3.geometry("450x250+483+456")
        screen3.config(bg="#232427")

        #Label Inicio de Partida
        lblInicioPartida = tk.Label(screen3, text="Inicio\nde\nPartida", bg="#36383d", fg="#ffffff",
                                    font=("Comic Sans MS", 40, "bold"))
        lblInicioPartida.place(x=10, y=10, width=430, height=230)

        #desvanecimiento
        Animations(screen3).desvanecimiento()
    
    def Intruccion_colocar_Piezas(self, screen):
        lblInfoTxt = tk.Label(screen, text="Coloque las piezas\npara iniciar la partida", bg="#232427",
                                fg="#ffffff", font=("Comic Sans MS", 20, "bold"))
        lblInfoTxt.place(x=20, y=20, width=350, height=80)

        InfoImg = ImgLabel("..//SmartChess//src//images//tablero.jpg",(300,300)).jpgLabel()
        lblInfoImg = tk.Label(screen, image=InfoImg, background="#ff0000")
        lblInfoImg.image = InfoImg
        lblInfoImg.place(x=50, y=125)

    def lbl_Pieza(self, dirImg, newsize, pos, funcEnterMouse):
        try:
            [bgcolor, bgcolorrgba] = ["#dad9b5", (158, 159, 162, 255)] if (((pos[0] + pos[1] - 60)/100)%2 == 0) else ["#0d4a6a", (13, 74, 106, 255)]
            cache_key = (dirImg, newsize, bgcolorrgba) #Uso de cache para mejorar el rendimiento del programa
            if cache_key not in self.cache:
                try:
                    image = Image.open(dirImg)
                    imageResized = image.resize(newsize)
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
            lblPieza.bind("<Enter>", funcEnterMouse)

            return lblPieza
        
        except Exception as e:
            print(f"Error: {e}")
        
        return None
    
    def colocar_Piezas_Inicio(self):
        #Accion de Click sobre dama Blanca
        def on_enter_mouse(event):
            event.widget.config(cursor="hand2")

        self.lbl_Pieza("..//SmartChess//src//images//torre_blanca.png", (90,90), (305, 855), on_enter_mouse)                    # TorreWhiteA
        self.lbl_Pieza("..//SmartChess//src//images//caballo_blanco.png", (90,90), (405, 855), on_enter_mouse)                  # CaballoWhiteB
        self.lbl_Pieza("..//SmartChess//src//images//alfil_blanco.png", (90,90), (505, 855), on_enter_mouse)                    # AlfilWhiteB 
        self.lbl_Pieza("..//SmartChess//src//images//dama_blanca.png", (90,90), (605, 855), on_enter_mouse)                     # DamaWhite
        self.lbl_Pieza("..//SmartChess//src//images//rey_blanco.png", (90,90), (705, 855), on_enter_mouse)                      # ReyWhite
        self.lbl_Pieza("..//SmartChess//src//images//alfil_blanco.png", (90,90), (805, 855), on_enter_mouse)                    # AlfilWhiteW
        self.lbl_Pieza("..//SmartChess//src//images//caballo_blanco.png", (90,90), (905, 855), on_enter_mouse)                  # CaballoWhiteG
        self.lbl_Pieza("..//SmartChess//src//images//torre_blanca.png", (90,90), (1005, 855), on_enter_mouse)                   # TorreWhiteH
        
        self.lbl_Pieza("..//SmartChess//src//images//torre_negra.png", (90,90), (305, 155), on_enter_mouse)                     # TorreBlackA
        self.lbl_Pieza("..//SmartChess//src//images//caballo_negro.png", (90,90), (405, 155), on_enter_mouse)                   # CaballoBlackB
        self.lbl_Pieza("..//SmartChess//src//images//alfil_negro.png", (90,90), (505, 155), on_enter_mouse)                     # AlfilBlackB
        self.lbl_Pieza("..//SmartChess//src//images//dama_negra.png", (90,90), (605, 155), on_enter_mouse)                      # DamaBlack
        self.lbl_Pieza("..//SmartChess//src//images//rey_negro.png", (90,90), (705, 155), on_enter_mouse)                       # ReyBlack
        self.lbl_Pieza("..//SmartChess//src//images//alfil_negro.png", (90,90), (805, 155), on_enter_mouse)                     # AlfilBlackW
        self.lbl_Pieza("..//SmartChess//src//images//caballo_negro.png", (90,90), (905, 155), on_enter_mouse)                   # CaballoBlackG
        self.lbl_Pieza("..//SmartChess//src//images//torre_negra.png", (90,90), (1005, 155), on_enter_mouse)                    # TorreBlackH
        
        for piece in range(0,8):
            self.lbl_Pieza("..//SmartChess//src//images//peon_blanco.png", (90,90), ((piece*100)+305, 755), on_enter_mouse)       
            self.lbl_Pieza("..//SmartChess//src//images//peon_negro.png", (90,90), ((piece*100)+305, 255), on_enter_mouse)

        
if __name__ == "__main__":
    screen = tk.Tk()
    #Matriz de Deteccion en inicio de Partida
    MatrizDetection = [
        #A B C D E F G H
        [0,1,1,1,1,1,1,1], #8
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