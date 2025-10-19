# Ejercicio 2 (resuelto) — Listar archivos .csv en data/raw y mostrarlos ordenados por tamaño
# Solución:

from pathlib import Path

raw = Path("data/raw")

# obtener todos los archivos .csv en data/raw
csv_files = list(raw.glob("*.csv"))

# obtener lista de .csv en data/raw
csv_files_sorted = sorted(csv_files, key=lambda p: p.stat().st_size, reverse=True)
# ordenar por tamaño (mayor a menor)
for p in csv_files_sorted:
    print(p.name, p.stat().st_size, "bytes")

# Explicación: stat().st_size devuelve tamaño en bytes.
