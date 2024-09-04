import tkinter as tk

def fade_out(window, alpha=1.0, step=0.05, delay=100):
    """
    Función para desvanecer la ventana antes de cerrarla.
    - window: la ventana a desvanecer.
    - alpha: valor inicial de opacidad.
    - step: decremento de la opacidad en cada paso.
    - delay: tiempo de espera entre pasos en milisegundos.
    """
    if alpha > 0:
        alpha -= step
        window.wm_attributes('-alpha', alpha)
        window.after(delay, fade_out, window, alpha, step, delay)
    else:
        window.destroy()

# Crear la ventana principal
root = tk.Tk()
root.geometry("300x200")
root.title("Ventana con efecto de desvanecimiento")

# Botón para iniciar el efecto de desvanecimiento
btn_close = tk.Button(root, text="Cerrar con desvanecimiento", command=lambda: fade_out(root))
btn_close.pack(pady=50)

# Ejecutar la aplicación
root.mainloop()