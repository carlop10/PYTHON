#Ejemplo 4 — Leer las primeras N líneas 
with open("data/ejemplo1.txt", "r", encoding="utf-8") as f: 
    for i in range(1): 
        print(f.readline().strip()) 