from PIL import Image, ImageOps

# Abrir la imagen
imagen = Image.open('D://MILO//PORTAFOLIO_PROYECTOS//SmartChess//src//images//alfil_blanco.png')
imagen = imagen.convert("RGB")
# Invertir los colores
imagen_invertida = ImageOps.invert(imagen)

# Guardar la imagen invertida
imagen_invertida.save('D://MILO//PORTAFOLIO_PROYECTOS//SmartChess//src//images//alfil_blanco_inv.png')

# Mostrar la imagen invertida
imagen_invertida.show()