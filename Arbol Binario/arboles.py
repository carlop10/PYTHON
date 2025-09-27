""" Estructuras de Datos - Árboles Binarios """
""" Autor: Carlos Lopez y David Alvarez """
""" Asignatura: Electiva de profundización 3 - 7A """
""" Fecha: 10 de septiembre de 2025 """
""" Descripción: Implementación de la funcionalidad solicitada: contar nodos del arbol. """

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


    ''' --------- 3. Cantidad de los Nodos (David Alvarez y Carlos Lopez) --------- '''

    def contar_nodos(self, raiz):
        if raiz is None:
            return 0
        return 1 + self.contar_nodos(raiz.izq) + self.contar_nodos(raiz.der)


"""------------------ |********************| ------------------ """
"""------------------ | Programa Principal | ------------------ """
"""------------------ |********************| ------------------ """

if __name__ == "__main__":
    numeros = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]

    arbol = arbol()
    arbol.recorrer(numeros)

    """
    print("Valores del árbol en inorden: \n ")
    arbol.inorden(arbol.raiz)
    print()
    
    print("Valores del árbol en preorden: \n ")
    arbol.preorden(arbol.raiz)
    print()
    
    print("Valores del árbol en postorden: \n ")
    arbol.postorden(arbol.raiz)
    print()

    """

    print("La cantidad de nodos en el árbol es:", arbol.contar_nodos(arbol.raiz))

