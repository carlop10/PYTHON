"""Enunciado:
Lee un archivo JSON desde una URL pública
(https://jsonplaceholder.typicode.com/todos)
y guarda en un archivo local solo las tareas completadas (completed: true).
Solución:"""

import json
import urllib.request

url = "https://jsonplaceholder.typicode.com/todos"
# Descargar datos
with urllib.request.urlopen(url) as respuesta:
    tareas = json.load(respuesta)
# Filtrar las completadas
completadas = [t for t in tareas if t["completed"]]
# Guardar en archivo local
with open("data/tareas_completadas.json", "w", encoding="utf-8") as archivo:
    json.dump(completadas, archivo, indent=4, ensure_ascii=False)

print("Se han guardado las tareas completadas en 'tareas_completadas.json'")
