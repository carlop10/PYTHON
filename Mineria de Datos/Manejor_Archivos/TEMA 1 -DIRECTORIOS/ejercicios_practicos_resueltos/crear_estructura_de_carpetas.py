# Ejercicio 1 (resuelto) — Crear estructura de carpetas
# Enunciado: Crear la siguiente estructura dentro de la carpeta actual: data/raw,
# data/processed, logs. Si ya existen, no lanzar error.
# Solución:

from pathlib import Path

# definir las rutas de las carpetas a crear
dirs = [Path("data/raw"), Path("data/processed"), Path("logs")]

# crear las carpetas
for d in dirs:
    d.mkdir(parents=True, exist_ok=True)

print("Estructura creada (o ya existía).")

# Explicación: parents=True crea los padres si faltan; exist_ok=True evita excepción si ya existe.
