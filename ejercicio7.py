"""
Ejercicio 7: Juego de adivinar el número con pistas.
Por: Leandro Marquez.
Para: Programación V - UBA.
"""
import tkinter as tk
from tkinter import messagebox
import random

def main_gui():
    def verificar_intento(event=None):
        nonlocal intentos
        try:
            intento = int(entry_intento.get())
            
            # Validar rango
            if intento < 1 or intento > 20:
                messagebox.showwarning("Fuera de rango", "El número debe estar entre 1 y 20")
                entry_intento.delete(0, tk.END)
                return
                
            intentos += 1
            label_intentos.config(text=f"Intentos: {intentos}")
            
            if intento < numero_secreto:
                resultado_var.set("¡Demasiado bajo! ⬇️")
                resultado_label.config(fg="#1976D2")  # Azul
            elif intento > numero_secreto:
                resultado_var.set("¡Demasiado alto! ⬆️")
                resultado_label.config(fg="#D32F2F")  # Rojo
            else:
                resultado_var.set(f"¡Correcto! 🎉")
                resultado_label.config(fg="#388E3C")  # Verde
                messagebox.showinfo("¡Felicidades!", 
                                  f"¡Adivinaste el número {numero_secreto} en {intentos} intentos!")
                reiniciar_juego()
                
            entry_intento.delete(0, tk.END)
        except ValueError:
            messagebox.showerror("Error", "Por favor ingresa un número válido")
            entry_intento.delete(0, tk.END)

    def reiniciar_juego():
        nonlocal numero_secreto, intentos
        numero_secreto = random.randint(1, 20)
        intentos = 0
        resultado_var.set("Ingresa tu primer intento")
        resultado_label.config(fg="#333333")
        label_intentos.config(text="Intentos: 0")
        entry_intento.delete(0, tk.END)
        entry_intento.focus_set()

    # Inicialización del juego
    numero_secreto = random.randint(1, 20)
    intentos = 0
    
    root = tk.Tk()
    root.title("Adivina el Número")
    root.geometry("500x400")
    root.resizable(False, False)
    
    # Frame principal
    main_frame = tk.Frame(root, padx=30, pady=30)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Título del juego
    tk.Label(main_frame, text="🔢 ADIVINA EL NÚMERO", 
            font=("Arial", 16, "bold"), fg="#5D4037").pack(pady=(0, 15))
    
    # Instrucciones
    tk.Label(main_frame, 
            text="Estoy pensando en un número entre 1 y 20.\n¡Adivina cuál es!",
            font=("Arial", 11), fg="#555555").pack(pady=(0, 20))
    
    # Contador de intentos
    intentos_frame = tk.Frame(main_frame)
    intentos_frame.pack(fill=tk.X, pady=(0, 15))
    
    label_intentos = tk.Label(intentos_frame, text=f"Intentos: {intentos}", 
                            font=("Arial", 11, "bold"), fg="#7B1FA2")
    label_intentos.pack(side=tk.LEFT)
    
    # Número secreto (solo para depuración)
    # tk.Label(intentos_frame, text=f"(Número secreto: {numero_secreto})", 
    #         font=("Arial", 9), fg="#AAAAAA").pack(side=tk.RIGHT)
    
    # Entrada de intento
    input_frame = tk.Frame(main_frame)
    input_frame.pack(fill=tk.X, pady=(0, 15))
    
    tk.Label(input_frame, text="Tu intento (1-20):", 
            font=("Arial", 11)).pack(anchor="w")
    
    entry_intento = tk.Entry(input_frame, font=("Arial", 14), justify="center")
    entry_intento.pack(fill=tk.X, pady=10)
    entry_intento.focus_set()
    entry_intento.bind("<Return>", verificar_intento)
    
    # Botón de verificación
    btn_verificar = tk.Button(main_frame, text="🔍 Verificar Intento", 
                            command=verificar_intento, bg="#303F9F", fg="white",
                            font=("Arial", 11, "bold"), padx=15, pady=8)
    btn_verificar.pack(pady=(10, 20))
    
    # Resultado
    resultado_frame = tk.Frame(main_frame)
    resultado_frame.pack(fill=tk.X, pady=(10, 15))
    
    resultado_var = tk.StringVar(value="Ingresa tu primer intento")
    resultado_label = tk.Label(resultado_frame, textvariable=resultado_var, 
                             font=("Arial", 12, "bold"), fg="#333333")
    resultado_label.pack()
    
    # Botón de reinicio
    btn_reiniciar = tk.Button(main_frame, text="🔄 Nuevo Juego", 
                            command=reiniciar_juego, bg="#F57C00", fg="white",
                            font=("Arial", 10))
    btn_reiniciar.pack(pady=(20, 0))
    
    root.mainloop()

if __name__ == "__main__":
    main_gui()