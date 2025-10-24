"""
    Enunciado:
    Descarga los datos de usuarios desde
    https://jsonplaceholder.typicode.com/users
    genera un archivo contactos.json que contenga únicamente el nombre, correo y
    ciudad de cada usuario.
    Luego, convierte ese archivo JSON a un CSV llamado contactos.csv.
"""

import json
import urllib.request
import csv

# Descargar datos
url = "https://jsonplaceholder.typicode.com/users"
with urllib.request.urlopen(url) as respuesta:
    usuarios = json.load(respuesta)
# Filtrar datos necesarios
contactos = [
    {
        "nombre": usuario["name"],
        "correo": usuario["email"],
        "ciudad": usuario["address"]["city"]
    }
    for usuario in usuarios
]
# Guardar en archivo JSON
with open("data/contactos.json", "w", encoding="utf-8") as archivo:
    json.dump(contactos, archivo, indent=4, ensure_ascii=False)
# Convertir JSON a CSV

with open("data/contactos.json", "r", encoding="utf-8") as archivo_json:
    datos_contactos = json.load(archivo_json)
with open("data/contactos.csv", "w", encoding="utf-8", newline='') as archivo_csv:
    campos = ["nombre", "correo", "ciudad"]
    escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(datos_contactos)
    
print("Se han creado 'contactos.json' y 'contactos.csv' con los datos filtrados.")