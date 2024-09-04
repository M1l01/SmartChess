import tkinter as tk
from PIL import Image, ImageTk

class ImageCache:
    def __init__(self):
        self.cache = {}

    def get_image(self, dirImg, newsize, bgcolorrgba):
        cache_key = (dirImg, newsize, bgcolorrgba)
        if cache_key not in self.cache:
            try:
                image = Image.open(dirImg)
                imageResized = image.resize(newsize)
                fondo = Image.new("RGBA", imageResized.size, bgcolorrgba)
                imageResized = imageResized.convert("RGBA")
                imageComposed = Image.alpha_composite(fondo, imageResized)
                imageRGB = imageComposed.convert("RGB")
                imageTk = ImageTk.PhotoImage(imageRGB)
                self.cache[cache_key] = imageTk
            except Exception as e:
                print(f"Error al cargar la imagen: {e}")
                return None
        return self.cache[cache_key]

class SmartChessInterface:
    def __init__(self, root):
        self.root = root
        self.root.title("Ventana Principal")
        self.root.geometry("1600x900")
        self.root.configure(bg="#232427")
        self.screen = root
        self.image_cache = ImageCache()

    def lbl_Pieza(self, dirImg, newsize, pos, funcEnterMouse):
        try:
            [bgcolor, bgcolorrgba] = ["#dad9b5", (158, 159, 162, 255)] if (((pos[0] + pos[1] - 60)/100) % 2 == 0) else ["#0d4a6a", (13, 74, 106, 255)]
            imageRGB = self.image_cache.get_image(dirImg, newsize, bgcolorrgba)
            if imageRGB:
                lblPieza = tk.Label(self.screen, image=imageRGB, bg=bgcolor, bd=0)
                lblPieza.image = imageRGB
                lblPieza.place(x=pos[0], y=pos[1])
                lblPieza.bind("<Enter>", funcEnterMouse)
                return lblPieza
        except Exception as e:
            print(f"Error: {e}")
        return None

if __name__ == "__main__":
    root = tk.Tk()
    app = SmartChessInterface(root)

    # Ejemplo de uso de lbl_Pieza
    def on_enter(event):
        print("Mouse ha entrado")

    app.lbl_Pieza("..//SmartChess//src//images//dama_blanca.png", (100, 100), (200, 200), on_enter)
    root.mainloop()
