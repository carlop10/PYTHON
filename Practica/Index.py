import datetime

""" Calcular edad

date = datetime.datetime.now()

dia_usu = int(input("Ingrese su dia de nacimiento: "))
mes_usu = int(input("Ingrese su mes de nacimiento: "))
año_usu = int(input("Ingrese su año de nacimiento: "))

print("Su edad actual es: ", date.year - año_usu, date.month - mes_usu, date.day - dia)}

"""

""" Par o impar

numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("El número es par")
else:
    print("El número es impar")

"""

""" tabla de multiplicar

numero = int(input("Ingrese un número: "))

for i in range (11):
    print(numero, " x ", i, " = ", numero*i)
    
"""

""" contador de vocales

palabra = input("Ingrese una palabra: ")
palabra.lower()
contador = 0

for i in palabra:
    if (i == 'a' or i == 'e' or i == 'i' or i == 'o' or i == 'u'):
        contador = contador + 1

print("La palabra ",palabra," contiene: ", contador, " vocales.")

""" 

""" adivina el número

numero_azar = 5

switch = True

while switch:
    numero = int(input("Ingrese un número entre 1 y 10: "))
    if numero == numero_azar:
        print("¡Felicidades! Adivinaste el número.")
        switch = False
    else:
        if numero < numero_azar:
            print("El número es muy bajo.")
        else:
            print("El número es muy alto.")

"""

""" Ingresar números y almacenarlos en una lista

lista = []

for i in range(5):
    numero = int(input("Ingrese un número: "))
    lista.append(numero)

print("Los números ingresados son:", lista)

""" 
""" Diccionario de contacto

listado = []

sw = 0

while sw == 0:

    nombre = input("Ingrese su nombre: ")
    telefono = input("Ingrese su teléfono: ")
    correo = input("Ingrese su correo: ")

    listado.append({"nombre": nombre, "telefono": telefono, "correo": correo})

    continuar = input("¿Desea ingresar otro contacto? (s/n): ")
    if continuar.lower() != "s":
        sw = 1

print("Listado de contactos:")
for contacto in listado:
    print("Nombre:", contacto["nombre"])
    print("Teléfono:", contacto["telefono"])
    print("Correo:", contacto["correo"])
    print("-------------------------")

"""

""" Encontrar el número mayor en una lista
lista = []
mayor = 0

for i in range(5):
    numero = int(input("Ingrese un número: "))
    lista.append(numero)
    if numero > mayor:
        mayor = numero

print("El número mayor es:", mayor)

"""

# FUNCIONES

""" Calcular área de un triángulo

def calcular_area_triangulo(base, altura):
    return (base * altura) / 2


base = int(input("Ingrese la base del triángulo: "))
altura = int(input("Ingrese la altura del triángulo: "))

area = calcular_area_triangulo(base, altura)

print("El área del triángulo es:", area)

"""

