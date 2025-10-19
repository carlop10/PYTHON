nombres = []
edades = []
promedios = []
programas = []


def agregar():
    n = input("Nombre: ")
    e = int(input("Edad: "))
    p = float(input("Promedio: "))
    pr = input("Programa: ")
    nombres.append(n)
    edades.append(e)
    promedios.append(p)
    programas.append(pr)


def mostrar():
    for i in range(len(nombres)):
        print(
            f"{nombres[i]} - {edades[i]} años - {programas[i]} - Promedio: {promedios[i]}"
        )


def buscar():
    nombre = input("Ingrese nombre a buscar: ")
    for i in range(len(nombres)):
        if nombres[i].lower() == nombre.lower():
            print(f"Encontrado: {nombres[i]} - Promedio: {promedios[i]}")


def promedio_general():
    print("Promedio general:", sum(promedios) / len(promedios))


def menu():
    while True:
        print("\n--- SISTEMA ESTUDIANTES ---")
        print("1. Agregar estudiante")
        print("2. Mostrar lista")
        print("3. Buscar estudiante")
        print("4. Promedio general")
        print("5. Salir")
        op = input("Seleccione opción: ")

        if op == "1":
            agregar()
        elif op == "2":
            mostrar()
        elif op == "3":
            buscar()
        elif op == "4":
            promedio_general()
        elif op == "5":
            break


menu()
