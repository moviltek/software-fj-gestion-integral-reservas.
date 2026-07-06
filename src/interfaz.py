# Desarrollado por: JOSE LUIS CARDOZO INCIARTE
# Módulo: Interfaz de Consola

from src.logica import SistemaReservasFJ
from src.excepciones import ErrorSistemaFJ

class InterfazConsola:
    """
    Clase que maneja la interacción con el usuario a través de la terminal.
    Garantiza que la aplicación nunca se detenga ante errores graves capturando
    las excepciones de la lógica de negocio.
    """
    def __init__(self):
        self.sistema = SistemaReservasFJ()

    def mostrar_menu(self):
        print("\n" + "="*50)
        print("   SISTEMA DE GESTIÓN DE RESERVAS - SOFTWARE FJ")
        print("="*50)
        print("1. Registrar nuevo cliente")
        print("2. Ver servicios disponibles")
        print("3. Crear una reserva")
        print("4. Ver todas las reservas")
        print("5. Salir")
        print("="*50)

    def ejecutar(self):
        """Bucle principal de la aplicación."""
        while True:
            self.mostrar_menu()
            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self._menu_registrar_cliente()
            elif opcion == '2':
                self._menu_ver_servicios()
            elif opcion == '3':
                self._menu_crear_reserva()
            elif opcion == '4':
                self._menu_ver_reservas()
            elif opcion == '5':
                print("\n¡Gracias por usar el sistema Software FJ! Hasta luego.")
                break
            else:
                print("\n[!] Opción inválida. Por favor, intente de nuevo.")

    def _menu_registrar_cliente(self):
        print("\n--- REGISTRO DE CLIENTE ---")
        documento = input("Documento de identidad: ")
        nombre = input("Nombre completo: ")
        correo = input("Correo electrónico: ")
        telefono = input("Teléfono: ")

        try:
            cliente = self.sistema.registrar_cliente(documento, nombre, correo, telefono)
            print(f"\n[ÉXITO] Cliente {cliente.nombre} registrado correctamente.")
        except ErrorSistemaFJ as e:
            # Aquí garantizamos que la aplicación no se detenga ante errores
            print(f"\n[ERROR DEL SISTEMA] {e.mensaje}")
        except Exception as e:
            print(f"\n[ERROR CRÍTICO] Ocurrió un fallo inesperado: {str(e)}")

    def _menu_ver_servicios(self):
        print("\n--- SERVICIOS DISPONIBLES ---")
        for id_srv, servicio in self.sistema.servicios.items():
            print(f"[{id_srv}] {servicio.mostrar_detalles()}")

    def _menu_crear_reserva(self):
        print("\n--- CREAR NUEVA RESERVA ---")
        documento = input("Ingrese el documento del cliente: ")
        
        self._menu_ver_servicios()
        id_servicio = input("\nIngrese el ID del servicio a reservar: ")
        
        try:
            duracion = float(input("Ingrese la duración (horas/días/sesiones): "))
            
            # Preguntamos por el parámetro opcional (seguro o descuento)
            opcional_input = input("¿Aplicar adicional (Descuento/Seguro)? (s/n): ").lower()
            parametro_opcional = True if opcional_input == 's' else False

            reserva = self.sistema.crear_reserva(documento, id_servicio, duracion, parametro_opcional)
            print(f"\n[ÉXITO] Reserva creada correctamente.")
            print(reserva)

        except ValueError:
            print("\n[ERROR] La duración debe ser un valor numérico.")
        except ErrorSistemaFJ as e:
            print(f"\n[ERROR DE NEGOCIO] {e.mensaje}")
            print("Revise el archivo 'errores.log' para más detalles técnicos.")
        except Exception as e:
            print(f"\n[ERROR CRÍTICO] Ocurrió un fallo inesperado: {str(e)}")

    def _menu_ver_reservas(self):
        print("\n--- LISTADO DE RESERVAS ---")
        reservas = self.sistema.obtener_todas_reservas()
        if not reservas:
            print("No hay reservas registradas en el sistema.")
        else:
            for r in reservas:
                print(r)
