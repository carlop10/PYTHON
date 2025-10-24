# Escribir un programa que lea un CSV y lo exporte en formato JSON (usando el 
# módulo json del siguiente tema).

import csv
import json
from pathlib import Path

entrada = Path("data/precios_cop.csv")
salida = Path("data/precios_cop.json") 
datos = []
with entrada.open("r", encoding="utf-8", newline="") as f_in:
    lector = csv.DictReader(f_in)
    for fila in lector:
        datos.append(fila)
with salida.open("w", encoding="utf-8") as f_out:
    json.dump(datos, f_out, indent=4, ensure_ascii=False)
    
print("Archivo JSON creado:", salida)

