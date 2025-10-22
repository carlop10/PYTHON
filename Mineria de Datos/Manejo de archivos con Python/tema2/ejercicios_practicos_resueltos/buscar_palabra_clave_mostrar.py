
#Ejercicio 2 — Buscar palabra clave y mostrar línea 
#Enunciado: Buscar una palabra dada y mostrar las líneas donde aparece. 
#Solución: 
# buscar_palabra.py 

palabra = "Python" 
with open("data/ejemplo1.txt", "r", encoding="utf-8") as f: 
    for num, linea in enumerate(f, start=1): 
        if palabra.lower() in linea.lower(): 
            print(f"[Línea {num}] {linea.strip()}") 