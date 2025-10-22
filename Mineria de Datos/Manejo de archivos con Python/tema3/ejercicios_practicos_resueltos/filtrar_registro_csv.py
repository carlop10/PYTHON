# 3.10 — Ejercicio práctico (resuelto) 
# Ejercicio 1 — Filtrar registros de un CSV 
# Enunciado: 
# Dado el archivo data/people.csv, generar un nuevo archivo data/mayores.csv solo 
# con personas mayores de 25 años. 
# Solución: 
# filtrar_csv.py 
import csv 
from pathlib import Path 
 
entrada = Path("data/people.csv") 
salida = Path("data/mayores.csv") 
 
with entrada.open("r", encoding="utf-8", newline="") as f_in, \
    salida.open("w", encoding="utf-8", newline="") as f_out: 
 
    lector = csv.DictReader(f_in) 
    campos = lector.fieldnames 
    escritor = csv.DictWriter(f_out, fieldnames=campos) 
    escritor.writeheader() 
 
    for fila in lector: 
        if int(fila["age"]) > 25: 
            escritor.writerow(fila) 
 
print("Archivo filtrado creado:", salida)