def laberinto(mapa, fila, col, visitados=None):
    if visitados is None:
        visitados = set()
    if (fila, col) in visitados or fila < 0 or col < 0 or fila >= len(mapa) or col >= len(mapa[0]):
        return 0
    if mapa[fila][col] == 9:
        return 1
    if mapa[fila][col] == 1:
        return 0

    visitados.add((fila, col))

    total = (
        laberinto(mapa, fila + 1, col, visitados.copy()) +
        laberinto(mapa, fila - 1, col, visitados.copy()) +
        laberinto(mapa, fila, col + 1, visitados.copy()) +
        laberinto(mapa, fila, col - 1, visitados.copy())
    )

    return total

# Mapa: 0 = libre, 1 = muro, 9 = salida
laberinto_mapa = [
    [0, 0, 1, 9],
    [1, 0, 1, 1],
    [0, 0, 0, 0]
]

print(laberinto(laberinto_mapa, 0, 0))

#Pregunta:
#Explica qué calcula esta función y por qué devuelve el número total de formas distintas de llegar a la salida (valor 9)
#desde la posición inicial (0, 0). ¿Cuál sería el resultado en el ejemplo y qué implicaciones tiene el uso de visitados.copy()
#en la recursión?
#Respuesta:
#La función 'laberinto' calcula el número total de formas distintas de llegar a la salida (representada por el valor 9) desde una posición inicial dada
#en un mapa bidimensional. El mapa está representado como una lista de listas, donde 0 indica una celda libre, 1 indica un muro (celda bloqueada) y 9 indica la salida.
#La función utiliza una estrategia de búsqueda recursiva para explorar todas las posibles rutas desde la posición actual (fila, col) hacia la salida, moviéndose en las cuatro direcciones posibles (arriba, abajo, izquierda, derecha).
#La función devuelve el número total de formas distintas de llegar a la salida porque, cada vez que encuentra la salida (valor 9), retorna 1, y suma todas las rutas válidas que conducen a esa salida desde la posición inicial.
#En el ejemplo proporcionado, la función se llama con la posición inicial (0, 0). El resultado sería 2, ya que hay dos rutas distintas para llegar a la salida:
#1. (0,0) -> (0,1) -> (1,1) -> (2,1) -> (2,2) -> (2,3) -> (1,3) -> (0,3)
#2. (0,0) -> (0,1) -> (1,1) -> (2,1) -> (2,2) -> (2,3) -> (1,3) -> (0,3)
#El uso de visitados.copy() en la recursión es crucial porque asegura que cada llamada recursiva tenga su propia copia del conjunto de celdas visitadas. Esto evita que las rutas exploradas en una rama de la recursión afecten a otras ramas. Si no se hiciera una copia, una celda marcada como visitada en una rama podría impedir que otra rama la explore, lo que resultaría en un conteo incorrecto de las rutas posibles. Al usar visitados.copy(), cada camino explorado mantiene su propio estado de celdas visitadas, permitiendo así una exploración completa y correcta de todas las rutas posibles hacia la salida.
# La función laberinto calcula el número total de formas distintas de llegar a la salida (valor 9)
# desde la posición inicial (0, 0) en un mapa representado por una matriz.
# La función utiliza una estrategia de búsqueda recursiva para explorar todas las posibles rutas desde la   posición actual.
# Cada vez que la función encuentra la salida (valor 9), retorna 1, y suma todas las rutas válidas que conducen a esa salida desde la posición inicial.
# En el ejemplo proporcionado, la función se llama con la posición inicial (0, 0). El resultado sería 2, ya que hay dos rutas distintas para llegar a la salida.
# El uso de visitados.copy() en la recursión es crucial porque asegura que cada llamada recursiva tenga su propia copia del conjunto de celdas visitadas.
# Esto evita que las rutas exploradas en una rama de la recursión afecten a otras ramas, permitiendo así una exploración completa y correcta de todas las rutas posibles hacia la salida.       

