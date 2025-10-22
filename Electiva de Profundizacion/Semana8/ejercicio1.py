#Ejercicio 1:
#Pregunta:
#Explica detalladamente el propósito de esta función y por qué su resultado no equivale simplemente a la suma de los elementos.
#¿Qué estrategia algorítmica se está utilizando y cuál es el resultado para [1, 3, 1, 5]?
#Justifica con trazas de ejecución parciales.

def resolver(data, memo={}):
    if not data:
        return 0
    if tuple(data) in memo:
        return memo[tuple(data)]

    max_val = 0
    for i in range(len(data)):
        left = data[:i]
        right = data[i+1:]
        val = data[i] + resolver(left, memo) + resolver(right, memo)
        max_val = max(max_val, val)

    memo[tuple(data)] = max_val
    return max_val



# Ejemplo de uso:
print(resolver([1, 3, 1, 5]))

#Respuesta:
#El propósito de la función 'resolver' es encontrar el valor máximo que se puede obtener al seleccionar elementos de una 
# lista de números enteros, donde al seleccionar un elemento, se suman sus valores y se consideran las sublistas resultantes 
# a la izquierda y a la derecha del elemento seleccionado. La función no simplemente suma todos los elementos porque cada vez 
# que se selecciona un elemento, se divide la lista en dos partes (izquierda y derecha), y se calcula el valor máximo posible 
# para cada una de estas partes de manera recursiva.

#La estrategia algorítmica utilizada aquí es la programación dinámica con memoización. La memoización almacena los resultados de 
# subproblemas ya resueltos en un diccionario (memo) para evitar cálculos redundantes, lo que mejora significativamente la eficiencia 
# del algoritmo.

#Para el caso de la lista [1, 3, 1, 5], la función realiza las siguientes trazas de ejecución parciales:
#1. Selecciona el primer elemento (1): valor = 1 + resolver([3, 1, 5])
#   - resolver([3, 1, 5]) selecciona 3: valor = 3 + resolver([1, 5])
#     - resolver([1, 5]) selecciona 1: valor = 1 + resolver([5]) = 1 + 5 = 6
#     - resolver([1, 5]) selecciona 5: valor = 5 + resolver([1]) = 5 + 1 = 6
#   - Máximo para [3, 1, 5] = 3 + 6 = 9
#2. Selecciona el segundo elemento (3): valor = 3 + resolver([1, 5])
#   - Ya calculado, máximo para [1, 5] = 6 
#   - Máximo para [1, 3, 1, 5] = 3 + 6 = 9
#3. Selecciona el tercer elemento (1): valor = 1 + resolver([1, 5])
#   - Ya calculado, máximo para [1, 5] = 6
#   - Máximo para [1, 3, 1, 5] = 1 + 6 = 7
#4. Selecciona el cuarto elemento (5): valor = 5 + resolver([1, 3, 1])
#   - resolver([1, 3, 1]) selecciona 1: valor = 1 + resolver([3, 1])
#     - resolver([3, 1]) selecciona 3: valor = 3 + resolver([1]) = 3 + 1 = 4
#     - resolver([3, 1]) selecciona 1: valor = 1 + resolver([3]) = 1 + 3 = 4
#   - Máximo para [1, 3, 1] = 1 + 4 = 5
#   - Máximo para [1, 3, 1, 5] = 5 + 5 = 10
#Finalmente, el resultado máximo para la lista [1, 3, 1, 5] es 10.
#El resultado de la función para la entrada [1, 3, 1, 5] es 10.



