"""
Pawn Rules:

- Movimiento:
  - De Inicio: En el primer movimiento de un peón el jugador puede dar un paso doble si lo desea.
  - Segundo movimiento: Desde el Segundo movimiento en adelante el jugador solo puede moverse 1 
    casilla por turno.

- Captura:
  - Normal: Normalmente un peón solo puede capturar una pieza rival al tenerla en diagonal a una
    distancia de (1x1 casillas).
  - Al paso: La captura al paso es un movimiento especial de los peones, consiste en si tienes un
    peón en cualquier casilla de la 4ta fila y el rival avanza con paso doble con algún peón ubicado
    en una columna lateral a la de tu peón, tu puedes capturarla de forma DIAGONAL. Cabe recalcar que
    movimiento puedes hacerlo unicamente en esa oportunidad.

- Enclavamiento: El enclavamiento es un concepto que debemos tomar para cualquier pieza excepto el rey,
  en el caso del peón si el rey se encuentra en la misma columna, fila o diagonal al peón este puede ser 
  enclavado por una torre (fila, columna), alfil(diagonales) o dama(columna, fila, diagonales). Esto produce
  que el peón sea incapaz de moverse de esta trayectoria, por ejemplo, si la torre rival se encuentra en
  la misma columna que tu rey y tu peón se interpone entre ambas piezas, este peón unicamnete puede moverse
  en esa dirección.
"""

team = "white"
posFila = 2
posCol = "E"


