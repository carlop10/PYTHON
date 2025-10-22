# 3.11 — Ejercicio práctico (resuelto) 
# Ejercicio 2 — Calcular promedio de edad 
# Enunciado: 
# Calcular la edad promedio de todas las personas en data/people.csv. 
# Solución: 
# promedio_edad.py 
import csv 
 
with open("data/people.csv", "r", encoding="utf-8", newline="") as f: 
    lector = csv.DictReader(f) 
    edades = [int(fila["age"]) for fila in lector] 
 
promedio = sum(edades) / len(edades) 
print("Edad promedio:", round(promedio, 2))