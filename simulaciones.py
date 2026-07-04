# Autor: José Luis
from src.gestor_logs import configurar_logging, registrar_info, registrar_error
from src.logica import GestorSistema

def ejecutar_simulaciones():
    configurar_logging()
    registrar_info("=== INICIANDO SIMULACIONES AUTOMÁTICAS ===")
    gestor = GestorSistema()

    # 1. Registro de cliente válido
    print("1. Registrando cliente válido...")
    gestor.registrar_cliente("1001", "Juan Perez", "juan@correo.com")

    # 2. Registro de cliente inválido (sin nombre)
    print("2. Registrando cliente inválido...")
    try:
        gestor.registrar_cliente("1002", "", "invalido@correo.com")
    except Exception as e:
        print(f"   Error esperado capturado: {e}")

    # 3. Registro de cliente inválido (email incorrecto)
    print("3. Registrando cliente inválido (email)...")
    try:
        gestor.registrar_cliente("1003", "Maria", "correosin_arroba.com")
    except Exception as e:
        print(f"   Error esperado capturado: {e}")

    # 4. Registro de servicio válido (Sala)
    print("4. Registrando servicio (Sala)...")
    gestor.registrar_servicio("Sala", "S01", "Sala de Juntas A", 50.0)

    # 5. Registro de servicio válido (Equipo)
    print("5. Registrando servicio (Equipo)...")
    gestor.registrar_servicio("Equipo", "E01", "Proyector 4K", 20.0)

    # 6. Reserva exitosa
    print("6. Creando reserva exitosa...")
    gestor.crear_reserva("1001", "S01", 2, incluye_equipos_extra=True)

    # 7. Reserva fallida (Servicio no disponible - ya está reservado)
    print("7. Creando reserva fallida (servicio ocupado)...")
    try:
        gestor.crear_reserva("1001", "S01", 1)
    except Exception as e:
        print(f"   Error esperado capturado: {e}")

    # 8. Reserva fallida (Cliente no existe)
    print("8. Creando reserva fallida (cliente inexistente)...")
    try:
        gestor.crear_reserva("9999", "E01", 1)
    except Exception as e:
        print(f"   Error esperado capturado: {e}")

    # 9. Reserva fallida (Duración inválida / cálculo inconsistente)
    print("9. Creando reserva fallida (duración negativa)...")
    try:
        gestor.crear_reserva("1001", "E01", -5)
    except Exception as e:
        print(f"   Error esperado capturado: {e}")

    # 10. Reserva exitosa con otro servicio
    print("10. Creando reserva exitosa (Equipo)...")
    gestor.crear_reserva("1001", "E01", 3, aplica_seguro=True)

    registrar_info("=== SIMULACIONES FINALIZADAS ===")
    print("\nSimulaciones finalizadas. Revise el archivo registro_errores.log para ver los detalles.")

if __name__ == "__main__":
    ejecutar_simulaciones()
