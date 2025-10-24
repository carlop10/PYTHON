from pathlib import Path

# 1) crear un objeto Path para el directorio actual
p = Path(".")  # Path('.') representa el directorio actual
print(p.resolve())  # ruta absoluta

# 2) construir rutas de forma segura (no usar concatenación manual)
data_dir = Path("data")  # carpeta 'data' en el directorio actual

file_path = data_dir / "archivo.txt"  # operador '/' para unir rutas
print(file_path)  # data/archivo.txt

# 3) comprobar existencia y tipo
if not data_dir.exists():
    print("La carpeta 'data' no existe.")
else:
    print("Existe y es:", "directorio" if data_dir.is_dir() else "archivo")

# 4) crear directorio (incluye padres si es necesario)
data_dir.mkdir(parents=True, exist_ok=True)

# 5) listar archivos con glob (por ejemplo todos .txt)
for txt in data_dir.glob("*.txt"):
    print("TXT:", txt.name)

# 6) renombrar/mover
old = data_dir / "viejo.txt"
nuevo = data_dir / "nuevo.txt"
if old.exists():
    old.rename(nuevo)  # si 'nuevo' está en otra carpeta, se mueve
