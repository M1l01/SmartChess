import tkinter as tk
import json

# Función para cargar datos desde el archivo JSON
def cargar_datos():
    try:
        with open('..//SmartChess//src//piezas.json', 'r') as archivo:
            datos = json.load(archivo)
        return datos
    except FileNotFoundError:
        return {"usuarios": []}  # Devuelve un diccionario vacío si el archivo no existe

# Función para mostrar los datos en la lista de Tkinter
def mostrar_datos():
    lista_usuarios.delete(0, tk.END)  # Limpia la lista antes de cargar nuevos datos
    datos = cargar_datos()
    for usuario in datos["usuarios"]:
        lista_usuarios.insert(tk.END, f"Nombre: {usuario['nombre']}, Edad: {usuario['edad']}")

# Crear la ventana principal
ventana = tk.Tk()
ventana.title("Lista de Usuarios")

# Crear un botón para cargar y mostrar los datos
btn_cargar = tk.Button(ventana, text="Cargar Usuarios", command=mostrar_datos)
btn_cargar.pack(pady=10)

# Crear una lista para mostrar los usuarios
lista_usuarios = tk.Listbox(ventana, width=40, height=10)
lista_usuarios.pack(pady=10)

# Ejecutar la aplicación
ventana.mainloop()
