from PIL import Image, ImageTk

class ImgLabel:
    def __init__(self, dirImg, newsize):
        self.dirImg = dirImg
        self.newsize = newsize
    def pngLabel(self, bgColorRgba):
        try:
            image = Image.open(self.dirImg)
            imageResized = image.resize(self.newsize)
            fondo = Image.new("RGBA", imageResized.size, bgColorRgba)
            imageResized = imageResized.convert("RGBA")
            imageComposed = Image.alpha_composite(fondo, imageResized)
            imageRGB = imageComposed.convert("RGB")
            imageRGB = ImageTk.PhotoImage(imageRGB)
            return imageRGB
        except Exception as e:
            print(f"Error: {e}")
        return None
    
    def jpgLabel(self):
        try:
            image = Image.open(self.dirImg)
            imageResized = image.resize(self.newsize)
            imageTK = ImageTk.PhotoImage(imageResized)
            return imageTK
        except Exception as e:
            print(f"Error al cargar la imagen: {e}")
        return None