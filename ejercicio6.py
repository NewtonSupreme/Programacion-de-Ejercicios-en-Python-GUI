"""
Ejercicio 6: Programa de lista de compras interactiva.
Por: Leandro Marquez.
Para: Programación V - UBA.
"""
import tkinter as tk
from tkinter import messagebox, scrolledtext

def main_gui():
    def agregar_elemento(event=None):
        elemento = entry_elemento.get().strip()
        
        # Validar entrada vacía
        if not elemento:
            messagebox.showwarning("Entrada vacía", "Por favor ingresa un elemento válido")
            return
            
        # Finalizar si se ingresa 'fin'
        if elemento.lower() == "fin":
            finalizar()
            return
            
        # Agregar a la lista y actualizar
        lista_compras.append(elemento)
        actualizar_lista()
        entry_elemento.delete(0, tk.END)
        
    def actualizar_lista():
        lista_texto.configure(state='normal')
        lista_texto.delete(1.0, tk.END)
        for i, elemento in enumerate(lista_compras, 1):
            lista_texto.insert(tk.END, f"{i}. {elemento}\n")
        lista_texto.configure(state='disabled')
        
    def finalizar():
        if not lista_compras:
            messagebox.showinfo("Lista vacía", "No se agregaron elementos a la lista")
        else:
            # Mostrar lista completa en un cuadro de diálogo
            lista_completa = "\n".join(f"{i}. {item}" for i, item in enumerate(lista_compras, 1))
            messagebox.showinfo("Lista de Compras Completa", 
                               f"Elementos en tu lista:\n\n{lista_completa}")
        root.destroy()

    # Configuración inicial
    lista_compras = []
    
    root = tk.Tk()
    root.title("Lista de Compras")
    root.geometry("500x450")
    root.resizable(True, True)
    
    # Frame principal con padding
    main_frame = tk.Frame(root, padx=20, pady=20)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Título
    tk.Label(main_frame, text="🛒 LISTA DE COMPRAS", 
            font=("Arial", 14, "bold"), fg="#2E7D32").pack(pady=10)
    
    # Instrucciones
    instrucciones = tk.Label(main_frame, 
                            text="Ingresa los elementos uno por uno.\nEscribe 'fin' para terminar.",
                            font=("Arial", 10), fg="#555555")
    instrucciones.pack(pady=(0, 15))
    
    # Entrada de elementos
    input_frame = tk.Frame(main_frame)
    input_frame.pack(fill=tk.X, pady=(0, 15))
    
    tk.Label(input_frame, text="Elemento:", font=("Arial", 10)).pack(anchor="w")
    
    entry_frame = tk.Frame(input_frame)
    entry_frame.pack(fill=tk.X, pady=5)
    
    entry_elemento = tk.Entry(entry_frame, font=("Arial", 11))
    entry_elemento.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))
    entry_elemento.focus_set()  # Foco inicial en la entrada
    entry_elemento.bind("<Return>", agregar_elemento)  # Enter para agregar
    
    btn_agregar = tk.Button(entry_frame, text="➕ Agregar", command=agregar_elemento,
                           bg="#4CAF50", fg="white", font=("Arial", 10))
    btn_agregar.pack(side=tk.RIGHT)
    
    # Lista de elementos
    tk.Label(main_frame, text="Elementos agregados:", 
            font=("Arial", 10, "bold")).pack(anchor="w", pady=(10, 5))
    
    lista_frame = tk.Frame(main_frame)
    lista_frame.pack(fill=tk.BOTH, expand=True)
    
    # Usamos ScrolledText para listas largas
    lista_texto = scrolledtext.ScrolledText(lista_frame, font=("Arial", 10),
                                          height=10, wrap=tk.WORD, state='disabled')
    lista_texto.pack(fill=tk.BOTH, expand=True)
    
    # Botón de finalización
    btn_frame = tk.Frame(main_frame)
    btn_frame.pack(fill=tk.X, pady=15)
    
    btn_finalizar = tk.Button(btn_frame, text="✅ Finalizar Lista", command=finalizar,
                            bg="#FF9800", fg="white", font=("Arial", 10, "bold"))
    btn_finalizar.pack(pady=10)
    
    # Manejar cierre de ventana
    root.protocol("WM_DELETE_WINDOW", finalizar)
    
    root.mainloop()

if __name__ == "__main__":
    main_gui()