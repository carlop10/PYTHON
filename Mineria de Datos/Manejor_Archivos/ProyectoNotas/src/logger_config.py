import logging
from pathlib import Path

def configurar_logger(nombre: str, path_logs: Path) -> logging.Logger:
    """
    Configura y devuelve un logger con formato estándar.
    """

    # Crear carpeta de logs si no existe
    path_logs.mkdir(parents=True, exist_ok=True)
    ruta_log = path_logs / "app.log"

    logger = logging.getLogger(nombre)
    logger.setLevel(logging.INFO)  # Cambiar a DEBUG para más detalle

    # Evitar duplicados si ya existe un handler
    if not logger.handlers:
        formato = logging.Formatter(
            fmt="%(asctime)s - [%(levelname)s] - %(name)s: %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        # Archivo
        fh = logging.FileHandler(ruta_log, encoding="utf-8")
        fh.setFormatter(formato)

        # Consola
        ch = logging.StreamHandler()
        ch.setFormatter(formato)

        logger.addHandler(fh)
        logger.addHandler(ch)

    return logger
