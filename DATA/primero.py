print("Hola mundo")

dato1:int = 10
dato2:int = 20

suma:int = dato1 + dato2
print("La suma es:", suma)


#for de una sola linea
numerosCuadrados = [x**2 for x in range(10)]
print(numerosCuadrados)

#for de una sola linea para extraer los numeros pares
numerosPares = [x for x in range(10) if x % 2 == 0]
print(numerosPares)