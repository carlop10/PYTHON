# ejemplo_with_lectura.py 
from pathlib import Path 
ruta = Path("data/ejemplo1.txt") 
with ruta.open("r", encoding="utf-8") as archivo: 
    contenido = archivo.read() 
print("Contenido del archivo:\n", contenido) 
# No es necesario llamar a archivo.close() 