"""
Ejercicio 9: Analizador de archivos de texto que cuenta palabras y frecuencias.
Por: Leandro Marquez.
Para: Programación V - UBA.
"""
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from collections import Counter
import os

def main_gui():
    def abrir_archivo():
        archivo = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if archivo:
            entry_archivo.delete(0, tk.END)
            entry_archivo.insert(0, archivo)
            analizar_archivo(archivo)
            
    def analizar_archivo(archivo):
        try:
            with open(archivo, 'r', encoding='utf-8') as file:
                contenido = file.read()
                
            palabras = contenido.split()
            total_palabras = len(palabras)
            
            # Contar frecuencia de palabras
            frecuencia = Counter(palabras)
            palabras_comunes = frecuencia.most_common(10)
            
            # Actualizar resultados
            label_total.config(text=f"Total de palabras: {total_palabras}")
            
            # Limpiar tabla
            for row in tree.get_children():
                tree.delete(row)
                
            # Llenar tabla con palabras más comunes
            for i, (palabra, count) in enumerate(palabras_comunes, 1):
                tree.insert("", tk.END, values=(i, palabra, count))
                
        except FileNotFoundError:
            messagebox.showerror("Error", "Archivo no encontrado")
        except Exception as e:
            messagebox.showerror("Error", f"Error al procesar el archivo:\n{str(e)}")

    root = tk.Tk()
    root.title("📊 Analizador de Texto")
    root.geometry("700x550")
    
    # Frame principal con estilo
    main_frame = tk.Frame(root, bg="#F5F5F5", padx=25, pady=25)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Título
    tk.Label(main_frame, text="🔠 ANALIZADOR DE TEXTO", 
            font=("Arial", 16, "bold"), bg="#F5F5F5", fg="#3F51B5").pack(pady=(0, 10))
    
    tk.Label(main_frame, text="Analiza archivos de texto contando palabras y frecuencias", 
            font=("Arial", 10), bg="#F5F5F5", fg="#666666").pack(pady=(0, 20))
    
    # Selección de archivo
    file_frame = tk.Frame(main_frame, bg="#F5F5F5")
    file_frame.pack(fill=tk.X, pady=(0, 15))
    
    tk.Label(file_frame, text="Archivo de texto:", 
            font=("Arial", 11, "bold"), bg="#F5F5F5").pack(anchor="w", pady=(0, 5))
    
    # Entrada y botón de examinar
    input_frame = tk.Frame(file_frame, bg="#F5F5F5")
    input_frame.pack(fill=tk.X)
    
    entry_archivo = tk.Entry(input_frame, font=("Arial", 10))
    entry_archivo.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
    
    btn_examinar = tk.Button(input_frame, text="📂 Examinar", 
                           command=abrir_archivo,
                           bg="#2196F3", fg="white", font=("Arial", 10))
    btn_examinar.pack(side=tk.RIGHT)
    
    # Resultados
    results_frame = tk.Frame(main_frame, bg="#F5F5F5")
    results_frame.pack(fill=tk.BOTH, expand=True, pady=(15, 0))
    
    # Estadísticas generales
    stats_frame = tk.Frame(results_frame, bg="#FFFFFF", bd=1, relief="solid", padx=15, pady=10)
    stats_frame.pack(fill=tk.X, pady=(0, 15))
    
    label_total = tk.Label(stats_frame, text="Total de palabras: 0", 
                         font=("Arial", 11, "bold"), bg="#FFFFFF")
    label_total.pack(anchor="w")
    
    # Palabras frecuentes
    tk.Label(results_frame, text="🔝 TOP 10 PALABRAS MÁS FRECUENTES", 
            font=("Arial", 11, "bold"), bg="#F5F5F5").pack(anchor="w", pady=(0, 5))
    
    # Contenedor para la tabla
    table_container = tk.Frame(results_frame, bd=1, relief="solid")
    table_container.pack(fill=tk.BOTH, expand=True)
    
    # Tabla de palabras frecuentes
    columns = ("#", "Palabra", "Frecuencia")
    tree = ttk.Treeview(table_container, columns=columns, show="headings", height=10)
    
    # Configurar columnas
    tree.heading("#", text="#")
    tree.heading("Palabra", text="Palabra")
    tree.heading("Frecuencia", text="Frecuencia")
    
    tree.column("#", width=50, anchor="center")
    tree.column("Palabra", width=200, anchor="w")
    tree.column("Frecuencia", width=100, anchor="center")
    
    # Barra de desplazamiento
    scrollbar = ttk.Scrollbar(table_container, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    
    tree.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    # Estilo para la tabla
    style = ttk.Style()
    style.configure("Treeview", font=("Arial", 10), rowheight=25)
    style.configure("Treeview.Heading", font=("Arial", 10, "bold"))
    style.map("Treeview", background=[("selected", "#3F51B5")])
    
    root.mainloop()

if __name__ == "__main__":
    main_gui()