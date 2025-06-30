"""
Ejercicio 8: Agenda de contactos para almacenar nombres y números de teléfono.
Por: Leandro Marquez.
Para: Programación V - UBA.
"""
import tkinter as tk
from tkinter import messagebox, ttk

def main_gui():
    contactos = {}
    
    def es_telefono_valido(telefono):
        """Valida números de teléfono con formato internacional"""
        # Eliminar espacios y guiones para validación
        limpio = telefono.replace(" ", "").replace("-", "")
        
        # Verificar si comienza con '+' y el resto son dígitos
        if limpio.startswith("+"):
            return limpio[1:].isdigit() and len(limpio[1:]) >= 8
        
        # Verificar si son solo dígitos
        return limpio.isdigit() and len(limpio) >= 8
    
    def agregar_contacto():
        nombre = entry_nombre.get().strip()
        telefono = entry_telefono.get().strip()
        
        # Validación de campos vacíos
        if not nombre or not telefono:
            messagebox.showwarning("Campos vacíos", "Debes completar ambos campos: nombre y teléfono.")
            return
            
        # Validación de formato de teléfono
        if not es_telefono_valido(telefono):
            messagebox.showerror("Teléfono inválido", 
                                "Formato de teléfono incorrecto.\n\n"
                                "Ejemplos válidos:\n"
                                "- 1123456789\n"
                                "- 11-2345-6789\n"
                                "- +584142279708\n\n"
                                f"Valor ingresado: '{telefono}'")
            return
            
        # Validación de contacto existente
        if nombre in contactos:
            respuesta = messagebox.askyesno("Contacto existente", 
                                           f"El contacto '{nombre}' ya existe.\n\n"
                                           f"Teléfono actual: {contactos[nombre]}\n\n"
                                           "¿Deseas actualizar el número?")
            if respuesta:
                contactos[nombre] = telefono
                actualizar_lista()
                messagebox.showinfo("Actualizado", f"Teléfono de '{nombre}' actualizado.")
            return
            
        # Agregar contacto
        contactos[nombre] = telefono
        actualizar_lista()
        entry_nombre.delete(0, tk.END)
        entry_telefono.delete(0, tk.END)
        messagebox.showinfo("Éxito", f"Contacto '{nombre}' agregado correctamente.")
        
    def buscar_contacto():
        nombre = entry_buscar.get().strip()
        if not nombre:
            messagebox.showwarning("Búsqueda vacía", "Por favor ingresa un nombre para buscar.")
            return
            
        if nombre in contactos:
            messagebox.showinfo("Resultado de búsqueda", 
                               f"Contacto encontrado:\n\n"
                               f"Nombre: {nombre}\n"
                               f"Teléfono: {contactos[nombre]}")
        else:
            messagebox.showinfo("Resultado de búsqueda", 
                               f"No se encontró ningún contacto con el nombre '{nombre}'.")
            
    def actualizar_lista():
        tree.delete(*tree.get_children())
        for nombre, telefono in contactos.items():
            tree.insert("", tk.END, values=(nombre, telefono))

    root = tk.Tk()
    root.title("📱 Agenda de Contactos")
    root.geometry("700x550")
    
    # Estilo para los elementos
    style = ttk.Style()
    style.configure("TNotebook", background="#F5F5F5")
    style.configure("TNotebook.Tab", font=("Arial", 10, "bold"), padding=[10, 5])
    
    # Frame principal
    main_frame = ttk.Frame(root)
    main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
    
    # Título principal
    header_frame = ttk.Frame(main_frame)
    header_frame.pack(fill=tk.X, pady=(0, 15))
    
    tk.Label(header_frame, text="📞 AGENDA DE CONTACTOS", 
            font=("Arial", 16, "bold"), fg="#3F51B5").pack()
    
    tk.Label(header_frame, text="Administra tus contactos de forma sencilla", 
            font=("Arial", 10), fg="#666666").pack(pady=(5, 0))
    
    # Pestañas
    notebook = ttk.Notebook(main_frame)
    notebook.pack(fill=tk.BOTH, expand=True, pady=10)
    
    # ----------------- Pestaña de Agregar -----------------
    tab_agregar = ttk.Frame(notebook, padding=15)
    notebook.add(tab_agregar, text="➕ Agregar Contacto")
    
    # Formulario de agregar
    form_frame = ttk.Frame(tab_agregar)
    form_frame.pack(fill=tk.X, pady=10)
    
    tk.Label(form_frame, text="Nombre completo:", 
            font=("Arial", 11)).grid(row=0, column=0, sticky="w", pady=5)
    entry_nombre = ttk.Entry(form_frame, font=("Arial", 11))
    entry_nombre.grid(row=0, column=1, sticky="ew", padx=(10, 0), pady=5)
    
    tk.Label(form_frame, text="Número de teléfono:", 
            font=("Arial", 11)).grid(row=1, column=0, sticky="w", pady=5)
    entry_telefono = ttk.Entry(form_frame, font=("Arial", 11))
    entry_telefono.grid(row=1, column=1, sticky="ew", padx=(10, 0), pady=5)
    
    # Configurar expansión de columnas
    form_frame.columnconfigure(1, weight=1)
    
    # Botón de agregar
    btn_frame = ttk.Frame(tab_agregar)
    btn_frame.pack(fill=tk.X, pady=(15, 5))
    
    ttk.Button(btn_frame, text="Guardar Contacto", command=agregar_contacto).pack(pady=10)
    
    # ----------------- Pestaña de Buscar -----------------
    tab_buscar = ttk.Frame(notebook, padding=15)
    notebook.add(tab_buscar, text="🔍 Buscar Contacto")
    
    # Campo de búsqueda
    search_frame = ttk.Frame(tab_buscar)
    search_frame.pack(fill=tk.X, pady=10)
    
    tk.Label(search_frame, text="Nombre a buscar:", 
            font=("Arial", 11)).pack(anchor="w", pady=(0, 5))
    
    input_frame = ttk.Frame(search_frame)
    input_frame.pack(fill=tk.X)
    
    entry_buscar = ttk.Entry(input_frame, font=("Arial", 11))
    entry_buscar.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
    entry_buscar.bind("<Return>", lambda event: buscar_contacto())
    
    ttk.Button(input_frame, text="Buscar", command=buscar_contacto).pack(side=tk.RIGHT)
    
    # ----------------- Pestaña de Listar -----------------
    tab_listar = ttk.Frame(notebook)
    notebook.add(tab_listar, text="👥 Listar Contactos")
    
    # Configurar estilo para el Treeview
    style.configure("Treeview", font=("Arial", 10), rowheight=25)
    style.configure("Treeview.Heading", font=("Arial", 11, "bold"))
    style.map("Treeview", background=[("selected", "#3F51B5")])
    
    # Contenedor para la tabla y scrollbar
    table_container = ttk.Frame(tab_listar)
    table_container.pack(fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Tabla de contactos
    columns = ("Nombre", "Teléfono")
    tree = ttk.Treeview(table_container, columns=columns, show="headings")
    
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=250, anchor="w")
    
    scrollbar = ttk.Scrollbar(table_container, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Botón de actualizar
    btn_refresh = ttk.Button(tab_listar, text="Actualizar Lista", 
                           command=actualizar_lista)
    btn_refresh.pack(pady=(10, 15))
    
    # Configurar estilo para botones destacados
    style.configure("Accent.TButton", background="#3F51B5", foreground="white", 
                   font=("Arial", 10, "bold"))
    
    # Establecer pestaña activa inicial
    notebook.select(0)
    
    root.mainloop()

if __name__ == "__main__":
    main_gui()