import csv 
import json 
import configparser
import xml.etree.ElementTree as ET 
 
# --- INICIO DE EXTRACCIÓN --- 
ventas = [] 
 
with open("data/ventas_1.csv", newline='', encoding='utf-8') as csvfile: 
    lector = csv.DictReader(csvfile) 
    for fila in lector: 
        ventas.append({ 
            "id": int(fila["id"]), 
            "producto": fila["producto"], 
            "cantidad": int(fila["cantidad"]), 
            "precio": float(fila["precio"]) 
        }) 
 
# --- EXTRACCIÓN DE JSON --- 
with open("data/ventas_2.json", encoding='utf-8') as jsonfile: 
    data_json = json.load(jsonfile) 
    for item in data_json: 
        ventas.append(item) 
 
# --- EXTRACCIÓN DE TXT --- 
with open("data/ventas_3.txt", encoding='utf-8') as txtfile: 
    next(txtfile)  # Saltar encabezado 
    for linea in txtfile: 
        id, producto, cantidad, precio = linea.strip().split(",") 
        ventas.append({ 
            "id": int(id), 
            "producto": producto, 
            "cantidad": int(cantidad), 
            "precio": float(precio) 
        }) 
 
print(" ✅ Datos extraídos correctamente:") 
for v in ventas: 
    print(v)
    
    
# --- FIN DE EXTRACCIÓN ---

# --- INICIO DE TRANSFORMACIÓN ---

config = configparser.ConfigParser() 
config.read("data/config.ini") 
iva = float(config["general"]["iva"]) 
moneda = config["general"]["moneda"] 
# Agregamos total con IVA 
for venta in ventas: 
    subtotal = venta["cantidad"] * venta["precio"] 
    total = subtotal * (1 + iva) 
    venta["total"] = round(total, 2) 
    venta["moneda"] = moneda 
print("\n ✅ Datos transformados:") 
for v in ventas: 
    print(v)
    
# --- FIN DE TRANSFORMACIÓN ---

# --- INICIO DE CARGA ---

# Crear raíz 
root = ET.Element("ventas") 
for venta in ventas: 
    nodo = ET.SubElement(root, "venta", id=str(venta["id"])) 
    ET.SubElement(nodo, "producto").text = venta["producto"] 
    ET.SubElement(nodo, "cantidad").text = str(venta["cantidad"]) 
    ET.SubElement(nodo, "precio").text = str(venta["precio"]) 
    ET.SubElement(nodo, "total").text = str(venta["total"]) 
    ET.SubElement(nodo, "moneda").text = venta["moneda"] 
 
# Guardar en archivo XML 
arbol = ET.ElementTree(root) 
arbol.write("data/ventas_finales.xml", encoding="utf-8", 
xml_declaration=True) 
 
print("\n ✅ Archivo 'ventas_finales.xml' generado con éxito.")

# -- FIN DE CARGA ---

# VALIDACION + GENERAR CSV

# Filtrar 
ventas_filtradas = [v for v in ventas if v["precio"] >= 10000] 
with open("ventas_filtradas.csv", "w", newline='', encoding="utf-8") as file: 
    campos = ["id", "producto", "cantidad", "precio", "total", "moneda"] 
    writer = csv.DictWriter(file, fieldnames=campos) 
    writer.writeheader() 
    writer.writerows(ventas_filtradas) 
print(" ✅ Archivo 'ventas_filtradas.csv' generado correctamente.")