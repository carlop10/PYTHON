""" Estructuras de Datos - Listas Enlazadas """
""" Autor: Carlos Arturo Lopez Manga """
""" Asignatura: Electiva de profundización 3 - 7A """
""" Fecha: 10 de septiembre de 2025 """
""" Descripción: Implementación de listas enlazadas simples, dobles y circulares con un menú interactivo. """

from nodo import nodo

""" ------------------ Lista Simple ------------------ """

class lista_simple:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.der:
                actual = actual.der
            actual.der = nuevo_nodo
            nuevo_nodo.izq = actual

    def eliminar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                if actual.izq:
                    actual.izq.der = actual.der
                if actual.der:
                    actual.der.izq = actual.izq
                if actual == self.cabeza:
                    self.cabeza = actual.der
                return
            actual = actual.der

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.der
        return False

    def mostrar(self):
        valores = []
        actual = self.cabeza
        while actual:
            valores.append(actual.valor)
            actual = actual.der
        return valores

""" ------------------ Lista Doble ------------------ """

class lista_doble:
    def __init__(self):
        self.cabeza = None
        self.cola = None

    def agregar(self, valor):
        nuevo_nodo = nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            self.cola = nuevo_nodo
        else:
            self.cola.der = nuevo_nodo
            nuevo_nodo.izq = self.cola
            self.cola = nuevo_nodo

    def eliminar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                if actual.izq:
                    actual.izq.der = actual.der
                if actual.der:
                    actual.der.izq = actual.izq
                if actual == self.cabeza:
                    self.cabeza = actual.der
                if actual == self.cola:
                    self.cola = actual.izq
                return
            actual = actual.der

    def buscar(self, valor):
        actual = self.cabeza
        while actual:
            if actual.valor == valor:
                return True
            actual = actual.der
        return False

    def mostrar(self):
        valores = []
        actual = self.cabeza
        while actual:
            valores.append(actual.valor)
            actual = actual.der
        return valores
    
    def mostrar_inverso(self):
        valores = []
        actual = self.cola
        while actual:
            valores.append(actual.valor)
            actual = actual.izq
        return valores
    
""" ------------------ Lista Circular ------------------ """

class lista_circular:
    def __init__(self):
        self.cabeza = None

    def agregar(self, valor):
        nuevo_nodo = nodo(valor)
        if not self.cabeza:
            self.cabeza = nuevo_nodo
            nuevo_nodo.der = nuevo_nodo
            nuevo_nodo.izq = nuevo_nodo
        else:
            cola = self.cabeza.izq
            cola.der = nuevo_nodo
            nuevo_nodo.izq = cola
            nuevo_nodo.der = self.cabeza
            self.cabeza.izq = nuevo_nodo

    def eliminar(self, valor):
        if not self.cabeza:
            return
        actual = self.cabeza
        while True:
            if actual.valor == valor:
                if actual.izq:
                    actual.izq.der = actual.der
                if actual.der:
                    actual.der.izq = actual.izq
                if actual == self.cabeza:
                    if actual.der == actual:
                        self.cabeza = None
                    else:
                        self.cabeza = actual.der
                return
            actual = actual.der
            if actual == self.cabeza:
                break

    def buscar(self, valor):
        if not self.cabeza:
            return False
        actual = self.cabeza
        while True:
            if actual.valor == valor:
                return True
            actual = actual.der
            if actual == self.cabeza:
                break
        return False

    def mostrar(self):
        valores = []
        if not self.cabeza:
            return valores
        actual = self.cabeza
        while True:
            valores.append(actual.valor)
            actual = actual.der
            if actual == self.cabeza:
                break
        return valores
    
    def mostrar_inverso(self):
        valores = []
        if not self.cabeza:
            return valores
        actual = self.cabeza.izq
        while True:
            valores.append(actual.valor)
            actual = actual.izq
            if actual == self.cabeza.izq:
                break
        return valores
    
""" --------------- Menú para interactuar con las listas --------------- """

def menu_lista(lista):
    while True:
        print("\n1. Agregar")
        print("2. Eliminar")
        print("3. Buscar")
        print("4. Mostrar")
        if hasattr(lista, "mostrar_inverso"):
            print("5. Mostrar inverso")
            print("6. Salir")
        else:
            print("5. Salir")
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            valor = input("Valor a agregar: ")
            lista.agregar(valor)
            print("Agregado.")
        elif opcion == "2":
            valor = input("Valor a eliminar: ")
            lista.eliminar(valor)
            print("Eliminado.")
        elif opcion == "3":
            valor = input("Valor a buscar: ")
            encontrado = lista.buscar(valor)
            print("Encontrado." if encontrado else "No encontrado.")
        elif opcion == "4":
            print("Lista:", lista.mostrar())
        elif opcion == "5" and hasattr(lista, "mostrar_inverso"):
            print("Lista inversa:", lista.mostrar_inverso())
        elif (opcion == "5" and not hasattr(lista, "mostrar_inverso")) or (opcion == "6" and hasattr(lista, "mostrar_inverso")):
            break
        else:
            print("Opción inválida.")


"""------------------ |********************| ------------------ """
"""------------------ | Programa Principal | ------------------ """
"""------------------ |********************| ------------------ """

if __name__ == "__main__":
    
    while True:
        print("\n--- Menú Principal ---")
        print("1. Lista Simple")
        print("2. Lista Doble")
        print("3. Lista Circular")
        print("4. Salir")
        tipo = input("Seleccione el tipo de lista: ")
        if tipo == "1":
            lista = lista_simple()
            menu_lista(lista)
        elif tipo == "2":
            lista = lista_doble()
            menu_lista(lista)
        elif tipo == "3":
            lista = lista_circular()
            menu_lista(lista)
        elif tipo == "4":
            break
        else:
            print("Opción inválida.")