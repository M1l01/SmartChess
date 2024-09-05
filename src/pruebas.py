import tkinter as tk
import time

# Crear la ventana principal
root = tk.Tk()
root.geometry("200x100")  # Establecer el tamaño de la ventana

# Función para mover la ventana de izquierda a derecha
def move_window():
    # Obtener la posición actual de la ventana
    x = 0  # Iniciar en el borde izquierdo de la pantalla
    y = 100  # Fijar la posición vertical de la ventana
    
    # Obtener el ancho de la pantalla
    screen_width = root.winfo_screenwidth()
    
    # Mover la ventana de izquierda a derecha
    while x < screen_width - 200:  # 200 es el ancho de la ventana
        root.geometry(f"200x100+{x}+{y}")  # Actualizar la posición de la ventana
        root.update()  # Actualizar la interfaz gráfica
        time.sleep(0.01)  # Esperar un poco para hacer visible el movimiento
        x += 5  # Incrementar la posición horizontal de la ventana

# Llamar a la función de movimiento después de que la ventana se haya mostrado
move_window()

# Ejecutar el bucle principal de Tkinter
root.mainloop()
