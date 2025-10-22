#Ejercicio 1 — Contar líneas, palabras y caracteres 
#Enunciado: Dado un archivo de texto, contar cuántas líneas, palabras y caracteres tiene. 
#Solución: 
# contar_texto.py 

ruta = "data/ejemplo1.txt" 
lineas = palabras = caracteres = 0 
 
with open(ruta, "r", encoding="utf-8") as f: 
    for linea in f: 
        lineas += 1 
        palabras += len(linea.split()) 
        caracteres += len(linea) 
        
print(f"Líneas: {lineas}, Palabras: {palabras}, Caracteres: {caracteres}") 