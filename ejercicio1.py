"""
Ejercicio 1: Generador de contraseñas seguras con opciones personalizadas
Por: Leandro Marquez.
Para: Programación V - UBA.
"""
import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

def generar_contraseña(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):
    caracteres = ""
    
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    
    if not caracteres:
        messagebox.showwarning("Advertencia", "Debe seleccionar al menos un tipo de carácter")
        return ""
    
    # Asegurar que la contraseña tenga al menos un carácter de cada tipo seleccionado
    contraseña = []
    if incluir_mayusculas:
        contraseña.append(random.choice(string.ascii_uppercase))
    if incluir_minusculas:
        contraseña.append(random.choice(string.ascii_lowercase))
    if incluir_numeros:
        contraseña.append(random.choice(string.digits))
    if incluir_simbolos:
        contraseña.append(random.choice(string.punctuation))
    
    # Completar el resto de la contraseña con caracteres aleatorios
    for _ in range(longitud - len(contraseña)):
        contraseña.append(random.choice(caracteres))
    
    # Mezclar los caracteres
    random.shuffle(contraseña)
    return ''.join(contraseña)

def main_gui():
    def generar():
        try:
            longitud = int(entry_longitud.get())
            if longitud < 8:
                messagebox.showwarning("Longitud inválida", "La longitud mínima es 8 caracteres")
                return
                
            # Obtener selecciones del usuario
            incluir_mayusculas = var_mayusculas.get()
            incluir_minusculas = var_minusculas.get()
            incluir_numeros = var_numeros.get()
            incluir_simbolos = var_simbolos.get()
            
            # Validar que se haya seleccionado al menos un tipo
            if not any([incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos]):
                messagebox.showwarning("Selección requerida", "Debe seleccionar al menos un tipo de carácter")
                return
                
            contraseña = generar_contraseña(
                longitud,
                incluir_mayusculas,
                incluir_minusculas,
                incluir_numeros,
                incluir_simbolos
            )
            
            if contraseña:  # Solo actualizar si se generó una contraseña válida
                resultado_var.set(contraseña)
                
        except ValueError:
            messagebox.showerror("Error", "Por favor ingrese un número válido para la longitud")

    # Configuración de la ventana
    root = tk.Tk()
    root.title("Generador de Contraseñas Seguras")
    root.geometry("600x500")
    root.resizable(False, False)
    
    # Estilo
    style = ttk.Style()
    style.configure('TFrame', background='#f0f5ff')
    style.configure('TLabel', background='#f0f5ff', font=('Arial', 10))
    style.configure('TCheckbutton', background='#f0f5ff', font=('Arial', 10))
    style.configure('TButton', font=('Arial', 10, 'bold'))
    
    # Contenedor principal
    main_frame = ttk.Frame(root, padding=20)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Título
    title_label = ttk.Label(
        main_frame, 
        text="Generador de Contraseñas Seguras",
        font=("Arial", 14, "bold"),
        foreground="#2c3e50"
    )
    title_label.pack(pady=(0, 20))
    
    # Configuración de longitud
    length_frame = ttk.Frame(main_frame)
    length_frame.pack(fill=tk.X, pady=(0, 15))
    
    ttk.Label(length_frame, text="Longitud de la contraseña (8-50):").pack(side=tk.LEFT)
    entry_longitud = ttk.Entry(length_frame, width=5, font=("Arial", 10))
    entry_longitud.insert(0, "12")
    entry_longitud.pack(side=tk.LEFT, padx=10)
    
    # Tipos de caracteres
    types_frame = ttk.LabelFrame(main_frame, text="Tipos de caracteres a incluir", padding=10)
    types_frame.pack(fill=tk.X, pady=(0, 15))
    
    var_mayusculas = tk.BooleanVar(value=True)
    ttk.Checkbutton(types_frame, text="Letras mayúsculas (A-Z)", variable=var_mayusculas).pack(anchor="w", pady=2)
    
    var_minusculas = tk.BooleanVar(value=True)
    ttk.Checkbutton(types_frame, text="Letras minúsculas (a-z)", variable=var_minusculas).pack(anchor="w", pady=2)
    
    var_numeros = tk.BooleanVar(value=True)
    ttk.Checkbutton(types_frame, text="Números (0-9)", variable=var_numeros).pack(anchor="w", pady=2)
    
    var_simbolos = tk.BooleanVar(value=True)
    ttk.Checkbutton(types_frame, text="Símbolos especiales (!@#$%^&* etc.)", variable=var_simbolos).pack(anchor="w", pady=2)
    
    # Botón de generación
    generate_btn = ttk.Button(
        main_frame,
        text="Generar Contraseña",
        command=generar,
        style='TButton'
    )
    generate_btn.pack(pady=(10, 15))
    
    # Resultado
    result_frame = ttk.Frame(main_frame)
    result_frame.pack(fill=tk.X, pady=(0, 15))
    
    ttk.Label(result_frame, text="Contraseña generada:", font=("Arial", 10, "bold")).pack(anchor="w", pady=(0, 5))
    
    resultado_var = tk.StringVar()
    result_entry = ttk.Entry(
        result_frame, 
        textvariable=resultado_var, 
        state="readonly",
        font=("Arial", 12, "bold"),
        width=40
    )
    result_entry.pack(fill=tk.X)
    
    # Botones adicionales
    btn_frame = ttk.Frame(main_frame)
    btn_frame.pack(fill=tk.X)
    
    def copiar_portapapeles():
        if resultado_var.get():
            root.clipboard_clear()
            root.clipboard_append(resultado_var.get())
            messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles")
        else:
            messagebox.showwarning("Advertencia", "Primero genere una contraseña")
    
    copy_btn = ttk.Button(
        btn_frame,
        text="Copiar Contraseña",
        command=copiar_portapapeles
    )
    copy_btn.pack(side=tk.LEFT, padx=5)
    
    close_btn = ttk.Button(
        btn_frame,
        text="Cerrar",
        command=root.destroy
    )
    close_btn.pack(side=tk.RIGHT, padx=5)
    
    root.mainloop()

if __name__ == "__main__":
    main_gui()