import csv 
import json 
import urllib.request 

# ========================== 
# 1. Leer archivo TXT 
# ========================== 

empleados_txt = [] 
with open("data/empleados.txt", "r", encoding="utf-8") as archivo_txt: 
    for linea in archivo_txt: 
        nombre, correo = linea.strip().split(",") 
        empleados_txt.append({"nombre": nombre.strip(), "correo": 
        correo.strip()}) 
 
print(" ✅ Datos TXT cargados:", empleados_txt, "\n") 
 
# ========================== 
# 2. Leer archivo CSV 
# ========================== 

empleados_csv = [] 
with open("data/info_empleados.csv", "r", encoding="utf-8") as archivo_csv: 
    lector = csv.DictReader(archivo_csv) 
    for fila in lector: 
        empleados_csv.append(fila) 
 
print(" ✅ Datos CSV cargados:", empleados_csv, "\n") 
 
# ========================== 
# 3. Leer datos JSON desde la nube 
# ========================== 

url = "https://jsonplaceholder.typicode.com/users" 
with urllib.request.urlopen(url) as respuesta: 
    datos_nube = json.load(respuesta) 
 
# Creamos un diccionario {nombre: ciudad} 
ciudades_remotas = {usuario["name"]: usuario["address"]["city"] for usuario in datos_nube} 
 
# ========================== 
# 4. Combinar toda la información 
# ========================== 

empleados_completos = [] 
for txt_emp in empleados_txt: 
    nombre = txt_emp["nombre"] 
     
    # Buscar info adicional en CSV 
    info_csv = next((emp for emp in empleados_csv if emp["nombre"] == nombre), None) 
     
    # Buscar ciudad en la nube (si existe) 
    ciudad = ciudades_remotas.get(nombre, "Desconocida") 


    if info_csv: 
        emp_final = { 
            "nombre": nombre, 
            "correo": txt_emp["correo"], 
            "edad": int(info_csv["edad"]), 
            "cargo": info_csv["cargo"], 
            "salario": float(info_csv["salario"]), 
            "ciudad": ciudad, 
            "activo": True 
        } 
        empleados_completos.append(emp_final) 
 
print(" ✅ Datos combinados:") 
for e in empleados_completos: 
    print(e) 
    print() 
 
# ========================== 
# 5. Guardar resultado en JSON 
# ========================== 

with open("data/empleados_completo.json", "w", encoding="utf-8") as archivo_json: 
    json.dump(empleados_completos, archivo_json, indent=4, ensure_ascii=False) 
 
print(" 💾 Archivo 'empleados_completo.json' generado correctamente.\n") 
 
# ========================== 
# 6. Estadísticas básicas 
# ========================== 

salarios = [emp["salario"] for emp in empleados_completos] 
promedio_salario = sum(salarios) / len(salarios) 
 
print(f" 📊 Número total de empleados: {len(empleados_completos)}") 
print(f" 💰 Promedio de salario: {promedio_salario:.2f}") 
print(f" 🏙 Ciudades registradas: {', '.join(set(e['ciudad'] for e in empleados_completos))}") 