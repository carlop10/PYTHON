# ejemplo_lineas.py 
with open("data/ejemplo1.txt", "r", encoding="utf-8") as f: 
    for linea in f: 
        print("Línea:", linea.strip())