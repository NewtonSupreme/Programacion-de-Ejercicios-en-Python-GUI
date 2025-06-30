"""
Ejercicio 10: Clasificador de imágenes por tamaño/resolución.
Por: Leandro Marquez.
Para: Programación V - UBA.
"""
import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from PIL import Image
import os
import shutil
import time
import threading

def main_gui():
    def seleccionar_directorio():
        directorio = filedialog.askdirectory()
        if directorio:
            entry_directorio.delete(0, tk.END)
            entry_directorio.insert(0, directorio)
            actualizar_boton()
            
    def actualizar_boton():
        if entry_directorio.get():
            btn_clasificar.config(state="normal", bg="#4CAF50", fg="white")
        else:
            btn_clasificar.config(state="normal", bg="#9E9E9E", fg="white")
            
    def iniciar_clasificacion():
        # Deshabilitar botón durante la operación
        btn_clasificar.config(state="disabled", text="Clasificando...", bg="#FF9800")
        progress_bar.pack(pady=10)
        progress_bar['value'] = 0
        
        # Crear un hilo para la clasificación
        threading.Thread(target=clasificar_imagenes).start()
            
    def clasificar_imagenes():
        directorio = entry_directorio.get()
        if not directorio:
            messagebox.showwarning("Error", "Selecciona un directorio")
            return
            
        try:
            # Crear categorías
            categorias = {
                "pequeñas": (0, 800),
                "medianas": (800, 2000),
                "grandes": (2000, float('inf'))
            }
            
            # Crear subdirectorios si no existen
            for categoria in categorias:
                os.makedirs(os.path.join(directorio, categoria), exist_ok=True)
            
            # Obtener lista de imágenes
            imagenes = [f for f in os.listdir(directorio) 
                       if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.bmp'))]
            
            total = len(imagenes)
            clasificadas = 0
            errores = []
            
            # Procesar imágenes
            for i, archivo in enumerate(imagenes):
                ruta_completa = os.path.join(directorio, archivo)
                
                try:
                    # Actualizar barra de progreso
                    progress = (i + 1) / total * 100
                    root.after(0, lambda v=progress: progress_bar.config(value=v))
                    
                    # Leer resolución
                    with Image.open(ruta_completa) as img:
                        ancho, alto = img.size
                        resolucion = max(ancho, alto)
                    
                    # Determinar categoría
                    categoria_destino = None
                    for categoria, (min_res, max_res) in categorias.items():
                        if min_res <= resolucion < max_res:
                            categoria_destino = categoria
                            break
                    
                    if categoria_destino:
                        destino = os.path.join(directorio, categoria_destino, archivo)
                        
                        # Intentar mover con reintentos
                        for intento in range(3):
                            try:
                                shutil.move(ruta_completa, destino)
                                clasificadas += 1
                                break
                            except PermissionError:
                                if intento < 2:
                                    time.sleep(0.5)  # Esperar medio segundo
                                else:
                                    errores.append(f"{archivo} (archivo bloqueado)")
                            except Exception as e:
                                errores.append(f"{archivo}: {str(e)}")
                                break
                except Exception as e:
                    errores.append(f"{archivo}: {str(e)}")
        
            # Mostrar resultados
            mensaje = f"✅ Proceso completado!\n\n" \
                     f"Imágenes procesadas: {total}\n" \
                     f"Imágenes clasificadas: {clasificadas}\n" \
                     f"Subdirectorios creados: {', '.join(categorias.keys())}"
            
            if errores:
                # CORRECCIÓN: Cambiado 'erres' por 'errores'
                mensaje += f"\n\n⚠️ Errores ({len(errores)}):\n- " + "\n- ".join(errores[:5])
                if len(errores) > 5:
                    mensaje += f"\n... y {len(errores)-5} errores más"
            
            root.after(0, lambda: mostrar_resultado(mensaje))
            
        except Exception as e:
            root.after(0, lambda: messagebox.showerror("Error", f"❌ No se pudieron clasificar las imágenes:\n{str(e)}"))
    
    def mostrar_resultado(mensaje):
        progress_bar.pack_forget()
        btn_clasificar.config(state="normal", text="🗂️ Clasificar Imágenes", bg="#4CAF50")
        messagebox.showinfo("Resultado", mensaje)

    root = tk.Tk()
    root.title("🖼️ Clasificador de Imágenes")
    root.geometry("650x450")
    root.resizable(False, False)
    
    # Frame principal con estilo
    main_frame = tk.Frame(root, bg="#F5F5F5", padx=30, pady=30)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Título
    tk.Label(main_frame, text="🖼️ CLASIFICADOR DE IMÁGENES", 
            font=("Arial", 16, "bold"), bg="#F5F5F5", fg="#3F51B5").pack(pady=(0, 10))
    
    tk.Label(main_frame, text="Organiza imágenes por tamaño/resolución en subdirectorios", 
            font=("Arial", 10), bg="#F5F5F5", fg="#666666").pack(pady=(0, 20))
    
    # Selección de directorio
    tk.Label(main_frame, text="Directorio con imágenes:", 
            font=("Arial", 11, "bold"), bg="#F5F5F5").pack(anchor="w", pady=(0, 5))
    
    dir_frame = tk.Frame(main_frame, bg="#F5F5F5")
    dir_frame.pack(fill=tk.X, pady=(0, 15))
    
    entry_directorio = tk.Entry(dir_frame, font=("Arial", 10))
    entry_directorio.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
    
    btn_examinar = tk.Button(dir_frame, text="📂 Examinar", 
                           command=seleccionar_directorio,
                           bg="#2196F3", fg="white", font=("Arial", 10))
    btn_examinar.pack(side=tk.RIGHT)
    
    # Información de categorías
    cat_frame = tk.Frame(main_frame, bg="#FFFFFF", bd=1, relief="solid", padx=15, pady=10)
    cat_frame.pack(fill=tk.X, pady=(0, 20))
    
    tk.Label(cat_frame, text="Categorías de clasificación:", 
            font=("Arial", 10, "bold"), bg="#FFFFFF").pack(anchor="w", pady=(0, 5))
    
    cats = [
        "🟢 Pequeñas: hasta 800px (ancho o alto)",
        "🟡 Medianas: entre 800px y 2000px",
        "🔴 Grandes: más de 2000px"
    ]
    
    for cat in cats:
        tk.Label(cat_frame, text=cat, font=("Arial", 9), bg="#FFFFFF", anchor="w").pack(anchor="w", padx=10)
    
    # Barra de progreso
    progress_bar = ttk.Progressbar(main_frame, orient="horizontal", length=400, mode="determinate")
    
    # Botón de clasificación
    btn_clasificar = tk.Button(main_frame, text="🗂️ Clasificar Imágenes", 
                             command=iniciar_clasificacion, 
                             state="normal", bg="#9E9E9E", fg="white", 
                             font=("Arial", 12, "bold"),
                             padx=15, pady=10)
    btn_clasificar.pack(pady=(10, 5), fill=tk.X)
    
    # Etiqueta de estado
    status_label = tk.Label(main_frame, text="Seleccione un directorio con imágenes", 
                          font=("Arial", 9), bg="#F5F5F5", fg="#666666")
    status_label.pack(pady=(5, 0))
    
    # Configurar actualización del botón
    entry_directorio.bind("<KeyRelease>", lambda e: actualizar_boton())
    
    root.mainloop()

if __name__ == "__main__":
    main_gui()