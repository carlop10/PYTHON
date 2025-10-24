import json 
persona = { 
    "nombre": "Luis", 
    "edad": 28, 
    "profesion": "Ingeniero", 
    "lenguajes": ["Python", "C++", "Go"] 
} 
 
# Guardamos el diccionario en un archivo JSON 
with open("data/persona.json", "w", encoding="utf-8") as archivo: 
    json.dump(persona, archivo, indent=4, ensure_ascii=False) 
 
print("Archivo 'persona.json' creado correctamente.") 