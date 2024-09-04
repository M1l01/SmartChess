from PIL import Image, ImageTk

class ImgLabel:
    def pngLabel(dirImg, colorFondo, newsize):
        try:
            image = Image.open(dirImg)
            imageResized = image.resize(newsize)
            fondo = Image.new("RGBA", imageResized.size, colorFondo)
            imageResized = imageResized.convert("RGBA")
            imageComposed = Image.alpha_composite(fondo, imageResized)
            imageRGB = imageComposed.convert("RGB")
            imageRGB = ImageTk.PhotoImage(imageRGB)
            
        except Exception as e:
            print(f"Error: {e}")
            return None
        return imageRGB