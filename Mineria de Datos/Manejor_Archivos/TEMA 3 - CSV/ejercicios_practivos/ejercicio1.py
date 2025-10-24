# Leer un archivo CSV remoto (por ejemplo, el de países) y mostrar solo las columnas 
# "Country Name" y "Region". 

import csv
from urllib.request import urlopen
import io

url = "https://raw.githubusercontent.com/google/dspl/master/samples/google/canonical/countries.csv"
with urlopen(url) as respuesta:
    # Convertir bytes a texto
    contenido = io.TextIOWrapper(respuesta, encoding="utf-8", newline="")
    lector = csv.DictReader(contenido)
    for i, fila in enumerate(lector):
        print(fila["Country Name"], "-", fila["Region"])
        if i >= 4:  # Mostrar solo primeras 5 filas
            break