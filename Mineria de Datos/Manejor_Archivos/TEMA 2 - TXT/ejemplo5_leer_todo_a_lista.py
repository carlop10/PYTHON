#Ejemplo 5 — Leer todo a lista 
with open("data/ejemplo1.txt", "r", encoding="utf-8") as f: 
    lineas = f.readlines() 
 
print("Total de líneas:", len(lineas)) 
print(lineas)