# Autor: José Luis
import logging
import os

def configurar_logging():
    """
    Configura el sistema de logging para guardar los registros en un archivo.
    """
    log_file = "registro_errores.log"
    
    # Configuración básica del logging
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S"
    )
    
    # También imprimir en consola para facilitar la depuración
    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter("%(asctime)s - %(levelname)s - %(message)s")
    console.setFormatter(formatter)
    logging.getLogger("").addHandler(console)

def registrar_info(mensaje):
    logging.info(mensaje)

def registrar_error(mensaje, excepcion=None):
    if excepcion:
        logging.error(f"{mensaje} | Detalle: {str(excepcion)}")
    else:
        logging.error(mensaje)
