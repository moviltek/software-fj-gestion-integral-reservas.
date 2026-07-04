# Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ

Este proyecto es el desarrollo de la Fase 4 del curso de Programación. Consiste en un sistema orientado a objetos, desarrollado en Python con interfaz gráfica en Tkinter, que gestiona clientes, servicios y reservas sin uso de bases de datos.

## Integrantes
- José Luis (rama-joseluis)
- [Nombre Integrante 2]
- [Nombre Integrante 3]
- [Nombre Integrante 4]
- [Nombre Integrante 5]

## Características Principales
- **Modularidad:** El código está dividido en múltiples archivos según su responsabilidad.
- **Programación Orientada a Objetos:** Uso de clases abstractas, herencia, polimorfismo y encapsulamiento.
- **Manejo Avanzado de Excepciones:** Implementación de excepciones personalizadas, bloques `try/except/else/finally` y encadenamiento de errores.
- **Sistema de Logs:** Registro de todos los eventos y errores en un archivo `registro_errores.log`.
- **Interfaz Gráfica:** Desarrollada con Tkinter.
- **Simulaciones:** Script para ejecutar operaciones válidas e inválidas y comprobar la robustez del sistema.

## Estructura del Proyecto
- `src/excepciones.py`: Definición de excepciones personalizadas.
- `src/gestor_logs.py`: Configuración del sistema de logging.
- `src/modelos.py`: Clases abstractas y entidades (Cliente, Servicio, Reserva).
- `src/logica.py`: Lógica de negocio y almacenamiento en memoria (listas).
- `src/interfaz.py`: Diseño de la interfaz gráfica con Tkinter.
- `main.py`: Punto de entrada de la aplicación.
- `simulaciones.py`: Script con las 10 simulaciones requeridas.
