# print("Hola Mundo")
# dato1:int = 10
# dato2:int = 20

# suma:int = dato1 + dato2
# print("La suma es:", suma)


# #for de una sola linea
# numerosCuadrados = [x**2 for x in range(10)]
# print(numerosCuadrados)

# #for de una sola linea para extraer los numeros pares
# numerosPares = [x for x in range(10) if x % 2 == 0]
# print(numerosPares)

#Evaluar número mayor, medio y menor.
#Haga una app en python que permita capturar 3 numeros
# enteros cualquiera y me informa cual es el numero mayor,
# cual es el menor y cual es el del medio.
# independientemente de cual sea el orden de captura. 
# tambien evalue los casos de numeros repetidos. en tal
#  caso si hay numeros repetidos debe decir cuales son
#  repetidos , cual es el diferente y si son mayores o
#  menores entre ellos. evalue todas las posibilidades.

def mayor_menor_medio(a, b, c):
    if a == b and b == c:
        return "Los tres números son iguales."
    elif a == b:
        if a > c:
            return f"Los números {a} y {b} son mayores y el número diferente es {c}."
        else:
            return f"Los números {a} y {b} son menores y el número diferente es {c}."
    elif a == c:
        if a > b:
            return f"Los números {a} y {c} son mayores y el número diferente es {b}."
        else:
            return f"Los números {a} y {c} son menores y el número diferente es {b}."
    elif b == c:
        if b > a:
            return f"Los números {b} y {c} son mayores y el número diferente es {a}."
        else:
            return f"Los números {b} y {c} son menores y el número diferente es {a}."
    else:
        mayor = max(a, b, c)
        menor = min(a, b, c)
        medio = a + b + c - mayor - menor
        return f"Número mayor: {mayor}, Número del medio: {medio}, Número menor: {menor}"
    

if __name__ == "__main__":
    print("App para determinar el número mayor, medio y menor entre tres números enteros.")
    sw = True
    while sw:
        try:
            a = int(input("Ingrese el primer número entero: "))
            b = int(input("Ingrese el segundo número entero: "))
            c = int(input("Ingrese el tercer número entero: "))

            resultado = mayor_menor_medio(a, b, c)
            print(resultado)

        except ValueError:
            print("Entrada inválida. Por favor, ingrese números enteros.")
            continue

        continuar = input("¿Desea ingresar otros números? (s/n): ").strip().lower()
        if continuar != 's':
            sw = False
            print("Ha terminado la ejecución.")
    
