# Desarrollado por: JOSE LUIS CARDOZO INCIARTE
# Módulo: Punto de Entrada Principal

from src.interfaz import InterfazConsola
from src.gestor_logs import configurar_logs

def main():
    """
    Función principal que inicializa el sistema de logs y arranca
    la interfaz de consola.
    """
    # 1. Inicializar el sistema de logs (errores.log)
    configurar_logs()
    
    # 2. Inicializar y arrancar la interfaz
    app = InterfazConsola()
    
    try:
        app.ejecutar()
    except KeyboardInterrupt:
        print("\n\n[!] Ejecución interrumpida por el usuario (Ctrl+C). Saliendo de forma segura...")
    except Exception as e:
        print(f"\n[FATAL] Error crítico no manejado: {str(e)}")
        print("El sistema se cerrará. Revise 'errores.log'.")

if __name__ == "__main__":
    main()
