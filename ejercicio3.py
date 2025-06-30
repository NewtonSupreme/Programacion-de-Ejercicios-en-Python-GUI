"""
Ejercicio 3: Convertidor de archivos entre PDF y Word.
Por: Leandro Marquez.
Para: Programación V - UBA.
"""
import tkinter as tk
from tkinter import filedialog, messagebox
from pdf2docx import Converter
from docx2pdf import convert
import os

def main_gui():
    def seleccionar_archivo():
        archivo = filedialog.askopenfilename(
            filetypes=[("PDF", "*.pdf"), ("Word", "*.docx"), ("Todos", "*.*")]
        )
        if archivo:
            entry_archivo.delete(0, tk.END)
            entry_archivo.insert(0, archivo)
            actualizar_boton_convertir()

    def actualizar_boton_convertir():
        archivo = entry_archivo.get()
        if archivo.lower().endswith('.pdf'):
            btn_convertir.config(text="🔄 Convertir PDF a Word", bg="#2196F3")
        elif archivo.lower().endswith('.docx'):
            btn_convertir.config(text="🔄 Convertir Word a PDF", bg="#4CAF50")
        else:
            btn_convertir.config(text="Convertir", bg="#9E9E9E")

    def convertir():
        archivo_entrada = entry_archivo.get()
        if not archivo_entrada:
            messagebox.showwarning("Error", "Seleccione un archivo primero")
            return
            
        if archivo_entrada.lower().endswith('.pdf'):
            # Convertir PDF a Word
            archivo_salida = os.path.splitext(archivo_entrada)[0] + ".docx"
            try:
                cv = Converter(archivo_entrada)
                cv.convert(archivo_salida)
                cv.close()
                messagebox.showinfo("Éxito", f"Archivo convertido con éxito:\n{archivo_salida}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo convertir el archivo:\n{str(e)}")
                
        elif archivo_entrada.lower().endswith('.docx'):
            # Convertir Word a PDF
            archivo_salida = os.path.splitext(archivo_entrada)[0] + ".pdf"
            try:
                convert(archivo_entrada, archivo_salida)
                messagebox.showinfo("Éxito", f"Archivo convertido con éxito:\n{archivo_salida}")
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo convertir el archivo:\n{str(e)}")
        else:
            messagebox.showwarning("Error", "Formato de archivo no soportado")

    root = tk.Tk()
    root.title("📄 Convertidor PDF/Word")
    root.geometry("600x300")
    root.resizable(False, False)
    
    # Frame principal con estilo
    main_frame = tk.Frame(root, bg="#F5F5F5", padx=30, pady=30)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Título
    tk.Label(main_frame, text="🔄 CONVERTIDOR PDF/WORD", 
            font=("Arial", 16, "bold"), bg="#F5F5F5", fg="#3F51B5").pack(pady=(0, 15))
    
    tk.Label(main_frame, text="Convierte archivos entre formatos PDF y Word", 
            font=("Arial", 10), bg="#F5F5F5", fg="#666666").pack(pady=(0, 25))
    
    # Contenedor para selección de archivo
    file_frame = tk.Frame(main_frame, bg="#F5F5F5")
    file_frame.pack(fill=tk.X, pady=(0, 20))
    
    tk.Label(file_frame, text="Seleccionar archivo:", 
            font=("Arial", 11, "bold"), bg="#F5F5F5").pack(anchor="w", pady=(0, 5))
    
    # Entrada y botón de examinar
    input_frame = tk.Frame(file_frame, bg="#F5F5F5")
    input_frame.pack(fill=tk.X)
    
    entry_archivo = tk.Entry(input_frame, font=("Arial", 10))
    entry_archivo.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
    
    btn_examinar = tk.Button(input_frame, text="📂 Examinar", 
                           command=seleccionar_archivo,
                           bg="#FF9800", fg="white", font=("Arial", 10))
    btn_examinar.pack(side=tk.RIGHT)
    
    # Botón de conversión
    btn_convertir = tk.Button(main_frame, text="Seleccione un archivo para convertir", 
                            command=convertir, 
                            bg="#9E9E9E", fg="white", 
                            font=("Arial", 12, "bold"),
                            padx=15, pady=10, state="normal")
    btn_convertir.pack(fill=tk.X, pady=(20, 10))
    
    # Información
    info_frame = tk.Frame(main_frame, bg="#F5F5F5")
    info_frame.pack(fill=tk.X, pady=(15, 0))
    
    tk.Label(info_frame, text="Formatos soportados:", 
            font=("Arial", 9, "bold"), bg="#F5F5F5").pack(anchor="w", side=tk.LEFT)
    
    tk.Label(info_frame, text="PDF → Word  |  Word → PDF", 
            font=("Arial", 9), bg="#F5F5F5", fg="#2196F3").pack(anchor="w", side=tk.LEFT, padx=5)
    
    root.mainloop()

if __name__ == "__main__":
    main_gui()