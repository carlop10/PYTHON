import json
from pathlib import Path
import configparser
from datetime import datetime
from src.logger_config import configurar_logger

class GenerarReporte:
    def __init__(self, path: Path, corte: str):
        self.path = path
        self.corte = corte
        self.config = self._leer_config()
        self.logger = configurar_logger("UnificarNotas", path / "logs")
        self.logger.info(f"Iniciando proceso de unificación para {corte}")

    def _leer_config(self):
        config_path = self.path / "config.ini"
        if not config_path.exists():
            raise FileNotFoundError(f"No se encontró el archivo de configuración: {config_path}")
        config = configparser.ConfigParser()
        config.read(config_path, encoding="utf-8")
        return config

    def generar(self, archivo_json: Path):
        if not archivo_json.exists():
            self.logger.error(f"No existe el archivo {archivo_json}")
            return

        try:
            with open(archivo_json, "r", encoding="utf-8") as f:
                estudiantes = json.load(f)
        except Exception as e:
            self.logger.error(f"Error leyendo JSON: {e}")
            return 

        equivalencia_total = float(self.config["equivalencias_notas"][self.corte])
        umbral = equivalencia_total * 0.5

        fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        reporte_path = self.path / f"reporte_bajo_rendimiento_{self.corte}.txt"

        try:
            with open(reporte_path, "w", encoding="utf-8") as reporte:
                reporte.write(f"REPORTE DE BAJO RENDIMIENTO - {self.corte.upper()}\n")
                reporte.write(f"Fecha de generación: {fecha_actual}\n")
                reporte.write(f"Umbral de equivalencia: {umbral}\n")
                reporte.write("="*60 + "\n\n")

                for e in estudiantes:
                    if e["promedio_general"] < umbral:
                        reporte.write(f"Nombre: {e['nombres']} | Código: {e['codigo']}\n")
                        for asignatura, nota in e["notas"].items():
                            reporte.write(f"  - {asignatura}: {nota}\n")
                        reporte.write(f"Promedio: {e['promedio_corte']} | Equivalencia: {e['promedio_general']}\n")
                        reporte.write("-"*40 + "\n")
            self.logger.info(f"Reporte generado: {reporte_path}")
        except Exception as e:
            self.logger.error(f"Error al escribir el reporte: {e}")
