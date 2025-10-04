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


    '''
    1. Profundidad del arbol
    '''
    def profundidad(self, nodo):
        if nodo is None:
            return -1  # La profundidad de un nodo nulo es -1
        else:
            izq_profundidad = self.profundidad(nodo.izq)
            der_profundidad = self.profundidad(nodo.der)
            return 1 + max(izq_profundidad, der_profundidad)
        
    '''
    2. La altura del arbol
    '''

    def altura(self, nodo):
        if nodo is None:
            return -1  # La altura de un nodo nulo es -1
        else:
            izq_altura = self.altura(nodo.izq)
            der_altura = self.altura(nodo.der)
            return 1 + max(izq_altura, der_altura)
    
    '''
    3. Cantidad de los nodos
    '''

    def contar_nodos(self, raiz):
        if raiz is None:
            return 0
        return 1 + self.contar_nodos(raiz.izq) + self.contar_nodos(raiz.der)


if __name__ == "__main__":
    numeros = [8, 4, 12, 2, 6, 10, 14, 1, 3, 5, 7, 9, 11, 13, 15]
    arbol = arbol()
    arbol.recorrer(numeros)

    '''
    print("Valores del árbol en inorden: \n ")
    arbol.inorden(arbol.raiz)
    print()
    
    print("Valores del árbol en preorden: \n ")
    arbol.preorden(arbol.raiz)
    print()
    
    print("Valores del árbol en postorden: \n ")
    arbol.postorden(arbol.raiz)
    
    '''

    

    print("Cantidad de nodos en el árbol:", arbol.contar_nodos(arbol.raiz))

    print("Profundidad del árbol:", arbol.profundidad(arbol.raiz))

    print("Altura del árbol:", arbol.altura(arbol.raiz))

"""

1. Profundidad del arbol
2. La altura del arbol
3. La cantidad de los nodos  
4. El nivel de un nodo X
5. Grado de un nodo
6. Si el arbol es completo o no completo
7. Si el arbol está lleno
8. Si el arbol es equilibrado      
9. Recorrido en anchura
10. Buscar un nodo X
11. Eliminar un nodo
12. Actualizar el valor de un nodo X
13. Balancear un arbol
14. Rotar un arbol
15. Preguntar si un arbol es binario o no binario
16. Si elarbol es degenerado
17. Identificar cuantos nodos hoha hay en un arbol
18. Identificar si dos nodos son hermanos

"""