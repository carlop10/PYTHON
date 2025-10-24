import urllib.request
import xml.etree.ElementTree as ET

url = "https://www.w3schools.com/xml/simple.xml"
with urllib.request.urlopen(url) as respuesta:
    datos_xml = respuesta.read()

# Convertimos el contenido en árbol
raiz = ET.fromstring(datos_xml)

# Mostrar platos y precios
for plato in raiz.findall("food"):
    nombre = plato.find("name").text
    precio = plato.find("price").text
    print(f" 🍽 {nombre} cuesta {precio}")
