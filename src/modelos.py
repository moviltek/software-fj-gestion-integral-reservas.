# Desarrollado por: JOSE LUIS CARDOZO INCIARTE
# Módulo: Modelos (Clases y POO)

from abc import ABC, abstractmethod
from datetime import datetime

class EntidadGeneral(ABC):
    """
    Clase abstracta base para todas las entidades del sistema.
    Aplica el principio de abstracción.
    """
    def __init__(self, id_entidad):
        self._id_entidad = id_entidad

    @abstractmethod
    def mostrar_detalles(self):
        """Método abstracto que debe ser implementado por las clases hijas."""
        pass

class Cliente(EntidadGeneral):
    """
    Clase que representa a un cliente de Software FJ.
    Aplica encapsulamiento para proteger los datos personales.
    """
    def __init__(self, documento, nombre, correo, telefono):
        super().__init__(documento)
        self.__nombre = nombre
        self.__correo = correo
        self.__telefono = telefono

    # Getters y Setters (Encapsulamiento)
    @property
    def documento(self):
        return self._id_entidad

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self, nuevo_nombre):
        if not nuevo_nombre.strip():
            raise ValueError("El nombre no puede estar vacío.")
        self.__nombre = nuevo_nombre

    def mostrar_detalles(self):
        return f"Cliente: {self.__nombre} | Doc: {self.documento} | Correo: {self.__correo}"

class Servicio(EntidadGeneral):
    """
    Clase abstracta que representa un servicio ofrecido por la empresa.
    """
    def __init__(self, id_servicio, nombre, tarifa_base):
        super().__init__(id_servicio)
        self.nombre = nombre
        self.tarifa_base = tarifa_base

    @abstractmethod
    def calcular_costo(self, cantidad):
        """
        Calcula el costo total del servicio. 
        Será sobrescrito (polimorfismo) por las clases hijas.
        """
        pass

class ReservaSalas(Servicio):
    """Clase derivada para el servicio de reserva de salas."""
    def __init__(self, id_servicio, nombre, tarifa_base, capacidad_maxima):
        super().__init__(id_servicio, nombre, tarifa_base)
        self.capacidad_maxima = capacidad_maxima

    def calcular_costo(self, horas, aplica_descuento=False, aplica_impuesto=True):
        """
        Sobrescritura del método. Calcula el costo por horas.
        Aplica sobrecarga simulada mediante parámetros opcionales.
        """
        costo = self.tarifa_base * horas
        if aplica_descuento and horas > 5:
            costo *= 0.90  # 10% de descuento si son más de 5 horas
        if aplica_impuesto:
            costo *= 1.19  # Aplica 19% de IVA
        return costo

    def mostrar_detalles(self):
        return f"Sala: {self.nombre} | Capacidad: {self.capacidad_maxima} | Tarifa/h: ${self.tarifa_base}"

class AlquilerEquipos(Servicio):
    """Clase derivada para el servicio de alquiler de equipos tecnológicos."""
    def __init__(self, id_servicio, nombre, tarifa_base, requiere_deposito=True):
        super().__init__(id_servicio, nombre, tarifa_base)
        self.requiere_deposito = requiere_deposito

    def calcular_costo(self, dias, seguro_adicional=False, aplica_impuesto=True):
        """Calcula el costo por días. Puede incluir un seguro opcional e impuestos."""
        costo = self.tarifa_base * dias
        if seguro_adicional:
            costo += 50000  # Costo fijo del seguro
        if aplica_impuesto:
            costo *= 1.19  # Aplica 19% de IVA
        return costo

    def mostrar_detalles(self):
        return f"Equipo: {self.nombre} | Tarifa/día: ${self.tarifa_base} | Depósito: {'Sí' if self.requiere_deposito else 'No'}"

class AsesoriaEspecializada(Servicio):
    """Clase derivada para el servicio de asesorías."""
    def __init__(self, id_servicio, nombre, tarifa_base, especialidad):
        super().__init__(id_servicio, nombre, tarifa_base)
        self.especialidad = especialidad

    def calcular_costo(self, sesiones, aplica_impuesto=True):
        """Calcula el costo por número de sesiones, aplicando impuestos por defecto."""
        costo = self.tarifa_base * sesiones
        if aplica_impuesto:
            costo *= 1.19  # Aplica 19% de IVA
        return costo

    def mostrar_detalles(self):
        return f"Asesoría: {self.nombre} | Especialidad: {self.especialidad} | Tarifa/sesión: ${self.tarifa_base}"

class Reserva:
    """
    Clase que integra un Cliente y un Servicio.
    """
    def __init__(self, id_reserva, cliente, servicio, duracion, fecha=None):
        self.id_reserva = id_reserva
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.fecha = fecha if fecha else datetime.now().strftime("%Y-%m-%d %H:%M")
        self.estado = "Pendiente"
        self.costo_total = 0.0

    def confirmar(self):
        """Confirma la reserva y calcula el costo final."""
        self.costo_total = self.servicio.calcular_costo(self.duracion)
        self.estado = "Confirmada"

    def cancelar(self):
        """Cancela la reserva."""
        self.estado = "Cancelada"

    def __str__(self):
        return (f"Reserva #{self.id_reserva} | Estado: {self.estado} | "
                f"Cliente: {self.cliente.nombre} | Servicio: {self.servicio.nombre} | "
                f"Costo Total: ${self.costo_total}")
