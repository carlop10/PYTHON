#Ejemplo 1 — Leer un CSV línea a línea 
# leer_csv_basico.py 
import csv 
from pathlib import Path 
ruta = Path("data/people.csv") 
 
with ruta.open("r", encoding="utf-8", newline="") as f: 
    lector = csv.reader(f) 
    for fila in lector: 
        print(fila) 