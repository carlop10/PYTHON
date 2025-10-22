
#Ejemplo 6 — Crear y escribir desde cero 
# ejemplo_escritura.py 
with open("data/salida.txt", "w", encoding="utf-8") as f: 
    f.write("Hola Mundo 2\n") 
f.write("Este archivo fue creado por Python.\n")