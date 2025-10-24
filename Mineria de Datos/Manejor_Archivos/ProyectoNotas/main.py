from pathlib import Path
from src.UnificarNotas import UnificarNotas
from src.GenerarReporte import GenerarReporte
from src.logger_config import configurar_logger

def main():
    
    path = Path("Data")
    logger = configurar_logger("Main", path / "logs")

    try:
        cortes_validos = ["primer_corte", "segundo_corte", "tercer_corte"]
        corte = input("Ingrese el corte actual (primer_corte, segundo_corte, tercer_corte): ").strip().lower()

        while corte not in cortes_validos:
            print("Corte no válido. Intente nuevamente.")
            corte = input("Ingrese el corte actual (primer_corte, segundo_corte, tercer_corte): ").strip().lower()

        
        unificador = UnificarNotas(path, corte)
        archivo_json = unificador.main()

        reporte = GenerarReporte(path, corte)
        reporte.generar(archivo_json)

        logger.info("Proceso completado correctamente.")

    except Exception as e:
        logger.exception(f"Error crítico durante la ejecución: {e}")

if __name__ == "__main__":
    main()
