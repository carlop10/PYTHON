# 3.5 — Leer con DictReader (modo diccionario) 
# Más legible cuando trabajas con columnas por nombre. 
# Ejemplo 2 — Uso de csv.DictReader 
# dict_reader.py 
import csv 
from pathlib import Path 
 
ruta = Path("data/people.csv") 
 
with ruta.open("r", encoding="utf-8", newline="") as f: 
    lector = csv.DictReader(f) 
    for fila in lector: 
        print(fila["name"], "tiene", fila["age"], "años y vive en", 
fila["city"])