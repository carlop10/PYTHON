'''
Crea un programa que: 
1. Lea un archivo XML de productos (productos.xml) con nombre, precio y cantidad. 
2. Lea una configuración (config.ini) que indique la tasa de IVA (por ejemplo, 0.19). 
3. Calcule el precio final con IVA y genere un nuevo archivo productos_actualizados.xml con ese valor adicional.
'''

import configparser
import xml.etree.ElementTree as ET
# Leer configuración
config = configparser.ConfigParser()
config.read("data/config.ini")
tasa_iva = config["impuestos"].getfloat("tasa_iva")
# Leer XML
arbol = ET.parse("data/productos.xml")
raiz = arbol.getroot()
# Procesar productos y calcular precio con IVA
for prod in raiz.findall("producto"):
    precio = float(prod.find("precio").text)
    precio_con_iva = precio * (1 + tasa_iva)
    prod.set("precio_con_iva", f"{precio_con_iva:.2f}")
# Guardar nuevo XML
arbol.write("data/productos_actualizados.xml", encoding="utf-8", xml_declaration=True)
print("Archivo 'productos_actualizados.xml' creado correctamente.")

