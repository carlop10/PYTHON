# Crear un script que reciba por línea de comandos una ruta (argumento) y borre todos
# los archivos .tmp dentro de esa carpeta (y subcarpetas) que tengan más de 7 días
# de antigüedad. (Pistas: pathlib.rglob, stat().st_mtime, time.time()).

from pathlib import Path
import time

ruta = Path(input("Ingrese la ruta de la carpeta: "))
ahora = time.time()
n_dias_segundos = 7 * 24 * 60 * 60  # 7 días en segundos
segundos_prueba = 10  # para pruebas, usar 10 segundos
sw = True

while sw:
    print("La ruta completa es:", ruta.resolve())
    print("La ruta ingresada es correcta? (Sí/No)")
    respuesta = input().strip().lower()

    if respuesta == "no":
        ruta = Path(input("Ingrese la ruta de la carpeta nuevamente: "))
        tmp_files = ruta.rglob("*.tmp")

    else:
        # Verificar si hay archivos .tmp en la ruta proporcionada
        tmp_files = list(ruta.rglob("*.tmp"))
        if not tmp_files:
            print("No se encontraron archivos .tmp en la ruta proporcionada.")
        else:
            sw = False


print("\n--- archivos .tmp encontrados ---")
for archivo in tmp_files:
    print(archivo)

print("--> Esta seguro(a) que desea eliminar estos archivos? (Sí/No)")
confirmacion = input().strip().lower()

if confirmacion == "no":
    print("Operación cancelada por el usuario.")
    exit()
else:

    print("Iniciando eliminación de archivos .tmp con más de 7 días de antigüedad...")
    try:
        for archivo in ruta.rglob("*.tmp"):
            tiempo_modificacion = archivo.stat().st_mtime
            if (ahora - tiempo_modificacion) > segundos_prueba:
                archivo.unlink()
                print(f"--> Archivo [{archivo}] eliminado.")
        print("Eliminación completada.")
    except Exception as e:
        print(f"Ocurrió un error durante la eliminación: {e}")
