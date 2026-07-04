# Autor: José Luis
from src.modelos import Cliente, ReservaSalas, AlquilerEquipos, AsesoriaEspecializada, Reserva
from src.excepciones import ClienteInvalidoError, ServicioNoDisponibleError, ReservaInvalidaError, CalculoInconsistenteError
from src.gestor_logs import registrar_info, registrar_error

class GestorSistema:
    """Clase encargada de administrar las listas en memoria y la lógica principal."""
    
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []
        self.contador_reservas = 1

    def registrar_cliente(self, identificacion, nombre, email):
        try:
            nuevo_cliente = Cliente(identificacion, nombre, email)
            # Verificar duplicados
            for c in self.clientes:
                if c.get_identificacion() == identificacion:
                    raise ClienteInvalidoError(f"El cliente con ID {identificacion} ya existe.")
        except ClienteInvalidoError as e:
            registrar_error("Error al registrar cliente", e)
            raise
        except Exception as e:
            registrar_error("Error inesperado al registrar cliente", e)
            raise ClienteInvalidoError(f"Error inesperado: {str(e)}") from e
        else:
            self.clientes.append(nuevo_cliente)
            registrar_info(f"Cliente registrado exitosamente: {nombre}")
            return nuevo_cliente
        finally:
            registrar_info("Intento de registro de cliente finalizado.")

    def registrar_servicio(self, tipo, codigo, nombre, precio_base):
        try:
            if tipo == "Sala":
                servicio = ReservaSalas(codigo, nombre, precio_base)
            elif tipo == "Equipo":
                servicio = AlquilerEquipos(codigo, nombre, precio_base)
            elif tipo == "Asesoria":
                servicio = AsesoriaEspecializada(codigo, nombre, precio_base)
            else:
                raise ValueError("Tipo de servicio desconocido.")
            
            for s in self.servicios:
                if s.obtener_identificador() == codigo:
                    raise ValueError(f"El servicio con código {codigo} ya existe.")
                    
            self.servicios.append(servicio)
            registrar_info(f"Servicio registrado: {nombre} ({tipo})")
            return servicio
        except Exception as e:
            registrar_error("Error al registrar servicio", e)
            raise

    def buscar_cliente(self, identificacion):
        for c in self.clientes:
            if c.get_identificacion() == identificacion:
                return c
        return None

    def buscar_servicio(self, codigo):
        for s in self.servicios:
            if s.obtener_identificador() == codigo:
                return s
        return None

    def crear_reserva(self, id_cliente, cod_servicio, duracion, **kwargs):
        try:
            cliente = self.buscar_cliente(id_cliente)
            if not cliente:
                raise ReservaInvalidaError(f"Cliente con ID {id_cliente} no encontrado.")
            
            servicio = self.buscar_servicio(cod_servicio)
            if not servicio:
                raise ReservaInvalidaError(f"Servicio con código {cod_servicio} no encontrado.")
                
            reserva = Reserva(self.contador_reservas, cliente, servicio, duracion, **kwargs)
            reserva.confirmar()
            
        except (ServicioNoDisponibleError, CalculoInconsistenteError, ReservaInvalidaError) as e:
            registrar_error(f"Error específico al crear reserva", e)
            raise
        except Exception as e:
            registrar_error("Error inesperado al crear reserva", e)
            raise ReservaInvalidaError(f"Fallo inesperado: {str(e)}") from e
        else:
            self.reservas.append(reserva)
            self.contador_reservas += 1
            registrar_info(f"Reserva creada y confirmada: {reserva.id_reserva}")
            return reserva
        finally:
            registrar_info("Proceso de creación de reserva finalizado.")
