# Escribir un programa que lea un archivo remoto (por URL), cuente las líneas y las 
# guarde localmente en data/copias/archivo_remoto.txt. 

from pathlib import Path
import requests

url = "https://data.iana.org/TLD/tlds-alpha-by-domain.txt"
response = requests.get(url)
ruta_local = Path("data/copias/archivo_remoto.txt")
ruta_local.parent.mkdir(parents=True, exist_ok=True)
with ruta_local.open("w", encoding="utf-8") as f:
    f.write(response.text)
lineas = response.text.count("\n") + 1
print(f"El archivo remoto tiene {lineas} líneas y se ha guardado en '{ruta_local}'.")

