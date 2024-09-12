"""
Pawn Rules:

Movimiento:
    - De Inicio: En el primer movimiento de un peón el jugador puede dar un paso doble si lo desea.
    - Segundo movimiento: Desde el Segundo movimiento en adelante el jugador solo puede moverse 1 
    casilla por turno.

Captura:
    Normal: Normalmente un peón solo puede capturar una pieza rival al tenerla en diagonal a una
    distancia de (1x1 casillas).

    Al paso: La captura al paso es un movimiento especial de los peones, consiste en si tienes un
    peón en cualquier casilla de la 4ta fila y el rival avanza con paso doble con algún peón ubicado
    en una columna lateral a la de tu peón, tu puedes capturarla de forma DIAGONAL. Cabe recalcar que
    movimiento puedes hacerlo unicamente en esa oportunidad.

Enclavamiento: El enclavamiento es un concepto que debemos tomar para cualquier pieza excepto el rey,
en el caso del peón si el rey se encuentra en la misma columna, fila o diagonal al peón este puede ser 
enclavado por una torre (fila, columna), alfil(diagonales) o dama(columna, fila, diagonales). Esto produce
que el peón sea incapaz de moverse de esta trayectoria, por ejemplo, si la torre rival se encuentra en
la misma columna que tu rey y tu peón se interpone entre ambas piezas, este peón unicamnete puede moverse
en esa dirección.
"""
import tkinter as tk
from tkinter import Canvas
from common.utils import Coords
from ImportarJson import tratamientoJson


class Pawn:
  def __init__(self, canvas, nombrePieza, lblPiezaSelect, cambio_turno_callback):
    self.canvas = canvas
    self.nombrePieza = nombrePieza
    self.piezas = tratamientoJson().import_datos()
    self.lblPiezaSelect = lblPiezaSelect

    #   """Funciones de Callback"""
    self.cambio_turno_callback = cambio_turno_callback

    self.puntosActuales = []
  
  def click_point(self, event, Coord, casillaSelect):
    bgColor = "#9e9fa2" if (((Coord[0] + Coord[1] - 60)/100)%2 == 0) else "#0d4a6a"
    self.lblPiezaSelect.config(bg = bgColor)
    self.lblPiezaSelect.place(x=Coord[0], y=Coord[1])

    tratamientoJson(self.nombrePieza).Almacenar_coordenada(casillaSelect)  
    
    self.cambio_turno_callback()
  
  def puntos_movimiento(self):
    coordenadaActual = self.piezas[self.nombrePieza]["coordenada"][-1] #ultima ubicacion
    team = self.piezas[self.nombrePieza]["team"]

    direccion = 1 if team == "white" else -1
    filaInicial = 2 if team == "white" else 7

    ubiRival = ""

    #Ver si puede dar un paso o dos
    for _, piezaParams in self.piezas.items():
      #Ultima coordenada
      lastCoord = piezaParams["coordenada"][-1]
      if team == "white":
        if (lastCoord == (coordenadaActual[0] + str(int(coordenadaActual[1])+1))) or (lastCoord == (coordenadaActual[0] + str(int(coordenadaActual[1])+2))):
          #Extraccion Coordenada
          ubiRival = lastCoord
      else:
        if (lastCoord == (coordenadaActual[0] + str(int(coordenadaActual[1])-1))) or (lastCoord == (coordenadaActual[0] + str(int(coordenadaActual[1])-2))):
          #Extraccion Coordenada
          ubiRival = lastCoord

    if int(coordenadaActual[1]) == filaInicial:
      #                 """Movimiento Inicial"""
      if (ubiRival == (coordenadaActual[0] + str(int(coordenadaActual[1])+1))) or (ubiRival == (coordenadaActual[0] + str(int(coordenadaActual[1])-1))):
        print("No puedes mover")

      elif (ubiRival == (coordenadaActual[0] + str(int(coordenadaActual[1])+2))) or (ubiRival == (coordenadaActual[0] + str(int(coordenadaActual[1])-2))):
        self.dar_paso(coordenadaActual, direccion)

      else:
        self.dar_paso(coordenadaActual, direccion)
        self.dar_paso_doble(coordenadaActual, direccion)

    else:
      if (ubiRival == (coordenadaActual[0] + str(int(coordenadaActual[1])+1))) or (ubiRival == (coordenadaActual[0] + str(int(coordenadaActual[1])-1))):
        print("No puedes mover")
      else:
        self.dar_paso(coordenadaActual, direccion)

    return self.puntosActuales
  
  def crear_punto(self, casilla): 
    posibleCoord = Coords().obtencion_coordenadas_piezas(casilla)
    x0_1, y0_1 = posibleCoord[0]-270, posibleCoord[1]-120
    punto = self.canvas.create_oval(x0_1, y0_1, x0_1+30, y0_1+30, outline="", fill="black")
    return punto, posibleCoord
  
  def dar_paso(self, coordenadaActual, direccion):
    nuevaFila = int(coordenadaActual[1]) + direccion
    casilla1 = coordenadaActual[0] + str(nuevaFila)
    punto1, posibleCoord1 = self.crear_punto(casilla1)
    self.canvas.tag_bind(punto1, "<Button-1>", lambda event: self.click_point(event, posibleCoord1, casilla1))
    self.puntosActuales.append(punto1)
  
  def dar_paso_doble(self, coordenadaActual, direccion):
    nuevaFila = int(coordenadaActual[1]) + (2*direccion)
    casilla2 = coordenadaActual[0] + str(nuevaFila)
    punto2, posibleCoord2 = self.crear_punto(casilla2)
    self.canvas.tag_bind(punto2, "<Button>", lambda event: self.click_point(event, posibleCoord2, casilla2))
    self.puntosActuales.append(punto2)