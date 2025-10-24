#3.4 — Ignorar el encabezado 
import csv 
from pathlib import Path 
 
ruta = Path("data/people.csv") 
 
with ruta.open("r", encoding="utf-8", newline="") as f: 
    lector = csv.reader(f) 
    encabezado = next(lector)  # Saltar encabezado 
    print("Encabezado:", encabezado) 
    for fila in lector: 
        print(fila)