import tkinter as tk
from tkinter import PhotoImage

# Crear la ventana principal
root = tk.Tk()
root.title("Imagen con Fondo Transparente")

# Crear un lienzo para dibujar
canvas = tk.Canvas(root, width=600, height=600)
canvas.pack()

# Cargar la imagen PNG con fondo transparente
image = PhotoImage(file="..//SmartChess//src//images//dama_negra.png")

# Colocar la imagen en el lienzo
canvas.create_image(0, 0, anchor=tk.NW, image=image)

# Agregar otros widgets encima del lienzo si es necesario
label = tk.Label(root, text="Texto sobre la imagen")
label.pack()

# Ejecutar la aplicación
root.mainloop()
