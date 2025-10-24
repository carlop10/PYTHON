# Juego Torres de Hanoi
# Estuduante: Carlos Lopez
# Asignatura: Electiva de Profundizacion III - 7A

def hanoi(n, origen, destino, auxiliar, movimientos):
    if n == 1:
        movimientos.append((origen, destino))
        return
    hanoi(n - 1, origen, auxiliar, destino, movimientos)
    movimientos.append((origen, destino))
    hanoi(n - 1, auxiliar, destino, origen, movimientos)


def mostrar_varillas(varillas):
    print()
    for i, varilla in enumerate(varillas):
        print(f"Varilla {i + 1}: {varilla}")
    print()


def mover_disco(varillas, origen, destino):
    if not varillas[origen]:
        print(">!! Movimiento inválido: La varilla de origen está vacía.")
        return False
    disco = varillas[origen][-1]
    if varillas[destino] and varillas[destino][-1] < disco:
        print(">!! Movimiento inválido: No se puede colocar un disco más grande sobre uno más pequeño.")
        return False
    varillas[origen].pop()
    varillas[destino].append(disco)
    return True


def jugar_hanoi(n):
    varillas = [list(range(n, 0, -1)), [], []]
    movimientos_realizados = 0
    print("=== Estado inicial de las varillas ===")
    mostrar_varillas(varillas)
    while len(varillas[2]) != n:
        try:
            origen = int(input("Ingrese la varilla de origen: ")) - 1
            destino = int(input("Ingrese la varilla de destino: ")) - 1
            if origen not in [0, 1, 2] or destino not in [0, 1, 2]:
                print(">$ Entrada inválida. Ingrese números entre 1 y 3.")
                continue
            if mover_disco(varillas, origen, destino):
                movimientos_realizados += 1
                print(
                    f"\n>> Movimiento realizado: Varilla {origen + 1} -> Varilla {destino + 1}"
                )
                mostrar_varillas(varillas)
        except ValueError:
            print(">$ Entrada inválida. Ingrese números válidos.")
    print(f"¡Felicidades! Has completado el juego en {movimientos_realizados} movimientos.")
    print("=== Estado final de las varillas ===")
    mostrar_varillas(varillas)


if __name__ == "__main__":
    num_discos = int(input("Ingrese el número de discos: "))
    jugar_hanoi(num_discos)
