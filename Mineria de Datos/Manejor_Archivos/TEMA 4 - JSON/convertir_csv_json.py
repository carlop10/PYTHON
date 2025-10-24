import csv 
import json 
with open("data/empleados.csv", "r", encoding="utf-8") as archivo_csv: 
    lector = csv.DictReader(archivo_csv) 
    lista_empleados = list(lector) 
 
# Guardar en formato JSON 
with open("data/empleados.json", "w", encoding="utf-8") as archivo_json: 
    json.dump(lista_empleados, archivo_json, indent=4, ensure_ascii=False)