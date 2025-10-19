# Implementar un script que haga backup incremental: copie solo archivos nuevos o
# modificados desde data/raw a backup/raw (preservando estructura de
# subcarpetas). Comparar por tamaño y mtime.

from pathlib import Path
import shutil
import time

origen = Path("data/raw")
destino = Path("backup/raw")

# Crear la carpeta de destino si no existe
destino.mkdir(parents=True, exist_ok=True)

ahora = time.time()
una_hora_segundos = 1 * 60 * 60  # 1 hora en segundos

for archivo_origen in origen.rglob("*"):
    if archivo_origen.is_file():
        if archivo_origen.stat().st_size < una_hora_segundos:
            archivo_destino = destino / archivo_origen.relative_to(origen)

            # Verificar si el archivo ya existe en el destino
            if archivo_destino.exists():
                tamaño_origen = archivo_origen.stat().st_size
                tamaño_destino = archivo_destino.stat().st_size
                mtime_origen = archivo_origen.stat().st_mtime
                mtime_destino = archivo_destino.stat().st_mtime

                # Comparar tamaño y tiempo de modificación
                if (
                    tamaño_origen != tamaño_destino
                    or abs(mtime_origen - mtime_destino) > una_hora_segundos
                ):
                    # Copiar archivo modificado
                    try:
                        shutil.copy2(archivo_origen, archivo_destino)
                        print(
                            f"Archivo modificado copiado: {archivo_origen} -> {archivo_destino}"
                        )
                    except Exception as e:
                        print(
                            f"Error al copiar {archivo_origen} a {archivo_destino}: {e}"
                        )
                else:
                    print(f"Archivo sin cambios: {archivo_origen}")
            else:
                # Copiar archivo nuevo
                archivo_destino.parent.mkdir(
                    parents=True, exist_ok=True
                )  # Asegurar que la carpeta exista
                try:
                    shutil.copy2(archivo_origen, archivo_destino)
                    print(
                        f"Archivo nuevo copiado: {archivo_origen} -> {archivo_destino}"
                    )
                except Exception as e:
                    print(f"Error al copiar {archivo_origen} a {archivo_destino}: {e}")
        else:
            print(f"Archivo {archivo_origen} excede el tamaño límite, no se copia.")

    elif archivo_origen.is_dir():
        if archivo_origen.stat().st_size < una_hora_segundos:
            try:
                carpeta_destino = destino / archivo_origen.relative_to(origen)
                carpeta_destino.mkdir(parents=True, exist_ok=True)
            except Exception as e:
                print(f"Error al crear carpeta {carpeta_destino}: {e}")
        else:
            print(f"Carpeta {archivo_origen} excede el tamaño límite, no se crea.")

    else:
        continue  # Saltar si no es archivo ni carpeta
