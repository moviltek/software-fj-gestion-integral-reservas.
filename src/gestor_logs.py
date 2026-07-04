# Desarrollado por: JOSE LUIS CARDOZO INCIARTE
# Módulo: Gestor de Logs

import logging
import os

def configurar_logs():
    """
    Configura el sistema de registro (logging) para la aplicación.
    Crea un archivo 'errores.log' en la raíz del proyecto donde se guardarán
    todos los eventos importantes y excepciones capturadas por el sistema.
    """
    # Definimos el nombre del archivo donde se guardarán los registros
    archivo_log = 'errores.log'
    
    # Configuramos el formato del log: Fecha/Hora - Nivel de severidad - Mensaje
    formato_log = '%(asctime)s - %(levelname)s - %(message)s'
    
    # Configuramos el logger básico de Python
    logging.basicConfig(
        filename=archivo_log,
        level=logging.INFO, # Registra eventos de nivel INFO, WARNING, ERROR y CRITICAL
        format=formato_log,
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    # Mensaje inicial para indicar que el sistema de logs arrancó correctamente
    logging.info("=== Sistema de Gestión FJ Iniciado ===")

def registrar_error(mensaje, excepcion=None):
    """
    Registra un error en el archivo de logs.
    Si se proporciona un objeto de excepción, incluye los detalles técnicos del error.
    """
    if excepcion:
        # Registra el mensaje personalizado junto con el error original
        logging.error(f"{mensaje} | Detalles técnicos: {str(excepcion)}")
    else:
        # Registra solo el mensaje personalizado
        logging.error(mensaje)

def registrar_evento(mensaje):
    """
    Registra un evento normal (no error) en el archivo de logs.
    Útil para registrar creaciones de clientes, servicios o reservas exitosas.
    """
    logging.info(mensaje)
