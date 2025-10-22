# Escribir un pequeño CLI que acepte --list, --create-dir NOMBRE y --delete
# FILE usando argparse, integrando operaciones de pathlib.

import argparse
from pathlib import Path


def listar_archivos(directorio, recursivo=False):
    ruta = Path(directorio).resolve()
    if not ruta.is_dir():
        print(f"'{ruta}' no es un directorio válido.")
        return
    archivos = ruta.rglob("*") if recursivo else ruta.iterdir()
    for f in archivos:
        if f.is_file():
            print(f"{f.name} ({f.stat().st_size} bytes)")


def crear_directorio(nombre):
    ruta = Path(nombre).resolve()
    ruta.mkdir(parents=True, exist_ok=True)
    print(f"Directorio creado: {ruta}")


def eliminar_archivo(archivo):
    ruta = Path(archivo).resolve()
    if ruta.is_file():
        confirm = input(f"¿Eliminar '{ruta}'? [s/N]: ").lower()
        if confirm == "s":
            ruta.unlink()
            print("Archivo eliminado.")
    else:
        print("Ruta inválida.")


def main():
    parser = argparse.ArgumentParser(description="CLI de gestión de archivos.")
    parser.add_argument("--list", metavar="DIR", help="Listar archivos del directorio.")
    parser.add_argument(
        "--recursive", action="store_true", help="Listar recursivamente."
    )
    parser.add_argument("--create-dir", metavar="NOMBRE", help="Crear un directorio.")
    parser.add_argument("--delete", metavar="FILE", help="Eliminar un archivo.")
    args = parser.parse_args()

    if args.list:
        listar_archivos(args.list, args.recursive)
    if args.create_dir:
        crear_directorio(args.create_dir)
    if args.delete:
        eliminar_archivo(args.delete)
    if not (args.list or args.create_dir or args.delete):
        parser.print_help()


if __name__ == "__main__":
    main()
