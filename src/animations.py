import tkinter as tk

class Animations:
    def __init__(self, screen):
        self.screen = screen
    def desvanecimiento(self, alpha=1.0, step=0.05, delay=100):
        if alpha > 0:
            alpha -= step
            self.screen.wm_attributes("-alpha", alpha)
            self.screen.after(delay, self.desvanecimiento, alpha, step, delay)
        else:
            self.screen.destroy()

    