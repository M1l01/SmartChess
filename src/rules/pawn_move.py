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
  def __init__(self, canvas, nombrePieza, lblPiezaSelect, listaLblPiezas,cambio_turno_callback):
    self.canvas = canvas
    self.nombrePieza = nombrePieza
    self.piezas = tratamientoJson().import_datos()
    self.lblPiezaSelect = lblPiezaSelect
    self.listaLblPiezas = listaLblPiezas

    #   """Funciones de Callback"""
    self.cambio_turno_callback = cambio_turno_callback

    self.puntosActuales = []
  
  
  def puntos_movimiento(self):
    coordenadaActual = self.piezas[self.nombrePieza]["coordenada"][-1] #ultima ubicacion
    team = self.piezas[self.nombrePieza]["team"]

    print(coordenadaActual)

    direccion = 1 if team == "white" else -1
    filaInicial = 2 if team == "white" else 7

    bloqueoPeon1 = False
    bloqueoPeon2 = False

    capturaDiagDer = False
    capturaDiagIzq = False

    nombrePiezaCapturaDer = ""
    nombrePiezaCapturaIzq = ""

    for clave, piezaParams in self.piezas.items():
      #Ultima coordenada
      lastCoord = piezaParams["coordenada"][-1]
      teamPieza = piezaParams["team"]

      #                     """Movimientos"""
      if lastCoord == (coordenadaActual[0] + str(int(coordenadaActual[1])+direccion)):
        # Pieza a una casilla bloqueando
        bloqueoPeon1 = True

      elif lastCoord == (coordenadaActual[0] + str(int(coordenadaActual[1])+(2*direccion))):
        # Pieza a dos casillas bloqueando
        bloqueoPeon2 = True

      #                       """Capturas"""
      if coordenadaActual[0] == "A" and lastCoord == (chr(ord(coordenadaActual[0])+1) + str(int(coordenadaActual[1])+direccion)) and teamPieza != team:
        #Revisar solo la diagonal Derecha
        capturaDiagDer = True
        #Extraer el nombre de la pieza
        nombrePiezaCapturaDer = clave
        print("Puedes capturar a la Derecha")

      elif (ord(coordenadaActual[0]) >= 66 or ord(coordenadaActual[0]) <= 71) and teamPieza != team:
        #Revisar diagonal Derecha e Izquierda
        if lastCoord == chr(ord(coordenadaActual[0])+1) + str(int(coordenadaActual[1])+direccion):
          capturaDiagDer = True
          #Extraer el nombre de la pieza
          nombrePiezaCapturaDer = clave
          print("puedes capturar a la derecha")

        elif lastCoord == chr(ord(coordenadaActual[0])-1) + str(int(coordenadaActual[1])+direccion) and teamPieza != team:
          capturaDiagIzq = True
          #Extraer el nombre de la pieza
          nombrePiezaCapturaIzq = clave
          print("puedes capturar a la izquierda")

      elif coordenadaActual[0] == "H" and lastCoord == (chr(ord(coordenadaActual[0])-1) + str(int(coordenadaActual[1])+direccion)) and teamPieza != team:
        #Revisar solo diagonal Izquierda
        capturaDiagIzq = True
        #Extraer el nombre de la pieza
        nombrePiezaCapturaIzq = clave
        print("Puedes capturar a la izquierda")

    #               """Movimientos"""
    if bloqueoPeon1 and not capturaDiagDer and not capturaDiagIzq:
      print("No puedes mover")

    elif bloqueoPeon2 or ((int(coordenadaActual[1]) > filaInicial) if team == "white" else (int(coordenadaActual[1]) < filaInicial)):
      self.dar_paso(coordenadaActual, direccion)
      print("puedes dar un paso")

    elif int(coordenadaActual[1]) == filaInicial:
      self.dar_paso(coordenadaActual, direccion)
      self.dar_paso_doble(coordenadaActual, direccion)
      print("puedes dar hasta 2 pasos")

    else:
      print("algo anda mal")

    #                 """Capturas"""
    if capturaDiagDer and not capturaDiagIzq and team:
      self.captura_derecha_lbl(nombrePiezaCapturaDer)
      self.captura_derecha(coordenadaActual, direccion)

    elif capturaDiagIzq and not capturaDiagDer:
      self.captura_izquierda(coordenadaActual, direccion)

    elif capturaDiagDer and capturaDiagIzq:
      self.captura_derecha(coordenadaActual, direccion)
      self.captura_izquierda(coordenadaActual, direccion)
    else:
      print("No hay capturas")
     
    return self.puntosActuales
  
  def click_cuadro(self, event, Coord, casillaSelect):
    print("capturaste")

  def click_pieza(self, event):
    print("Label de la Pieza pulsada -> Capturaste")

  def captura_derecha_lbl(self, nombreCapturaDer):
    lblPiezaCapturaDer = None
    for nombrePieza, lblPieza in self.listaLblPiezas:
      if nombrePieza == nombreCapturaDer:
        lblPiezaCapturaDer = lblPieza

    if lblPiezaCapturaDer != None:
      print("boton activado")
      lblPiezaCapturaDer.bind("<Button-1>", self.click_pieza)
  
  def captura_derecha(self, coordenadaActual, direccion):
    casilla = chr(ord(coordenadaActual[0])+1) + str(int(coordenadaActual[1])+direccion)
    cuadro, posibleCoord = self.crear_cuadro_captura(casilla)
    self.canvas.tag_bind(cuadro, "<Button-1>", lambda event: self.click_cuadro(event, posibleCoord, casilla))
    self.puntosActuales.append(cuadro)

  def captura_izquierda(self, coordenadaActual, direccion):
    casilla = chr(ord(coordenadaActual[0])-1) + str(int(coordenadaActual[1])+direccion)
    cuadro, posibleCoord = self.crear_cuadro_captura(casilla)
    self.canvas.tag_bind(cuadro, "<Button-1>", lambda event: self.click_cuadro(event, posibleCoord, casilla))
    self.puntosActuales.append(cuadro)

  def crear_cuadro_captura(self, casilla):
    posibleCoord = Coords().obtencion_coordenadas_piezas(casilla)
    x0, y0 = posibleCoord[0]-305, posibleCoord[1]-155
    cuadro = self.canvas.create_rectangle(x0, y0, x0+100, y0+100, outline="", fill="#f00")
    return cuadro, posibleCoord
  
  def click_point(self, event, Coord, casillaSelect):
    bgColor = "#9e9fa2" if (((Coord[0] + Coord[1] - 60)/100)%2 == 0) else "#0d4a6a"
    self.lblPiezaSelect.config(bg = bgColor)
    self.lblPiezaSelect.place(x=Coord[0], y=Coord[1])

    tratamientoJson(self.nombrePieza).Almacenar_coordenada(casillaSelect)  
    
    self.cambio_turno_callback()

  def crear_punto(self, casilla): 
    posibleCoord = Coords().obtencion_coordenadas_piezas(casilla)
    pointColor = "#898a8c" if (((posibleCoord[0] + posibleCoord[1] - 60)/100)%2 == 0) else "#093a54"
    x0, y0 = posibleCoord[0]-270, posibleCoord[1]-120
    punto = self.canvas.create_oval(x0, y0, x0+30, y0+30, outline="", fill=pointColor)
    return punto, posibleCoord
  
  def dar_paso(self, coordenadaActual, direccion):
    nuevaFila = int(coordenadaActual[1]) + direccion
    casilla = coordenadaActual[0] + str(nuevaFila)
    punto, posibleCoord = self.crear_punto(casilla)
    self.canvas.tag_bind(punto, "<Button-1>", lambda event: self.click_point(event, posibleCoord, casilla))
    self.puntosActuales.append(punto)
  
  def dar_paso_doble(self, coordenadaActual, direccion):
    nuevaFila = int(coordenadaActual[1]) + (2*direccion)
    casilla = coordenadaActual[0] + str(nuevaFila)
    punto, posibleCoord = self.crear_punto(casilla)
    self.canvas.tag_bind(punto, "<Button>", lambda event: self.click_point(event, posibleCoord, casilla))
    self.puntosActuales.append(punto)