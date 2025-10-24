import json 
# Abrimos el archivo en modo lectura 
with open("data/datos.json", "r", encoding="utf-8") as archivo: 
    datos = json.load(archivo)  # Convertimos el JSON a un diccionario Python 
# Mostramos el contenido 
print("Nombre:", datos["nombre"]) 
print("Edad:", datos["edad"]) 
print("Hobbies:", ", ".join(datos["hobbies"])) 