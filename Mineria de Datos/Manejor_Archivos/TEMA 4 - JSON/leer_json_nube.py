import json 
import urllib.request 
 
# URL pública con datos JSON 
url = "https://jsonplaceholder.typicode.com/users" 
# Descargamos y leemos los datos desde la web 
with urllib.request.urlopen(url) as respuesta: 
    datos = json.load(respuesta) 
# Mostramos los primeros 2 usuarios 
for usuario in datos[:2]: 
    print(f"Nombre: {usuario['name']}") 
    print(f"Email: {usuario['email']}") 
    print("-" * 40)