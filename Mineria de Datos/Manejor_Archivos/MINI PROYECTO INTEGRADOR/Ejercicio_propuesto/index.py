# https://fakestoreapi.com/products
# generar un .txt que contiene los nombres y códigos de los productos. 
# generar un .csv que contiene precios y existencias
# El JSON remoto (usa https://fakestoreapi.com/products) se usa para agregar las categorías. 
# El resultado final debe guardarse en data/productos_completo.json con estadísticas del inventario. 
'''
Ejemplo de un producto en el JSON remoto:
{
    "id": 1,
    "title": "Fjallraven - Foldsack No. 1 Backpack, Fits 15 Laptops",
    "price": 109.95,
    "description": "Your perfect pack for everyday use and walks in the forest. Stash your laptop (up to 15 inches) in the padded sleeve, your everyday",
    "category": "men's clothing",
    "image": "https://fakestoreapi.com/img/81fPKd-2AYL._AC_SL1500_t.png",
    "rating": {"rate": 3.9, "count": 120},
}
'''

import json
import csv
import urllib.request

# ==========================
# 1. Crear archivo TXT con nombres y códigos
# ==========================

productos_txt = []
url = "https://fakestoreapi.com/products"
with urllib.request.urlopen(url) as respuesta:
    productos = json.load(respuesta)
for producto in productos:
    productos_txt.append(f"{producto['title']}, {producto['id']}\n")
with open("data/productos.txt", "w", encoding="utf-8") as archivo_txt:
    archivo_txt.writelines(productos_txt)
print(" 💾 Archivo 'productos.txt' generado correctamente.\n")

# ==========================
# 2. Crear archivo CSV con precios y existencias
# ==========================

with open("data/productos.csv", "w", encoding="utf-8", newline='') as archivo_csv:
    campos = ["id", "price", "stock"]
    escritor = csv.DictWriter(archivo_csv, fieldnames=campos)
    escritor.writeheader()
    for producto in productos:
        escritor.writerow({
            "id": producto["id"],
            "price": producto["price"],
            "stock": producto["rating"]["count"]
        })
print(" 💾 Archivo 'productos.csv' generado correctamente.\n")

# ==========================
# 3. Leer datos JSON desde la nube
# ==========================

url = "https://fakestoreapi.com/products"
with urllib.request.urlopen(url) as respuesta:
    datos_nube = json.load(respuesta)
# Creamos un diccionario {id: categoría}
categorias_remotas = {producto["id"]: producto["category"] for producto in datos_nube}

# ==========================
# 4. Combinar toda la información
# ==========================

productos_completos = []
for producto in productos:
    prod_final = {
        "id": producto["id"],
        "nombre": producto["title"],
        "precio": producto["price"],
        "stock": producto["rating"]["count"],
        "categoria": categorias_remotas.get(producto["id"], "Desconocida")
    }
    productos_completos.append(prod_final)
# Guardar en archivo JSON
with open("data/productos_completo.json", "w", encoding="utf-8") as archivo_json:
    json.dump(productos_completos, archivo_json, indent=4, ensure_ascii=False)
print(" 💾 Archivo 'productos_completo.json' generado correctamente.\n")

# ==========================
# 5. Estadísticas básicas
# ==========================

total_stock = sum(p["stock"] for p in productos_completos)
valor_inventario = sum(p["precio"] * p["stock"] for p in productos_completos)
promedio_precio = sum(p["precio"] for p in productos_completos) / len(productos_completos)
print(f" 📊 Número total de productos: {len(productos_completos)}")
print(f" 📦 Stock total: {total_stock}")
print(f" 💰 Valor total del inventario: {valor_inventario:.2f}")
print(f" 🛒 Precio promedio por producto: {promedio_precio:.2f}")
print(f" 🛍 Categorías registradas: {', '.join(set(p['categoria'] for p in productos_completos))}")
