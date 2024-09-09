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

class Pawn:
  def __init__(self, canvas = Canvas, coordenada="A1", team="white"):
    self.canvas = canvas
    self.coordenada = coordenada
    self.team = team

  def movimiento_peon(self):
    self.casillas_primer_movimiento()
    self.crear_punto_captura()

  def click_circulo(self, event):
    print("click en punto")

  def casillas_primer_movimiento(self):
    #Primer Movimiento
    if int(self.coordenada[1]) == 2:
      for fila in range(1,3):
        posibleCoord = Coords().obtencion_coordenadas_piezas(self.coordenada[0] + str(int(self.coordenada[1]) + fila))
        x0, y0 = posibleCoord[0]-270, posibleCoord[1]-120
        punto = self.canvas.create_oval(x0, y0, x0+30, y0+30, outline="", fill="black")
        self.canvas.tag_bind(punto, "<Button-1>", self.click_circulo)

  def crear_punto_captura(self):
    # Detección para captura
    if self.coordenada[0] == chr(65): #Columna A
      # Revisamos diagonal derecha - Columna B
      posibleCoord = Coords().obtencion_coordenadas_piezas(chr(ord(self.coordenada[0]) + 1) + str(int(self.coordenada[1])+1))
      x0,y0 = posibleCoord[0]-270, posibleCoord[1]-120
      punto=self.canvas.create_oval(x0, y0, x0+30, y0+30, outline="black", fill="")
      self.canvas.tag_bind(punto, "<Button-1>", self.click_circulo)
    elif self.coordenada[0] >= chr(66) or self.coordenada[0] <= chr(71):
      # Revisamos las 2 diagonales
      posibleCoord1 = chr(ord(self.coordenada[0])+1) + str(int(self.coordenada[1])+1)
      posibleCoord2 = chr(ord(self.coordenada[0])-1) + str(int(self.coordenada[1])+1)
    elif self.coordenada[0] == chr(72):
      # Revisamos diagonal izquierda - Columna G
      posibleCoord = chr(ord(self.coordenada[0])+1) + str(int(self.coordenada[1])+1)
    else:
      print("Coordenada fuera de rango")

