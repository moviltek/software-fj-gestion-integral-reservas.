# Autor: José Luis
import tkinter as tk
from tkinter import messagebox, ttk
from src.logica import GestorSistema
from src.excepciones import ErrorSistemaFJ

class AppInterfaz:
    def __init__(self, root, gestor):
        self.root = root
        self.gestor = gestor
        self.root.title("Software FJ - Gestión de Reservas")
        self.root.geometry("600x500")
        
        self.notebook = ttk.Notebook(root)
        self.notebook.pack(expand=True, fill='both')
        
        self.tab_clientes = ttk.Frame(self.notebook)
        self.tab_servicios = ttk.Frame(self.notebook)
        self.tab_reservas = ttk.Frame(self.notebook)
        
        self.notebook.add(self.tab_clientes, text='Clientes')
        self.notebook.add(self.tab_servicios, text='Servicios')
        self.notebook.add(self.tab_reservas, text='Reservas')
        
        self._construir_tab_clientes()
        self._construir_tab_servicios()
        self._construir_tab_reservas()

    def _construir_tab_clientes(self):
        tk.Label(self.tab_clientes, text="Identificación:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_id_cliente = tk.Entry(self.tab_clientes)
        self.entry_id_cliente.grid(row=0, column=1)

        tk.Label(self.tab_clientes, text="Nombre:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_nom_cliente = tk.Entry(self.tab_clientes)
        self.entry_nom_cliente.grid(row=1, column=1)

        tk.Label(self.tab_clientes, text="Email:").grid(row=2, column=0, padx=10, pady=10)
        self.entry_email_cliente = tk.Entry(self.tab_clientes)
        self.entry_email_cliente.grid(row=2, column=1)

        tk.Button(self.tab_clientes, text="Registrar Cliente", command=self.registrar_cliente).grid(row=3, column=0, columnspan=2, pady=20)

    def _construir_tab_servicios(self):
        tk.Label(self.tab_servicios, text="Tipo:").grid(row=0, column=0, padx=10, pady=10)
        self.combo_tipo_serv = ttk.Combobox(self.tab_servicios, values=["Sala", "Equipo", "Asesoria"])
        self.combo_tipo_serv.grid(row=0, column=1)
        self.combo_tipo_serv.current(0)

        tk.Label(self.tab_servicios, text="Código:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_cod_serv = tk.Entry(self.tab_servicios)
        self.entry_cod_serv.grid(row=1, column=1)

        tk.Label(self.tab_servicios, text="Nombre:").grid(row=2, column=0, padx=10, pady=10)
        self.entry_nom_serv = tk.Entry(self.tab_servicios)
        self.entry_nom_serv.grid(row=2, column=1)

        tk.Label(self.tab_servicios, text="Precio Base:").grid(row=3, column=0, padx=10, pady=10)
        self.entry_precio_serv = tk.Entry(self.tab_servicios)
        self.entry_precio_serv.grid(row=3, column=1)

        tk.Button(self.tab_servicios, text="Registrar Servicio", command=self.registrar_servicio).grid(row=4, column=0, columnspan=2, pady=20)

    def _construir_tab_reservas(self):
        tk.Label(self.tab_reservas, text="ID Cliente:").grid(row=0, column=0, padx=10, pady=10)
        self.entry_res_cliente = tk.Entry(self.tab_reservas)
        self.entry_res_cliente.grid(row=0, column=1)

        tk.Label(self.tab_reservas, text="Cod. Servicio:").grid(row=1, column=0, padx=10, pady=10)
        self.entry_res_serv = tk.Entry(self.tab_reservas)
        self.entry_res_serv.grid(row=1, column=1)

        tk.Label(self.tab_reservas, text="Duración/Días/Horas:").grid(row=2, column=0, padx=10, pady=10)
        self.entry_res_duracion = tk.Entry(self.tab_reservas)
        self.entry_res_duracion.grid(row=2, column=1)

        tk.Button(self.tab_reservas, text="Crear Reserva", command=self.crear_reserva).grid(row=3, column=0, columnspan=2, pady=20)

    def registrar_cliente(self):
        try:
            id_c = self.entry_id_cliente.get()
            nom = self.entry_nom_cliente.get()
            email = self.entry_email_cliente.get()
            self.gestor.registrar_cliente(id_c, nom, email)
            messagebox.showinfo("Éxito", "Cliente registrado correctamente.")
        except ErrorSistemaFJ as e:
            messagebox.showerror("Error de Validación", str(e))
        except Exception as e:
            messagebox.showerror("Error Inesperado", "Ocurrió un error. Revise el log.")

    def registrar_servicio(self):
        try:
            tipo = self.combo_tipo_serv.get()
            cod = self.entry_cod_serv.get()
            nom = self.entry_nom_serv.get()
            precio = float(self.entry_precio_serv.get())
            self.gestor.registrar_servicio(tipo, cod, nom, precio)
            messagebox.showinfo("Éxito", "Servicio registrado correctamente.")
        except ValueError:
            messagebox.showerror("Error", "El precio debe ser numérico.")
        except Exception as e:
            messagebox.showerror("Error Inesperado", "Ocurrió un error. Revise el log.")

    def crear_reserva(self):
        try:
            id_c = self.entry_res_cliente.get()
            cod_s = self.entry_res_serv.get()
            duracion = float(self.entry_res_duracion.get())
            reserva = self.gestor.crear_reserva(id_c, cod_s, duracion)
            messagebox.showinfo("Éxito", f"Reserva creada. Costo: ${reserva.costo_total:.2f}")
        except ValueError:
            messagebox.showerror("Error", "La duración debe ser numérica.")
        except ErrorSistemaFJ as e:
            messagebox.showerror("Error en Reserva", str(e))
        except Exception as e:
            messagebox.showerror("Error Inesperado", "Ocurrió un error. Revise el log.")
