# Crear un script que recorra todos los archivos .txt en una carpeta y cuente cuántas 
# veces aparece una palabra clave en total. (Usar pathlib y lectura línea a línea). 

from pathlib import Path
carpeta = Path("data")
palabra_clave = "ejemplo"
contador_total = 0

for archivo in carpeta.glob("*.txt"):
    with archivo.open("r", encoding="utf-8") as f:
        for linea in f:
            contador_total += linea.lower().count(palabra_clave.lower())
            
print(f"La palabra '{palabra_clave}' aparece {contador_total} veces en total en los archivos .txt de la carpeta '{carpeta}'.")

