# 3.9 — Leer un CSV remoto (desde la nube) 
# Podemos acceder a archivos CSV públicos mediante URL sin necesidad de descargar 
# manualmente. 
# Ejemplo 6 — Leer CSV remoto con urllib 
# csv_remoto.py 
import csv 
from urllib.request import urlopen 
import io 
 
url = "https://raw.githubusercontent.com/google/dspl/master/samples/google/canonical/countries.csv" 
 
with urlopen(url) as respuesta: 
    # Convertir bytes a texto 
    contenido = io.TextIOWrapper(respuesta, encoding="utf-8", newline="") 
    lector = csv.reader(contenido) 
    for i, fila in enumerate(lector): 
        print(fila) 
        if i >= 4:  # Mostrar solo primeras 5 filas 
            break 
 

# Aquí usamos io.TextIOWrapper para envolver el flujo binario y poder leerlo como texto. 