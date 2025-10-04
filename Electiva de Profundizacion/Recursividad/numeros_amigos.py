# Estudiante: Carlos Arturo Lopez Manga
# Asignatura: Electiva de Profundizacion III
# Fecha: 01/10/2025

class namigos_recursividad:
    def __init__(self, n):
        self.n = n
        self.suma = 0
        
    def numeros_amigos(self, n):
        if n < 1:
            return self.suma
        if self.n % n == 0:
            print(n)
            self.suma += n

        return self.numeros_amigos(n - 1)


if __name__ == "__main__":
    n1 = int(input("Ingrese el primer numero: "))
    n2 = int(input("Ingrese el segundo numero: "))

    num1 = namigos_recursividad(n1)
    num2 = namigos_recursividad(n2)

    print(f"\nDivisores de {n1}")
    suma1 = num1.numeros_amigos(n1 / 2)
    print(f"Suma de divisores de {n1}: {suma1}")

    print(f"\nDivisores de {n2}")
    suma2 = num2.numeros_amigos(n2 / 2)
    print(f"Suma de divisores de {n2}: {suma2}")

    print()

    if suma1 == n2 and suma2 == n1:
        print(f"{n1} y {n2} son numeros amigos")
    else:
        print(f"{n1} y {n2} no son numeros amigos")
