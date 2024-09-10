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
import ImportarJson


class Pawn:
  def __init__(self, nombrePieza, paramPieza, ListaClavesJson):
    self.nombrePieza = nombrePieza
    self.paramPieza = paramPieza
    self.ListaClavesJson = ListaClavesJson

    self.puntosActuales = []
  
  def click_point(self, event):
    print("click en punto, Mover la pieza a este punto")
  
  def puntos_primer_movimiento(self, canvas):
    coordenadaActual = self.paramPieza["coordenada"][-1] #ultima ubicacion
    team = self.paramPieza["team"]
    if team == "white":
      if int(coordenadaActual[1]) == 2: #Fila 2
        #Crear Puntos
        for fila in range(1,3):
          posibleCoord = Coords().obtencion_coordenadas_piezas(coordenadaActual[0] + str(int(coordenadaActual[1]) + fila))
          x0, y0 = posibleCoord[0]-270, posibleCoord[1]-120
          punto = canvas.create_oval(x0, y0, x0+30, y0+30, outline="", fill="black")
          canvas.tag_bind(punto, "<Button-1>", self.click_point)
          self.puntosActuales.append(punto)
    elif team == "black":
      if int(coordenadaActual[1]) == 7:
        for fila in range(1,3):
          posibleCoord = Coords().obtencion_coordenadas_piezas(coordenadaActual[0] + str(int(coordenadaActual[1]) - fila))
          x0, y0 = posibleCoord[0]-270, posibleCoord[1]-120
          punto = canvas.create_oval(x0, y0, x0+30, y0+30, outline="", fill="black")
          canvas.tag_bind(punto, "<Button-1>", self.click_point)
          self.puntosActuales.append(punto)
    
    return self.puntosActuales



  
  
  
  
  
  """
  def movimiento(self):
    print("movimiento del peon")

  def click_point(self, event):
    print("click en punto")
  
  def casillas_primer_movimiento(self):
    #Primer Movimiento
    if int(self.coordenada[1]) == 2 and self.team == "white":
      for fila in range(1,3):
        posibleCoord = Coords().obtencion_coordenadas_piezas(self.coordenada[0] + str(int(self.coordenada[1]) + fila))
        x0, y0 = posibleCoord[0]-270, posibleCoord[1]-120
        punto = self.canvas.create_oval(x0, y0, x0+30, y0+30, outline="", fill="black")
        self.canvas.tag_bind(punto, "<Button-1>", self.click_point)

  """