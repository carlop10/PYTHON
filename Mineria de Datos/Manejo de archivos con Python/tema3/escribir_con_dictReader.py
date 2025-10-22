# 3.7 — Escribir con DictWriter (modo diccionario) 
# Ejemplo 4 — Crear CSV con encabezados automáticos 
# dict_writer.py 
import csv 
from pathlib import Path 
 
ruta = Path("data/ventas.csv") 
 
productos = [ 
    {"id": 1, "producto": "Laptop", "precio": 3500000}, 
    {"id": 2, "producto": "Tablet", "precio": 1500000}, 
    {"id": 3, "producto": "Celular", "precio": 2200000} 
] 
 
with ruta.open("w", encoding="utf-8", newline="") as f: 
    campos = ["id", "producto", "precio"] 
    escritor = csv.DictWriter(f, fieldnames=campos) 
    escritor.writeheader()        # Escribir encabezado 
    escritor.writerows(productos) # Escribir filas 