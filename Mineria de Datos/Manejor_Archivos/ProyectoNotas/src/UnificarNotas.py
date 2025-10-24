import json
import csv
import xml.etree.ElementTree as ET
from pathlib import Path
import configparser
from src.logger_config import configurar_logger

class UnificarNotas:
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

    def _leer_txt(self, ruta: Path):
        try:
            notas = []
            with open(ruta, "r", encoding="utf-8") as f:
                next(f)
                for linea in f:
                    partes = linea.strip().split(" ")
                    if len(partes) >= 6:
                        codigo, nombres, correo, celular, inasistencias, nota = partes[:6]
                        notas.append({
                            "codigo": codigo,
                            "nombres": nombres,
                            "correo": correo,
                            "celular": celular,
                            "inasistencias": int(inasistencias),
                            "nota": float(nota)
                        })
            self.logger.info(f"TXT leído: {ruta.name} ({len(notas)} registros)")
            return notas
        except Exception as e:
            self.logger.error(f"Error leyendo TXT {ruta.name}: {e}")
            return []

    def _leer_csv(self, ruta: Path):
        notas = []
        try:
            with open(ruta, "r", encoding="utf-8") as archivo:
                lector = csv.DictReader(archivo)
                for fila in lector:
                    fila["inasistencias"] = int(fila["inasistencias"])
                    fila["nota"] = float(fila["nota"])
                    notas.append(fila)
            self.logger.info(f"CSV leído: {ruta.name} ({len(notas)} registros)")
            return notas
        except Exception as e:
            self.logger.error(f"Error leyendo CSV {ruta.name}: {e}")
            return []

    def _leer_xml(self, ruta: Path):
        notas = []
        try:
            tree = ET.parse(ruta)
            root = tree.getroot()
            for estudiante in root.findall("estudiante"):
                notas.append({
                    "codigo": estudiante.find("codigo").text,
                    "nombres": estudiante.find("nombres").text,
                    "correo": estudiante.find("correo").text,
                    "celular": estudiante.find("celular").text,
                    "inasistencias": int(estudiante.find("inasistencias").text),
                    "nota": float(estudiante.find("nota").text)
                })
            self.logger.info(f"XML leído: {ruta.name} ({len(notas)} registros)")
            return notas
        except Exception as e:
            self.logger.error(f"Error leyendo XML {ruta.name}: {e}")
            return []

    def _calcular_equivalencia(self, promedio):
        equivalencia = float(self.config["equivalencias_notas"][self.corte])
        return round(promedio * (equivalencia / 5), 2)

    def main(self):
        notas_por_asignatura = {}
        for archivo in self.path.glob("asignatura_*.*"):
            ext = archivo.suffix.lower()
            nombre_asignatura = archivo.stem.replace("asignatura_", "")
            if ext == ".txt":
                notas = self._leer_txt(archivo)
            elif ext == ".csv":
                notas = self._leer_csv(archivo)
            elif ext == ".xml":
                notas = self._leer_xml(archivo)
            else:
                continue
            notas_por_asignatura[nombre_asignatura] = notas

        estudiantes = {}
        for asignatura, lista_notas in notas_por_asignatura.items():
            for n in lista_notas:
                codigo = n["codigo"]
                if codigo not in estudiantes:
                    estudiantes[codigo] = {
                        "codigo": codigo,
                        "nombres": n["nombres"],
                        "correo": n["correo"],
                        "celular": n["celular"],
                        "notas": {},
                    }
                estudiantes[codigo]["notas"][asignatura] = n["nota"]

        notas_finales = []
        for est in estudiantes.values():
            notas_asignaturas = list(est["notas"].values())
            promedio = sum(notas_asignaturas) / len(notas_asignaturas)
            equivalencia = self._calcular_equivalencia(promedio)
            est["promedio_corte"] = round(promedio, 2)
            est["promedio_general"] = equivalencia
            notas_finales.append(est)

        salida_json = self.path / f"notas_unificadas_{self.corte}.json"
        try:
            with open(salida_json, "w", encoding="utf-8") as salida:
                json.dump(notas_finales, salida, indent=4, ensure_ascii=False)
            self.logger.info(f"JSON escrito: {salida_json}")
        except Exception as e:
            self.logger.error(f"Error escribiendo JSON {salida_json}: {e}")

        return salida_json


