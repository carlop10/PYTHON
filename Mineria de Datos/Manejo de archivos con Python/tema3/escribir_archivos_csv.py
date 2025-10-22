#3.6 — Escribir archivos CSV 
#Ejemplo 3 — Escribir con csv.writer 
# escribir_csv.py 
import csv 
from pathlib import Path 
 
ruta = Path("data/nuevo.csv") 
 
filas = [ 
    ["id", "producto", "precio"], 
    [1, "Teclado", 120000], 
    [2, "Mouse", 80000], 
    [3, "Monitor", 600000] 
] 
 
with ruta.open("w", encoding="utf-8", newline="") as f: 
    escritor = csv.writer(f) 
    escritor.writerows(filas) 
 
print("Archivo creado:", ruta)