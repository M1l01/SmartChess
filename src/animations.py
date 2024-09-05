import time

class Animations:
    def __init__(self, screen):
        self.screen = screen

    def desvanecimiento(self, alpha=1.0, step=0.05, delay=80):
        if alpha > 0.4:
            self.screen.wm_attributes("-alpha", alpha)
            alpha -= step
            self.screen.update()
            self.screen.after(delay, self.desvanecimiento, alpha, step, delay)
        else:
            self.screen.destroy()
        
    def movimiento_horizontal(self, posInicialX, posY, geometryX, geometryY, posFinalX):
        while posInicialX <= posFinalX:
            try:
                self.screen.geometry(f"{geometryX}x{geometryY}+{posInicialX}+{posY}")
                self.screen.update()
                time.sleep(0.01)
                posInicialX += 5
            except Exception as e:
                print(f"Error: {e}")
        self.screen.destroy()

    def desvanecimiento_horizontal(self, posInicialX, posY, geometryX, geometryY, posFinalX, alpha=1.0, step=0.05):
        while posInicialX < posFinalX:
            try:
                self.screen.geometry(f"{geometryX}x{geometryY}+{posInicialX}+{posY}")
                self.screen.wm_attributes("-alpha", alpha)
                self.screen.update()
                time.sleep(0.01)
                posInicialX += 5
                alpha -= step
            except Exception as e:
                print(f"Error: {e}")
        self.screen.destroy()

    