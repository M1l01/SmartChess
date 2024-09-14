from PIL import Image, ImageTk

class ImgLabel:
    def __init__(self, dirImg, newsize) -> None:
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

class Coords:
    def obtencion_coordenadas_piezas(self, coord):
        try:
            if len(coord) == 2:
                letra = ord(coord[0])
                numero = int(coord[1])
                if (letra>=65 or letra <=72) and (numero>=1 or numero <=8):
                    coordLetra = 240 + (99*(letra-65)) + letra
                    coordNumero = 855 - (100*(numero-1))
                    return (coordLetra, coordNumero)
                else:
                    raise SyntaxError("Coordenada fuera de rango")
            else:
                raise SyntaxError("Error en la longitud de la coordenada se espera una letra mayuscula y un número")
        except SyntaxError:
            raise
    
if __name__ == "__main__":
    coordenada = Coords()
    pos = coordenada.obtencion_coordenadas_piezas("E5")
    print(pos[0])
    print(pos[1])
    