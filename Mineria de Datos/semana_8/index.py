# Crear una aplicacion en python que cargue una lista con N cantidad de valores numericos( solo se deben cargar datos numericos) a partir de esto debe hacer lo siguiente:
# 1)detectar si existen numeros repetidos,
# 2)si hay numeros repetidos debe informar cuantas veces aparece cada numero repetido.
# 3)adicional a eso debe cargar en una tupla o lista diferente con todos esos numeros repetidos y decir de todos esos numeros repetidos cual es el que mas se repite.
# 4)En el caso de que no exista numeros repetidos simplemente no genera ningun otra lista o tupla.
# 5)tambien debe limpiar la lista original de tal manera que quede sin numeros repetidos.

class NumerosRepetidos:
    def __init__(self):
        self.numeros = []
        self.repetidos = {}
        self.lista_repetidos = []

    def cargar_lista(self, cantidad):
        for _ in range(cantidad):
            sw = True
            while sw:
                try:
                    numero = float(input("Ingrese un numero: "))
                    self.numeros.append(numero)
                    sw = False
                except ValueError:
                    print("--> Por favor, ingrese un valor numerico valido.")

    def detectar_repetidos(self):
        for numero in self.numeros:
            repeticiones = self.numeros.count(numero)
            if repeticiones > 1:
                self.repetidos[numero] = repeticiones

        if self.repetidos:
            self.lista_repetidos = list(self.repetidos.keys())
            numero_mas_repetido = max(self.repetidos, key=self.repetidos.get)
            print(f"--> Números repetidos y sus conteos: {self.repetidos}")
            print(
                f"--> Número que más se repite: {numero_mas_repetido} "
                f"(se repite {self.repetidos[numero_mas_repetido]} veces)"
            )
        else:
            print("--> No hay números repetidos.")

    def limpiar_lista(self):
        self.numeros = list(set(self.numeros))
        print(f"--> Lista original sin números repetidos: {self.numeros}")

    def main(self):
        sw = True
        while sw:
            try:
                cantidad = int(input("¿Cuántos números desea ingresar?: "))
                if cantidad <= 0:
                    print("--> Por favor, ingrese un número positivo.")
                else:
                    sw = False
            except ValueError:
                print("--> Por favor, ingrese un valor numérico válido.")

        self.cargar_lista(cantidad)
        self.detectar_repetidos()
        if self.repetidos:
            self.limpiar_lista()

if __name__ == "__main__":
    app = NumerosRepetidos()
    app.main()
