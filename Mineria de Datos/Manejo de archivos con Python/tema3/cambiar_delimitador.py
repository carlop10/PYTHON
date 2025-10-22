#3.8 — Separadores personalizados 
#No todos los CSV usan ,. Algunos usan ; o |. 

#Ejemplo 5 — Cambiar el delimitador 
import csv 
from pathlib import Path 
 
ruta = Path("data/paises.csv") 
 
with ruta.open("w", encoding="utf-8", newline="") as f: 
    escritor = csv.writer(f, delimiter=";") 
    escritor.writerow(["pais", "poblacion"]) 
    escritor.writerow(["Colombia", "52 millones"]) 
    escritor.writerow(["Peru", "33 millones"]) 
    escritor.writerow(["Chile", "19 millones"])