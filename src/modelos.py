# Autor: José Luis
from abc import ABC, abstractmethod
from src.excepciones import ClienteInvalidoError, CalculoInconsistenteError

class EntidadGeneral(ABC):
    """Clase abstracta que representa entidades generales del sistema."""
    
    @abstractmethod
    def obtener_identificador(self):
        pass

class Cliente(EntidadGeneral):
    """Clase que representa a un cliente con datos encapsulados."""
    
    def __init__(self, identificacion, nombre, email):
        self.__identificacion = identificacion
        self.__nombre = nombre
        self.__email = email
        self.validar_datos()

    def validar_datos(self):
        if not self.__identificacion or not str(self.__identificacion).strip():
            raise ClienteInvalidoError("La identificación del cliente no puede estar vacía.")
        if not self.__nombre or not str(self.__nombre).strip():
            raise ClienteInvalidoError("El nombre del cliente no puede estar vacío.")
        if "@" not in str(self.__email):
            raise ClienteInvalidoError("El email del cliente no es válido.")

    def obtener_identificador(self):
        return self.__identificacion

    # Getters
    def get_identificacion(self): return self.__identificacion
    def get_nombre(self): return self.__nombre
    def get_email(self): return self.__email

    def __str__(self):
        return f"Cliente: {self.__nombre} (ID: {self.__identificacion})"


class Servicio(EntidadGeneral):
    """Clase abstracta que representa un servicio ofrecido por Software FJ."""
    
    def __init__(self, codigo, nombre, precio_base):
        self._codigo = codigo
        self._nombre = nombre
        self._precio_base = precio_base
        self._disponible = True

    def obtener_identificador(self):
        return self._codigo

    def is_disponible(self):
        return self._disponible

    def set_disponible(self, estado):
        self._disponible = estado

    @abstractmethod
    def calcular_costo(self, duracion, *args, **kwargs):
        """Método abstracto para calcular el costo, permite sobrecarga simulada con *args y **kwargs"""
        pass

    @abstractmethod
    def describir_servicio(self):
        pass

    def __str__(self):
        return f"Servicio: {self._nombre} - Código: {self._codigo}"


class ReservaSalas(Servicio):
    def calcular_costo(self, duracion, incluye_equipos_extra=False):
        try:
            duracion = float(duracion)
            if duracion <= 0:
                raise ValueError("La duración debe ser mayor a 0.")
            costo = self._precio_base * duracion
            if incluye_equipos_extra:
                costo += 50.0  # Cargo fijo por equipos extra
            return costo
        except ValueError as e:
            raise CalculoInconsistenteError(f"Error al calcular costo de sala: {e}")

    def describir_servicio(self):
        return f"Reserva de Sala '{self._nombre}' a ${self._precio_base}/hora."


class AlquilerEquipos(Servicio):
    def calcular_costo(self, dias, aplica_seguro=True):
        try:
            dias = int(dias)
            if dias <= 0:
                raise ValueError("Los días de alquiler deben ser mayores a 0.")
            costo = self._precio_base * dias
            if aplica_seguro:
                costo *= 1.10  # 10% adicional por seguro
            return costo
        except ValueError as e:
            raise CalculoInconsistenteError(f"Error al calcular costo de equipo: {e}")

    def describir_servicio(self):
        return f"Alquiler de Equipo '{self._nombre}' a ${self._precio_base}/día."


class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, horas, nivel_experto=False):
        try:
            horas = float(horas)
            if horas <= 0:
                raise ValueError("Las horas de asesoría deben ser mayores a 0.")
            costo = self._precio_base * horas
            if nivel_experto:
                costo *= 1.50  # 50% extra por nivel experto
            return costo
        except ValueError as e:
            raise CalculoInconsistenteError(f"Error al calcular costo de asesoría: {e}")

    def describir_servicio(self):
        return f"Asesoría '{self._nombre}' a ${self._precio_base}/hora."


class Reserva:
    """Clase que integra cliente, servicio, duración y estado."""
    
    def __init__(self, id_reserva, cliente, servicio, duracion, **kwargs):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.parametros_extra = kwargs
        self.estado = "Pendiente"
        self.costo_total = 0.0

    def confirmar(self):
        if not self.servicio.is_disponible():
            from src.excepciones import ServicioNoDisponibleError
            raise ServicioNoDisponibleError(f"El servicio {self.servicio.obtener_identificador()} no está disponible.")
        
        self.costo_total = self.servicio.calcular_costo(self.duracion, **self.parametros_extra)
        self.servicio.set_disponible(False)
        self.estado = "Confirmada"

    def cancelar(self):
        self.estado = "Cancelada"
        self.servicio.set_disponible(True)

    def __str__(self):
        return f"Reserva {self.id_reserva} | {self.cliente.get_nombre()} | {self.servicio._nombre} | Estado: {self.estado} | Costo: ${self.costo_total:.2f}"
