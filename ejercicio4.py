"""
Ejercicio 4: Comparador de archivos de texto que reporta diferencias línea por línea.
Por: Leandro Marquez.
Para: Programación V - UBA.
"""
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

def main_gui():
    def seleccionar_archivo(entry):
        archivo = filedialog.askopenfilename(filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if archivo:
            entry.delete(0, tk.END)
            entry.insert(0, archivo)

    def comparar():
        archivo1 = entry_archivo1.get()
        archivo2 = entry_archivo2.get()
        
        if not archivo1 or not archivo2:
            messagebox.showwarning("Error", "Seleccione ambos archivos")
            return
            
        try:
            with open(archivo1, 'r') as f1, open(archivo2, 'r') as f2:
                lineas1 = f1.readlines()
                lineas2 = f2.readlines()
                
            resultado.delete(1.0, tk.END)
            max_lineas = max(len(lineas1), len(lineas2))
            diferencias = []
            
            for i in range(max_lineas):
                linea1 = lineas1[i].strip() if i < len(lineas1) else ""
                linea2 = lineas2[i].strip() if i < len(lineas2) else ""
                
                if linea1 != linea2:
                    diferencias.append(f"Línea {i+1}:\n- Archivo 1: {linea1}\n- Archivo 2: {linea2}\n{'='*50}\n")
                    
            if diferencias:
                resultado.insert(tk.END, f"Se encontraron {len(diferencias)} diferencias:\n\n")
                for diff in diferencias:
                    resultado.insert(tk.END, diff)
            else:
                resultado.insert(tk.END, "Los archivos son idénticos")
                
        except Exception as e:
            messagebox.showerror("Error", f"No se pudieron comparar los archivos:\n{str(e)}")

    root = tk.Tk()
    root.title("🔍 Comparador de Archivos de Texto")
    root.geometry("800x600")
    
    # Frame principal con estilo
    main_frame = tk.Frame(root, bg="#F5F5F5", padx=25, pady=25)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Título
    tk.Label(main_frame, text="📄 COMPARADOR DE ARCHIVOS DE TEXTO", 
            font=("Arial", 16, "bold"), bg="#F5F5F5", fg="#3F51B5").pack(pady=(0, 15))
    
    tk.Label(main_frame, text="Compara dos archivos de texto y encuentra diferencias línea por línea", 
            font=("Arial", 10), bg="#F5F5F5", fg="#666666").pack(pady=(0, 25))
    
    # Contenedor para los archivos
    files_frame = tk.Frame(main_frame, bg="#F5F5F5")
    files_frame.pack(fill=tk.X, pady=(0, 20))
    
    # Archivo 1
    file1_frame = tk.Frame(files_frame, bg="#F5F5F5")
    file1_frame.pack(fill=tk.X, pady=(0, 15))
    
    tk.Label(file1_frame, text="Archivo 1:", 
            font=("Arial", 11, "bold"), bg="#F5F5F5").pack(anchor="w", pady=(0, 5))
    
    entry_frame1 = tk.Frame(file1_frame, bg="#F5F5F5")
    entry_frame1.pack(fill=tk.X)
    
    entry_archivo1 = tk.Entry(entry_frame1, font=("Arial", 10))
    entry_archivo1.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
    
    btn_examinar1 = tk.Button(entry_frame1, text="📂 Examinar", 
                            command=lambda: seleccionar_archivo(entry_archivo1),
                            bg="#2196F3", fg="white", font=("Arial", 10))
    btn_examinar1.pack(side=tk.RIGHT)
    
    # Archivo 2
    file2_frame = tk.Frame(files_frame, bg="#F5F5F5")
    file2_frame.pack(fill=tk.X, pady=(0, 15))
    
    tk.Label(file2_frame, text="Archivo 2:", 
            font=("Arial", 11, "bold"), bg="#F5F5F5").pack(anchor="w", pady=(0, 5))
    
    entry_frame2 = tk.Frame(file2_frame, bg="#F5F5F5")
    entry_frame2.pack(fill=tk.X)
    
    entry_archivo2 = tk.Entry(entry_frame2, font=("Arial", 10))
    entry_archivo2.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
    
    btn_examinar2 = tk.Button(entry_frame2, text="📂 Examinar", 
                            command=lambda: seleccionar_archivo(entry_archivo2),
                            bg="#2196F3", fg="white", font=("Arial", 10))
    btn_examinar2.pack(side=tk.RIGHT)
    
    # Botón de comparación
    btn_frame = tk.Frame(main_frame, bg="#F5F5F5")
    btn_frame.pack(fill=tk.X, pady=(10, 15))
    
    btn_comparar = tk.Button(btn_frame, text="🔍 Comparar Archivos", 
                           command=comparar, 
                           bg="#4CAF50", fg="white", 
                           font=("Arial", 12, "bold"),
                           padx=15, pady=8)
    btn_comparar.pack(pady=10)
    
    # Resultado
    tk.Label(main_frame, text="Resultado de la comparación:", 
            font=("Arial", 11, "bold"), bg="#F5F5F5").pack(anchor="w", pady=(0, 5))
    
    # Contenedor para el área de texto
    result_container = tk.Frame(main_frame, bd=2, relief="groove")
    result_container.pack(fill=tk.BOTH, expand=True)
    
    resultado = ScrolledText(result_container, font=("Consolas", 10), wrap=tk.WORD)
    resultado.pack(fill=tk.BOTH, expand=True, padx=2, pady=2)
    
    # Configurar tags para mejor visualización
    resultado.tag_configure("diferencia", foreground="#D32F2F")
    resultado.tag_configure("identico", foreground="#388E3C", font=("Arial", 11, "bold"))
    
    root.mainloop()

if __name__ == "__main__":
    main_gui()