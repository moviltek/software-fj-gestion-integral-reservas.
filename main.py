# Autor: José Luis
import tkinter as tk
from src.gestor_logs import configurar_logging, registrar_info
from src.logica import GestorSistema
from src.interfaz import AppInterfaz

def main():
    # 1. Configurar logging
    configurar_logging()
    registrar_info("Iniciando Sistema Integral de Gestión de Reservas - Software FJ")
    
    # 2. Inicializar lógica
    gestor = GestorSistema()
    
    # 3. Inicializar GUI
    root = tk.Tk()
    app = AppInterfaz(root, gestor)
    
    # 4. Bucle principal
    root.mainloop()
    
    registrar_info("Sistema cerrado correctamente.")

if __name__ == "__main__":
    main()
