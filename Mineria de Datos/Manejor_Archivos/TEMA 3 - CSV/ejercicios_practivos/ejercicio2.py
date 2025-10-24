# Generar un archivo data/precios_usd.csv a partir de un CSV con precios en 
# pesos colombianos, convirtiéndolos a USD (1 USD = 4000 COP)

import csv
from pathlib import Path

entrada = Path("data/precios_cop.csv")
salida = Path("data/precios_usd.csv")

with entrada.open("r", encoding="utf-8", newline="") as f_in, \
    salida.open("w", encoding="utf-8", newline="") as f_out:    
    lector = csv.DictReader(f_in)
    campos = lector.fieldnames + ["precio_usd"]
    escritor = csv.DictWriter(f_out, fieldnames=campos)
    escritor.writeheader()
    
    for fila in lector:
        precio_cop = float(fila["precio_cop"])
        precio_usd = round(precio_cop / 4000, 2) 
        fila["precio_usd"] = precio_usd 
        escritor.writerow(fila)
        
print("Archivo con precios en USD creado:", salida)

# Nota: Asegúrate de que el archivo data/precios_cop.csv exista con los datos
# apropiados antes de ejecutar este script.
