# Desarrollado por: JOSE LUIS CARDOZO INCIARTE
# Módulo: Lógica de Negocio y Manejo de Excepciones

from src.modelos import Cliente, ReservaSalas, AlquilerEquipos, AsesoriaEspecializada, Reserva
from src.excepciones import ClienteNoEncontradoError, ClienteDuplicadoError, ServicioNoDisponibleError, DatosInvalidosError, ReservaInvalidaError
from src.gestor_logs import registrar_error, registrar_evento

class SistemaReservasFJ:
    """
    Clase principal que gestiona las listas en memoria y aplica la lógica de negocio.
    Implementa el manejo avanzado de excepciones (try/except/else/finally).
    """
    def __init__(self):
        self.clientes = {}  # Diccionario para búsqueda rápida por documento
        self.servicios = {} # Diccionario para búsqueda rápida por ID
        self.reservas = []
        self.contador_reservas = 1
        self._inicializar_servicios_base()

    def _inicializar_servicios_base(self):
        """Carga algunos servicios por defecto en el sistema."""
        self.servicios["S01"] = ReservaSalas("S01", "Sala de Conferencias A", 150000, 20)
        self.servicios["E01"] = AlquilerEquipos("E01", "Proyector 4K", 80000, True)
        self.servicios["A01"] = AsesoriaEspecializada("A01", "Consultoría IT", 120000, "Arquitectura de Software")

    def registrar_cliente(self, documento, nombre, correo, telefono):
        """
        Registra un nuevo cliente aplicando validaciones y manejo de errores.
        Uso de try/except/else/finally.
        """
        try:
            # Validaciones básicas
            if not documento or not nombre:
                raise DatosInvalidosError("Documento o Nombre", "Los campos obligatorios no pueden estar vacíos.")
            
            if documento in self.clientes:
                raise ClienteDuplicadoError(documento)
                
            # Creación del objeto
            nuevo_cliente = Cliente(documento, nombre, correo, telefono)
            
        except (DatosInvalidosError, ClienteDuplicadoError) as e:
            registrar_error("Error al registrar cliente", e)
            raise # Relanza la excepción para que la interfaz la maneje
        except Exception as e:
            # Captura cualquier otro error inesperado y lo encadena
            registrar_error("Error inesperado al crear cliente", e)
            raise DatosInvalidosError("General", f"Error interno: {str(e)}") from e
        else:
            # Se ejecuta solo si no hubo excepciones
            self.clientes[documento] = nuevo_cliente
            registrar_evento(f"Cliente registrado exitosamente: {nombre} ({documento})")
            return nuevo_cliente
        finally:
            # Se ejecuta siempre, haya error o no
            registrar_evento(f"Intento de registro finalizado para documento: {documento}")

    def buscar_cliente(self, documento):
        """Busca un cliente y lanza excepción si no existe."""
        if documento not in self.clientes:
            raise ClienteNoEncontradoError(documento)
        return self.clientes[documento]

    def buscar_servicio(self, id_servicio):
        """Busca un servicio y lanza excepción si no existe."""
        if id_servicio not in self.servicios:
            raise ServicioNoDisponibleError(id_servicio)
        return self.servicios[id_servicio]

    def crear_reserva(self, documento_cliente, id_servicio, duracion, parametro_opcional=False):
        """
        Crea una reserva integrando cliente y servicio.
        Aplica encadenamiento de excepciones y bloques completos.
        """
        try:
            # Validar duración
            if not isinstance(duracion, (int, float)) or duracion <= 0:
                raise DatosInvalidosError("Duración", "La duración debe ser un número mayor a cero.")

            # Buscar entidades (pueden lanzar sus propias excepciones)
            cliente = self.buscar_cliente(documento_cliente)
            servicio = self.buscar_servicio(id_servicio)

            # Crear reserva
            nueva_reserva = Reserva(self.contador_reservas, cliente, servicio, duracion)
            
            # Confirmar reserva (aquí se aplica el polimorfismo y sobrecarga)
            # Pasamos el parametro_opcional que puede ser descuento o seguro dependiendo del servicio
            try:
                nueva_reserva.costo_total = servicio.calcular_costo(duracion, parametro_opcional)
                nueva_reserva.estado = "Confirmada"
            except TypeError:
                # Si el servicio no acepta el parámetro opcional, lo calculamos normal
                nueva_reserva.confirmar()

        except (ClienteNoEncontradoError, ServicioNoDisponibleError, DatosInvalidosError) as e:
            registrar_error("Fallo al crear la reserva por datos inválidos o no encontrados", e)
            # Encadenamiento de excepciones: Convertimos el error base en un error de reserva
            raise ReservaInvalidaError(str(e)) from e
        except Exception as e:
            registrar_error("Error crítico inesperado al procesar reserva", e)
            raise ReservaInvalidaError(f"Fallo del sistema: {str(e)}") from e
        else:
            self.reservas.append(nueva_reserva)
            self.contador_reservas += 1
            registrar_evento(f"Reserva #{nueva_reserva.id_reserva} creada con éxito. Costo: ${nueva_reserva.costo_total}")
            return nueva_reserva
        finally:
            registrar_evento(f"Proceso de reserva finalizado para cliente: {documento_cliente}")

    def obtener_todas_reservas(self):
        return self.reservas
