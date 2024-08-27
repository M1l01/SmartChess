from tkinter import *
import tkinter as tk
from tkinter import font, ttk, Canvas
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
#---------------------------------------Declaramos la ventana----------------------------
wdInicio = tk.Tk() 
wdInicio.title("Smart Chess")
wdInicio.geometry("1920x1080")
wdInicio.config(bg="#dad9b5")

# Label background Titulo
lblbgTitle = tk.Label(wdInicio, text="", bg="#332000")
lblbgTitle.place(x=0, y=0, width=1920, height=100)

# *Titulo Label
#Configuracion de nueva fuente
image = Image.new('RGB', (400,85), color="#ffffff")
dirFont = "D://MILO//PORTAFOLIO_PROYECTOS//SmartChess//customFont//KOMIKAX_.ttf"
customfont = ImageFont.truetype(dirFont, 48)
draw = ImageDraw.Draw(image)
draw.text((30,1), "Smart Chess", font=customfont, fill="#332000")
#image_cropped = image.crop((100,20,400,80))
photo = ImageTk.PhotoImage(image)

lblTitle = tk.Label(wdInicio, image=photo)
lblTitle.place(x=750, y=5)

# *Label Tablero
lblTablero = tk.Label(wdInicio, text="", bg="#4C330C")
lblTablero.place(x=560, y=110, width=880, height=880)

canvas = Canvas(wdInicio, width=800, height=800)
canvas.place(x=600, y=150)

dimCasilla = 100
flagColor = True
for f in range(0,8):
    for c in range(0,8):
        if ((c%2==0) and (f%2==0)) or ((c%2!=0) and (f%2!=0)):
            canvas.create_rectangle(c*dimCasilla, f*dimCasilla, c*dimCasilla+100, f*dimCasilla+100, fill="#ffffff")
        else:
            canvas.create_rectangle(c*dimCasilla, f*dimCasilla, c*dimCasilla+100, f*dimCasilla+100, fill="#000000")

# *Labels para identificación de coords 
lblA = tk.Label(wdInicio, text="A", bg="#4C330C", fg="#ffffff",
                font=("Calisto MT", 12, "bold"))
lblA.place(x=640, y=960)
lblB = tk.Label(wdInicio, text="B", bg="#4C330C", fg="#ffffff",
                font=("Calisto MT", 12, "bold"))
lblB.place(x=740, y=960)
lblC = tk.Label(wdInicio, text="C", bg="#4C330C", fg="#ffffff",
                font=("Calisto MT", 12, "bold"))
lblC.place(x=840, y=960)
lblD = tk.Label(wdInicio, text="D", bg="#4C330C", fg="#ffffff",
                font=("Calisto MT", 12, "bold"))
lblD.place(x=940, y=960)
lblE = tk.Label(wdInicio, text="E", bg="#4C330C", fg="#ffffff",
                font=("Calisto MT", 12, "bold"))
lblE.place(x=1040, y=960)
lblF = tk.Label(wdInicio, text="F", bg="#4C330C", fg="#ffffff",
                font=("Calisto MT", 12, "bold"))
lblF.place(x=1140, y=960)
lblG = tk.Label(wdInicio, text="G", bg="#4C330C", fg="#ffffff",
                font=("Calisto MT", 12, "bold"))
lblG.place(x=1240, y=960)
lblH = tk.Label(wdInicio, text="H", bg="#4C330C", fg="#ffffff",
                font=("Calisto MT", 12, "bold"))
lblH.place(x=1340, y=960)

lbl8 = tk.Label(wdInicio, text="8", bg="#4C330C", fg="#ffffff",
                font=("Calisto MT", 14, "bold"))
lbl8.place(x=575, y=185)
lbl7 = tk.Label(wdInicio, text="7", bg="#4C330C", fg="#ffffff",
                font=("Calisto MT", 14, "bold"))
lbl7.place(x=575, y=285)
lbl6 = tk.Label(wdInicio, text="6", bg="#4C330C", fg="#ffffff",
                font=("Calisto MT", 14, "bold"))
lbl6.place(x=575, y=385)
lbl5 = tk.Label(wdInicio, text="5", bg="#4C330C", fg="#ffffff",
                font=("Calisto MT", 14, "bold"))
lbl5.place(x=575, y=485)
lbl4 = tk.Label(wdInicio, text="4", bg="#4C330C", fg="#ffffff",
                font=("Calisto MT", 14, "bold"))
lbl4.place(x=575, y=585)
lbl3 = tk.Label(wdInicio, text="3", bg="#4C330C", fg="#ffffff",
                font=("Calisto MT", 14, "bold"))
lbl3.place(x=575, y=685)
lbl2 = tk.Label(wdInicio, text="2", bg="#4C330C", fg="#ffffff",
                font=("Calisto MT", 14, "bold"))
lbl2.place(x=575, y=785)
lbl1 = tk.Label(wdInicio, text="1", bg="#4C330C", fg="#ffffff",
                font=("Calisto MT", 14, "bold"))
lbl1.place(x=575, y=885)

wdInicio.mainloop()