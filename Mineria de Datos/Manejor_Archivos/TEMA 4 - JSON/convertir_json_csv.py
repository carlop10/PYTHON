import csv 
import json 
 
with open("data/empleados2.json", "r", encoding="utf-8") as archivo_json: 
    datos = json.load(archivo_json) 
 
# Convertimos JSON a CSV 
with open("data/empleados2.csv", "w", newline="", 
encoding="utf-8") as archivo_csv: 
    campos = datos[0].keys()  # Obtener encabezados 
    escritor = csv.DictWriter(archivo_csv, fieldnames=campos) 
    escritor.writeheader() 
    escritor.writerows(datos)