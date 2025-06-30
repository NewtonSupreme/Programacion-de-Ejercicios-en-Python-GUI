"""
Índice Interactivo de Ejercicios Python - Versión Moderna
Por: Leandro Marquez
Para: Sumativa 3 Programación V
"""
import tkinter as tk
from tkinter import ttk, messagebox, font
import os
import subprocess
import sys

class ModernIndexApp:
    def __init__(self, root):
        self.root = root
        self.setup_window()
        self.create_styles()
        self.create_widgets()
        self.center_window()
        
    def setup_window(self):
        self.root.title("Índice de Ejercicios Python")
        self.root.geometry("900x700")
        self.root.minsize(800, 600)
        self.root.configure(bg='#f5f7fa')
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)
        
        # Intentar cargar un ícono
        try:
            self.root.iconbitmap('python.ico')
        except:
            pass
    
    def center_window(self):
        """Centrar la ventana en la pantalla"""
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'+{x}+{y}')
    
    def create_styles(self):
        """Crear estilos modernos para los widgets"""
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Configurar colores
        self.style.configure('TFrame', background='#f5f7fa')
        self.style.configure('Header.TFrame', background='#3498db')
        self.style.configure('TLabel', background='#f5f7fa', foreground='#2c3e50')
        self.style.configure('Header.TLabel', background='#3498db', foreground='white', font=('Arial', 14, 'bold'))
        self.style.configure('Treeview', 
                             background='white', 
                             fieldbackground='white',
                             foreground='#34495e',
                             rowheight=30)
        self.style.configure('Treeview.Heading', 
                             background='#2c3e50', 
                             foreground='white',
                             font=('Arial', 10, 'bold'),
                             relief='flat')
        self.style.map('Treeview.Heading', background=[('active', '#3498db')])
        
        # Botones modernos
        self.style.configure('Accent.TButton', 
                            foreground='white',
                            background='#3498db',
                            font=('Arial', 10, 'bold'),
                            borderwidth=1,
                            focuscolor='#3498db')
        self.style.map('Accent.TButton', 
                      background=[('active', '#2980b9')])
        
        self.style.configure('Exit.TButton', 
                            foreground='white',
                            background='#e74c3c',
                            font=('Arial', 10, 'bold'))
        self.style.map('Exit.TButton', 
                      background=[('active', '#c0392b')])
    
    def create_widgets(self):
        """Crear todos los elementos de la interfaz"""
        # Frame principal
        main_frame = ttk.Frame(self.root)
        main_frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)
        
        # Encabezado con efecto moderno
        header_frame = ttk.Frame(main_frame, style='Header.TFrame')
        header_frame.pack(fill=tk.X, pady=(0, 20))
        
        # Título con sombra
        title_label = ttk.Label(
            header_frame, 
            text="ÍNDICE DE EJERCICIOS PYTHON", 
            style='Header.TLabel'
        )
        title_label.pack(pady=15)
        
        # Subtítulo
        subtitle = ttk.Label(
            header_frame,
            text="Seleccione un ejercicio para ejecutarlo",
            style='Header.TLabel',
            font=('Arial', 10)
        )
        subtitle.pack(pady=(0, 15))
        
        # Lista de ejercicios
        self.exercises = [
            {"name": "1. Generador de contraseñas seguras", "file": "ejercicio1.py", 
             "desc": "Crea contraseñas seguras con múltiples caracteres"},
            {"name": "2. Calendario interactivo", "file": "ejercicio2.py", 
             "desc": "Muestra calendarios mensuales o anuales"},
            {"name": "3. Convertidor PDF ↔ Word", "file": "ejercicio3.py", 
             "desc": "Convierte entre formatos de documentos"},
            {"name": "4. Comparador de archivos", "file": "ejercicio4.py", 
             "desc": "Encuentra diferencias entre archivos de texto"},
            {"name": "5. Generador de códigos QR", "file": "ejercicio5.py", 
             "desc": "Crea códigos QR personalizados para URLs"},
            {"name": "6. Lista de compras", "file": "ejercicio6.py", 
             "desc": "Administra tu lista de compras interactiva"},
            {"name": "7. Adivina el número", "file": "ejercicio7.py", 
             "desc": "Juego de adivinanzas con pistas"},
            {"name": "8. Agenda de contactos", "file": "ejercicio8.py", 
             "desc": "Administra tus contactos y números telefónicos"},
            {"name": "9. Analizador de texto", "file": "ejercicio9.py", 
             "desc": "Analiza archivos de texto y cuenta palabras"},
            {"name": "10. Clasificador de imágenes", "file": "ejercicio10.py", 
             "desc": "Organiza imágenes por tamaño/resolución"}
        ]
        
        # Contenedor para la tabla
        table_frame = ttk.Frame(main_frame)
        table_frame.pack(fill=tk.BOTH, expand=True)
        
        # Crear Treeview con barras de desplazamiento
        scroll_y = ttk.Scrollbar(table_frame, orient=tk.VERTICAL)
        scroll_x = ttk.Scrollbar(table_frame, orient=tk.HORIZONTAL)
        
        self.tree = ttk.Treeview(
            table_frame,
            columns=('name', 'desc', 'file'),
            show='headings',
            yscrollcommand=scroll_y.set,
            xscrollcommand=scroll_x.set
        )
        
        # Configurar columnas
        self.tree.heading('name', text='Ejercicio', anchor=tk.W)
        self.tree.heading('desc', text='Descripción', anchor=tk.W)
        self.tree.heading('file', text='Archivo', anchor=tk.W)
        
        self.tree.column('name', width=250, minwidth=200, stretch=tk.NO)
        self.tree.column('desc', width=400, minwidth=300, stretch=tk.YES)
        self.tree.column('file', width=150, minwidth=100, stretch=tk.NO)
        
        # Configurar scrollbars
        scroll_y.config(command=self.tree.yview)
        scroll_x.config(command=self.tree.xview)
        
        # Posicionar elementos
        self.tree.grid(row=0, column=0, sticky='nsew')
        scroll_y.grid(row=0, column=1, sticky='ns')
        scroll_x.grid(row=1, column=0, sticky='ew')
        
        # Configurar grid para expansión
        table_frame.grid_rowconfigure(0, weight=1)
        table_frame.grid_columnconfigure(0, weight=1)
        
        # Insertar datos
        for exercise in self.exercises:
            self.tree.insert('', tk.END, values=(
                exercise['name'], 
                exercise['desc'],
                exercise['file']
            ))
        
        # Marco para botones
        button_frame = ttk.Frame(main_frame)
        button_frame.pack(fill=tk.X, pady=(20, 0))
        
        # Botones con estilo moderno
        run_btn = ttk.Button(
            button_frame,
            text="EJECUTAR EJERCICIO",
            style='Accent.TButton',
            command=self.run_exercise
        )
        run_btn.pack(side=tk.LEFT, padx=5, ipady=5)
        
        refresh_btn = ttk.Button(
            button_frame,
            text="ACTUALIZAR LISTA",
            style='Accent.TButton',
            command=self.refresh_list
        )
        refresh_btn.pack(side=tk.LEFT, padx=5, ipady=5)
        
        exit_btn = ttk.Button(
            button_frame,
            text="SALIR",
            style='Exit.TButton',
            command=self.on_close
        )
        exit_btn.pack(side=tk.RIGHT, padx=5, ipady=5)
        
        # Evento doble click para ejecutar
        self.tree.bind('<Double-1>', lambda event: self.run_exercise())
        
        # Evento Enter para ejecutar
        self.tree.bind('<Return>', lambda event: self.run_exercise())
    
    def run_exercise(self):
        """Ejecutar el ejercicio seleccionado"""
        selected_item = self.tree.focus()
        if not selected_item:
            messagebox.showwarning("Selección requerida", "Por favor seleccione un ejercicio de la lista")
            return
        
        item = self.tree.item(selected_item)
        exercise_file = item['values'][2]  # El archivo está en la tercera columna
        
        # Verificar si el archivo existe
        if not os.path.exists(exercise_file):
            messagebox.showerror(
                "Archivo no encontrado",
                f"No se pudo encontrar el archivo:\n{exercise_file}\n\n"
                "Asegúrese de que todos los archivos estén en el mismo directorio."
            )
            return
        
        try:
            # Ocultar la ventana principal temporalmente
            self.root.withdraw()
            
            # SOLUCIÓN: Usar el intérprete de Python actual
            python_exe = sys.executable
            
            # Ejecutar el script seleccionado
            if sys.platform == 'win32':
                # Para Windows
                subprocess.Popen(f'"{python_exe}" "{exercise_file}"', shell=True)
            else:
                # Para Linux/macOS
                subprocess.Popen([python_exe, exercise_file])
            
            # Mostrar la ventana principal nuevamente
            self.root.deiconify()
            
        except Exception as e:
            messagebox.showerror(
                "Error de ejecución",
                f"No se pudo ejecutar el ejercicio:\n\n{str(e)}"
            )
            self.root.deiconify()
    
    def refresh_list(self):
        """Actualizar la lista de ejercicios"""
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        for exercise in self.exercises:
            self.tree.insert('', tk.END, values=(
                exercise['name'], 
                exercise['desc'],
                exercise['file']
            ))
    
    def on_close(self):
        """Manejar el cierre de la aplicación"""
        if messagebox.askokcancel("Salir", "¿Está seguro que desea salir de la aplicación?"):
            self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = ModernIndexApp(root)
    root.mainloop()