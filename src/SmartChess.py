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
image = Image.new('RGB', (400,85), color="#332000")
dirFont = "D://MILO//PORTAFOLIO_PROYECTOS//SmartChess//customFont//KOMIKAX_.ttf"
customfont = ImageFont.truetype(dirFont, 48)
draw = ImageDraw.Draw(image)
draw.text((30,1), "Smart Chess", font=customfont, fill="#ffffff")
#image_cropped = image.crop((100,20,400,80))
photo = ImageTk.PhotoImage(image)

lblTitle = tk.Label(wdInicio, image=photo)
lblTitle.place(x=750, y=5)

# *Label Tablero
lblTablero = tk.Label(wdInicio, text="", bg="#4C330C")
lblTablero.place(x=560, y=110, width=880, height=880)

canvas = Canvas(wdInicio, width=800, height=800, highlightthickness=0)
canvas.place(x=600, y=150)

dimCasilla = 100
for f in range(0,8):
    for c in range(0,8):
        if ((c%2==0) and (f%2==0)) or ((c%2!=0) and (f%2!=0)):
            canvas.create_rectangle(c*dimCasilla, f*dimCasilla, c*dimCasilla+100, f*dimCasilla+100, fill="#ffffff", outline="#ffffff")
        else:
            canvas.create_rectangle(c*dimCasilla, f*dimCasilla, c*dimCasilla+100, f*dimCasilla+100, fill="#000000", outline="#000000")

# *Labels para identificación de coords
# LETRAS
lblLetters = tk.Label(wdInicio, text="A\t         B\t\t  C\t           D\t\t     E\t             F\t\t     G\t\tH",
                bg="#4C330C", fg="#ffffff", font=("Calisto MT", 12, "bold"))
lblLetters.place(x=640, y=960)
# NUMEROS
lblNumeros = Canvas(wdInicio, width=40, height=800, highlightthickness=0)
lblNumeros.place(x=560, y=150)
contador = 8
for fila in range(0, 8):
    lblNumeros.create_rectangle(0, fila*100, 40, fila*100+100, fill="#4C330C", outline="#4C330C")
    lblNumeros.create_text(20, fila*100+50, text=str(contador), fill="#ffffff", font=("Calisto MT", 14, "bold"))
    contador -= 1

wdInicio.mainloop()