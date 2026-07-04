# Desarrollado por: JOSE LUIS CARDOZO INCIARTE
# Módulo: Excepciones Personalizadas

class ErrorSistemaFJ(Exception):
    """Clase base abstracta para todas las excepciones del sistema Software FJ."""
    pass

class ClienteNoEncontradoError(ErrorSistemaFJ):
    """Excepción lanzada cuando se intenta buscar o usar un cliente que no existe."""
    def __init__(self, documento, mensaje="El cliente con el documento especificado no fue encontrado."):
        self.documento = documento
        self.mensaje = f"{mensaje} (Documento: {documento})"
        super().__init__(self.mensaje)

class ClienteDuplicadoError(ErrorSistemaFJ):
    """Excepción lanzada cuando se intenta registrar un cliente con un documento que ya existe."""
    def __init__(self, documento, mensaje="Ya existe un cliente registrado con este documento."):
        self.documento = documento
        self.mensaje = f"{mensaje} (Documento: {documento})"
        super().__init__(self.mensaje)

class ServicioNoDisponibleError(ErrorSistemaFJ):
    """Excepción lanzada cuando un servicio solicitado no está disponible o no existe."""
    def __init__(self, servicio_id, mensaje="El servicio solicitado no se encuentra disponible."):
        self.servicio_id = servicio_id
        self.mensaje = f"{mensaje} (ID Servicio: {servicio_id})"
        super().__init__(self.mensaje)

class DatosInvalidosError(ErrorSistemaFJ):
    """Excepción lanzada cuando los datos ingresados por el usuario no cumplen con las validaciones."""
    def __init__(self, campo, mensaje="Los datos ingresados no son válidos."):
        self.campo = campo
        self.mensaje = f"{mensaje} (Campo inválido: {campo})"
        super().__init__(self.mensaje)

class ReservaInvalidaError(ErrorSistemaFJ):
    """Excepción lanzada cuando se intenta crear una reserva que incumple las reglas de negocio."""
    def __init__(self, motivo, mensaje="No se pudo procesar la reserva."):
        self.motivo = motivo
        self.mensaje = f"{mensaje} Motivo: {motivo}"
        super().__init__(self.mensaje)
