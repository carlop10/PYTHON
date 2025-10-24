from pathlib import Path 
try: 
    with Path("data/no_existe.txt").open("r", encoding="utf-8") as f: 
        contenido = f.read() 
except FileNotFoundError: 
    print("❌ Archivo no encontrado.") 
except UnicodeDecodeError: 
    print(" ⚠ Error de codificación.")