import tkinter as tk
from PIL import Image, ImageTk

class MoverImagen:
    def __init__(self, ventana, ruta_imagen):
        self.ventana = ventana
        self.ventana.title("Mover Imagen con Mouse")

        # Cargar la imagen
        imagen = Image.open(ruta_imagen)
        self.imagen_tk = ImageTk.PhotoImage(imagen)

        # Crear un canvas y añadir la imagen
        self.canvas = tk.Canvas(ventana, width=1000, height=1000)
        self.canvas.pack()
        self.imagen_en_canvas = self.canvas.create_image(1000, 1000, image=self.imagen_tk)

        # Vincular eventos del mouse
        self.canvas.tag_bind(self.imagen_en_canvas, '<ButtonPress-1>', self.iniciar_arrastre)
        self.canvas.tag_bind(self.imagen_en_canvas, '<B1-Motion>', self.arrastrar)

    def iniciar_arrastre(self, event):
        self.x = event.x
        self.y = event.y

    def arrastrar(self, event):
        dx = event.x - self.x
        dy = event.y - self.y
        self.canvas.move(self.imagen_en_canvas, dx, dy)
        self.x = event.x
        self.y = event.y

# Crear la ventana principal
ventana_principal = tk.Tk()

# Crear una instancia de la clase MoverImagen
# Asegúrate de reemplazar 'ruta/a/tu/imagen.png' con la ruta real de tu imagen
app = MoverImagen(ventana_principal, 'D://MILO//PORTAFOLIO_PROYECTOS//SmartChess//src//images//dama.png')

# Iniciar el bucle principal de la aplicación
ventana_principal.mainloop()