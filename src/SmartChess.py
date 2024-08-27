from tkinter import *
import tkinter as tk
from tkinter import font, ttk, Canvas
from tkinter.ttk import *
from PIL import Image, ImageDraw, ImageFont, ImageTk

"""
Paleta de Colores de la aplicación
fondo: #5c82cf
blanco: #ffffff
cafe claro: #332000
cafe oscuro: #964d22
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

customfont = ImageFont.truetype("D://MILO//PORTAFOLIO_PROYECTOS//SmartChess//customFont//KOMIKAX_.ttf", 48)
draw = ImageDraw.Draw(image)
draw.text((30,1), "Smart Chess", font=customfont, fill="#332000")
#image_cropped = image.crop((100,20,400,80))
photo = ImageTk.PhotoImage(image)

lblTitle = tk.Label(wdInicio, image=photo)
lblTitle.place(x=750, y=5)

# *Label Tablero
lblTablero = tk.Label(wdInicio, text="", bg="#4C330C")
lblTablero.place(x=580, y=130, width=840, height=840)

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

wdInicio.mainloop()