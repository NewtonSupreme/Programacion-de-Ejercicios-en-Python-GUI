"""
Ejercicio 5: Generador de códigos QR personalizados.
Por: Leandro Marquez.
Para: Programación V - UBA.
"""
import tkinter as tk
from tkinter import messagebox, colorchooser
import qrcode
from PIL import ImageTk, Image
import os

def main_gui():
    def generar_qr():
        url = "https://www.python.org"
        try:
            tamaño = int(entry_tamaño.get())
            if tamaño < 1 or tamaño > 20:
                messagebox.showwarning("Tamaño inválido", "El tamaño debe estar entre 1 y 20")
                return
        except ValueError:
            messagebox.showerror("Error", "Tamaño inválido")
            return
            
        color = color_var.get()
        try:
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=tamaño,
                border=4,
            )
            qr.add_data(url)
            qr.make(fit=True)
            
            img = qr.make_image(fill_color=color, back_color="white")
            img.save("python_qr.png")
            
            # Mostrar imagen generada
            img_tk = ImageTk.PhotoImage(Image.open("python_qr.png").resize((200, 200)))
            qr_label.config(image=img_tk)
            qr_label.image = img_tk
            
            messagebox.showinfo("Éxito", "Código QR generado como 'python_qr.png'")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el QR:\n{str(e)}")

    def seleccionar_color():
        color = colorchooser.askcolor(title="Seleccione un color")[1]
        if color:
            color_var.set(color)
            color_btn.config(bg=color, fg="white" if color != "#000000" else "white")

    root = tk.Tk()
    root.title("🔄 Generador de Códigos QR")
    root.geometry("550x550")
    root.resizable(False, False)
    
    # Frame principal con estilo
    main_frame = tk.Frame(root, bg="#F5F5F5", padx=25, pady=25)
    main_frame.pack(fill=tk.BOTH, expand=True)
    
    # Título
    tk.Label(main_frame, text="🔢 GENERADOR DE CÓDIGOS QR", 
            font=("Arial", 16, "bold"), bg="#F5F5F5", fg="#3F51B5").pack(pady=(0, 15))
    
    tk.Label(main_frame, text="Personaliza tu código QR para la URL de Python", 
            font=("Arial", 10), bg="#F5F5F5", fg="#666666").pack(pady=(0, 20))
    
    # Configuración del tamaño
    size_frame = tk.Frame(main_frame, bg="#F5F5F5")
    size_frame.pack(fill=tk.X, pady=(0, 15))
    
    tk.Label(size_frame, text="Tamaño del QR (1-20):", 
            font=("Arial", 11), bg="#F5F5F5").grid(row=0, column=0, sticky="w", padx=(0, 10))
    
    entry_tamaño = tk.Entry(size_frame, font=("Arial", 11), width=5, justify="center")
    entry_tamaño.insert(0, "10")
    entry_tamaño.grid(row=0, column=1, sticky="w")
    
    # Configuración del color
    color_frame = tk.Frame(main_frame, bg="#F5F5F5")
    color_frame.pack(fill=tk.X, pady=(0, 25))
    
    tk.Label(color_frame, text="Color del QR:", 
            font=("Arial", 11), bg="#F5F5F5").grid(row=0, column=0, sticky="w", padx=(0, 10))
    
    color_var = tk.StringVar(value="#000000")
    
    color_btn = tk.Button(color_frame, text="Seleccionar Color", 
                         command=seleccionar_color, 
                         bg="#000000", fg="white",
                         font=("Arial", 10))
    color_btn.grid(row=0, column=1, sticky="w")
    
    # Botón de generación
    btn_generar = tk.Button(main_frame, text="🔄 Generar Código QR", 
                          command=generar_qr, 
                          bg="#4CAF50", fg="white", 
                          font=("Arial", 12, "bold"),
                          padx=15, pady=8)
    btn_generar.pack(pady=(0, 25))
    
    # Área para mostrar el QR
    qr_container = tk.Frame(main_frame, bg="#FFFFFF", bd=1, relief="solid")
    qr_container.pack(pady=(0, 15), fill=tk.BOTH, expand=True)
    
    qr_label = tk.Label(qr_container, bg="#FFFFFF")
    qr_label.pack(pady=20, padx=20)
    
    # Nota
    tk.Label(main_frame, text="El código QR se guardará como 'python_qr.png' en el directorio actual", 
            font=("Arial", 9), bg="#F5F5F5", fg="#666666").pack()
    
    root.mainloop()

if __name__ == "__main__":
    main_gui()