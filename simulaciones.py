# Desarrollado por: JOSE LUIS CARDOZO INCIARTE
# Módulo: Simulaciones (Pruebas Automatizadas)

from src.logica import SistemaReservasFJ
from src.gestor_logs import configurar_logs

def ejecutar_simulaciones():
    """
    Ejecuta las 10 operaciones completas exigidas por la rúbrica
    para demostrar la estabilidad del sistema ante errores.
    """
    configurar_logs()
    sistema = SistemaReservasFJ()
    
    print("="*50)
    print(" INICIANDO SIMULACIONES AUTOMATIZADAS (10 OPERACIONES)")
    print("="*50)

    # --- OPERACIONES VÁLIDAS ---
    print("\n>>> 1. Creación de cliente válido")
    try:
        sistema.registrar_cliente("1001", "Juan Perez", "juan@mail.com", "555-1234")
        print("Operación 1 Exitosa.")
    except Exception as e:
        print(f"Fallo en Operación 1: {e}")

    print("\n>>> 2. Creación de segundo cliente válido")
    try:
        sistema.registrar_cliente("1002", "Maria Gomez", "maria@mail.com", "555-9876")
        print("Operación 2 Exitosa.")
    except Exception as e:
        print(f"Fallo en Operación 2: {e}")

    print("\n>>> 3. Reserva válida (Sala con descuento)")
    try:
        sistema.crear_reserva("1001", "S01", 6, parametro_opcional=True)
        print("Operación 3 Exitosa.")
    except Exception as e:
        print(f"Fallo en Operación 3: {e}")

    print("\n>>> 4. Reserva válida (Equipo sin seguro)")
    try:
        sistema.crear_reserva("1002", "E01", 2, parametro_opcional=False)
        print("Operación 4 Exitosa.")
    except Exception as e:
        print(f"Fallo en Operación 4: {e}")

    print("\n>>> 5. Reserva válida (Asesoría)")
    try:
        sistema.crear_reserva("1001", "A01", 3)
        print("Operación 5 Exitosa.")
    except Exception as e:
        print(f"Fallo en Operación 5: {e}")


    # --- OPERACIONES INVÁLIDAS (Para probar excepciones) ---
    print("\n>>> 6. Error: Cliente duplicado")
    try:
        sistema.registrar_cliente("1001", "Juan Copia", "juan2@mail.com", "111")
        print("Operación 6 Falló (Debió lanzar error).")
    except Exception as e:
        print(f"Operación 6 Exitosa (Error capturado): {e}")

    print("\n>>> 7. Error: Datos de cliente vacíos")
    try:
        sistema.registrar_cliente("", "", "", "")
        print("Operación 7 Falló (Debió lanzar error).")
    except Exception as e:
        print(f"Operación 7 Exitosa (Error capturado): {e}")

    print("\n>>> 8. Error: Reserva con cliente inexistente")
    try:
        sistema.crear_reserva("9999", "S01", 2)
        print("Operación 8 Falló (Debió lanzar error).")
    except Exception as e:
        print(f"Operación 8 Exitosa (Error capturado): {e}")

    print("\n>>> 9. Error: Reserva con servicio inexistente")
    try:
        sistema.crear_reserva("1001", "X99", 2)
        print("Operación 9 Falló (Debió lanzar error).")
    except Exception as e:
        print(f"Operación 9 Exitosa (Error capturado): {e}")

    print("\n>>> 10. Error: Reserva con duración inválida")
    try:
        sistema.crear_reserva("1002", "E01", -5)
        print("Operación 10 Falló (Debió lanzar error).")
    except Exception as e:
        print(f"Operación 10 Exitosa (Error capturado): {e}")

    print("\n" + "="*50)
    print(" SIMULACIONES FINALIZADAS. EL SISTEMA NO SE DETUVO.")
    print(" Revise el archivo 'errores.log' para ver el registro.")
    print("="*50)

if __name__ == "__main__":
    ejecutar_simulaciones()
