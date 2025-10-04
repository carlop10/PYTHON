""" Estructuras de Datos - Arboles Binarios """
""" Autor: Carlos Arturo Lopez Manga """
""" Asignatura: Electiva de profundización 3 - 7A """
""" Fecha: 10 de septiembre de 2025 """
""" Descripción: Implementación de árboles binarios con recorridos inorden, preorden y postorden. """

from nodo import nodo

class arbol:
    def __init__(self):
        self.raiz = None
        
    def insertar(self, valor):
        self.raiz = self.insertar_recursivo(self.raiz, valor)
        
    def insertar_recursivo(self, raiz, valor):
        if raiz == None:
            return nodo(valor)        
        if valor < raiz.valor:
            raiz.izq = self.insertar_recursivo(raiz.izq, valor)
        else:
            raiz.der = self.insertar_recursivo(raiz.der, valor)
            
        return raiz
    
    def recorrer(self, lista_numeros):
        for num in lista_numeros:
            self.insertar(num)
            
    def inorden(self, raiz):
        if raiz is not None:
            self.inorden(raiz.izq)
            print(raiz.valor, end=" ")
            self.inorden(raiz.der)
            
    def preorden(self, raiz):
        if raiz is not None:
            print(raiz.valor, end=" ")
            self.preorden(raiz.izq)
            self.preorden(raiz.der)
            
    def postorden(self, raiz):
        if raiz is not None:
            self.postorden(raiz.izq)
            self.postorden(raiz.der)
            print(raiz.valor, end=" ")
        
    def contar_nodos(self, raiz):
        if raiz is None:
            return 0
        return 1 + self.contar_nodos(raiz.izq) + self.contar_nodos(raiz.der)


"""------------------ |********************| ------------------ """
"""------------------ | Programa Principal | ------------------ """
"""------------------ |********************| ------------------ """

if __name__ == "__main__":

    lista_a = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    lista_b = [0, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    lista_c = [50, 30, 70, 20, 40, 60, 80, 10, 25, 35, 45]

    arbol_a = arbol()
    arbol_a.recorrer(lista_a)

    arbol_b = arbol()
    arbol_b.recorrer(lista_b)

    arbol_c = arbol()
    arbol_c.recorrer(lista_c)

    print("Árbol A - Inorden:")
    arbol_a.inorden(arbol_a.raiz)
    print("\nÁrbol A - Preorden:")
    arbol_a.preorden(arbol_a.raiz)
    print("\nÁrbol A - Postorden:")
    arbol_a.postorden(arbol_a.raiz)
    print("\n")

    print("Árbol B - Inorden:")
    arbol_b.inorden(arbol_b.raiz)
    print("\nÁrbol B - Preorden:")
    arbol_b.preorden(arbol_b.raiz)
    print("\nÁrbol B - Postorden:")
    arbol_b.postorden(arbol_b.raiz)
    print("\n")

    print("Árbol C - Inorden:")
    arbol_c.inorden(arbol_c.raiz)
    print("\nÁrbol C - Preorden:")
    arbol_c.preorden(arbol_c.raiz)
    print("\nÁrbol C - Postorden:")
    arbol_c.postorden(arbol_c.raiz)
    print()

