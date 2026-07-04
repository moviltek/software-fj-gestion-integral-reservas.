# Autor: José Luis

class ErrorSistemaFJ(Exception):
    """Clase base para las excepciones personalizadas del sistema."""
    pass

class ClienteInvalidoError(ErrorSistemaFJ):
    """Se lanza cuando los datos de un cliente no son válidos."""
    pass

class ServicioNoDisponibleError(ErrorSistemaFJ):
    """Se lanza cuando se intenta reservar un servicio que no está disponible."""
    pass

class ReservaInvalidaError(ErrorSistemaFJ):
    """Se lanza cuando hay un error al crear o procesar una reserva."""
    pass

class CalculoInconsistenteError(ErrorSistemaFJ):
    """Se lanza cuando ocurre un error matemático o lógico en el cálculo de costos."""
    pass
