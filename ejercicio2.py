"""
Programa que muestra un calendario (mes o año completo) según la selección del usuario.
Por: Leandro Marquez.
Para: Programación V.
"""
import tkinter as tk
from tkinter import ttk
import calendar
import locale

# Configurar el locale para español
try:
    locale.setlocale(locale.LC_TIME, 'es_ES.UTF-8')
except:
    try:
        locale.setlocale(locale.LC_TIME, 'spanish')
    except:
        print("Advertencia: No se pudo configurar el locale en español")

def main_gui():
    def mostrar_calendario():
        try:
            año = int(entry_año.get())
            if opcion_var.get() == 'M':
                mes = combo_mes.current() + 1
                # Calendario en español
                cal = calendar.month(año, mes)
                # Reemplazar nombres en inglés por español si es necesario
                cal = cal.replace("January", "Enero").replace("February", "Febrero") \
                         .replace("March", "Marzo").replace("April", "Abril") \
                         .replace("May", "Mayo").replace("June", "Junio") \
                         .replace("July", "Julio").replace("August", "Agosto") \
                         .replace("September", "Septiembre").replace("October", "Octubre") \
                         .replace("November", "Noviembre").replace("December", "Diciembre") \
                         .replace("Mon", "Lun").replace("Tue", "Mar") \
                         .replace("Wed", "Mié").replace("Thu", "Jue") \
                         .replace("Fri", "Vie").replace("Sat", "Sab") \
                         .replace("Sun", "Dom")
            else:
                # Generar calendario anual en español
                cal = calendar.calendar(año)
                cal = cal.replace("January", "Enero").replace("February", "Febrero") \
                         .replace("March", "Marzo").replace("April", "Abril") \
                         .replace("May", "Mayo").replace("June", "Junio") \
                         .replace("July", "Julio").replace("August", "Agosto") \
                         .replace("September", "Septiembre").replace("October", "Octubre") \
                         .replace("November", "Noviembre").replace("December", "Diciembre") \
                         .replace("Mon", "Lun").replace("Tue", "Mar") \
                         .replace("Wed", "Mié").replace("Thu", "Jue") \
                         .replace("Fri", "Vie").replace("Sat", "Sab") \
                         .replace("Sun", "Dom")
            
            texto_calendario.delete(1.0, tk.END)
            texto_calendario.insert(tk.END, cal)
        except ValueError:
            tk.messagebox.showerror("Error", "Por favor ingrese un año válido")
        except Exception as e:
            tk.messagebox.showerror("Error", f"Ocurrió un error: {str(e)}")

    root = tk.Tk()
    root.title("Calendario Interactivo")
    root.geometry("700x600")
    
    frame = tk.Frame(root, padx=20, pady=20)
    frame.pack(fill=tk.BOTH, expand=True)
    
    # Título
    titulo = tk.Label(frame, text="Calendario", 
                     font=("Arial", 14, "bold"), fg="#2c3e50")
    titulo.pack(pady=(0, 15))
    
    # Selector de opción
    opcion_frame = tk.Frame(frame)
    opcion_frame.pack(fill=tk.X, pady=(0, 10))
    
    tk.Label(opcion_frame, text="Mostrar:", font=("Arial", 11)).pack(side=tk.LEFT)
    
    opcion_var = tk.StringVar(value='M')
    tk.Radiobutton(opcion_frame, text="Mes", variable=opcion_var, value='M').pack(side=tk.LEFT, padx=10)
    tk.Radiobutton(opcion_frame, text="Año completo", variable=opcion_var, value='A').pack(side=tk.LEFT)
    
    # Selector de año
    año_frame = tk.Frame(frame)
    año_frame.pack(fill=tk.X, pady=(0, 10))
    
    tk.Label(año_frame, text="Año:", font=("Arial", 11)).pack(side=tk.LEFT)
    entry_año = tk.Entry(año_frame, font=("Arial", 11), width=8)
    entry_año.insert(0, "2024")
    entry_año.pack(side=tk.LEFT, padx=5)
    
    # Botón para año actual
    tk.Button(año_frame, text="Año actual", command=lambda: entry_año.delete(0, tk.END) or entry_año.insert(0, str(datetime.now().year))).pack(side=tk.LEFT, padx=10)
    
    # Selector de mes (solo para opción mes)
    mes_frame = tk.Frame(frame)
    mes_frame.pack(fill=tk.X, pady=(0, 15))
    
    tk.Label(mes_frame, text="Mes:", font=("Arial", 11)).pack(side=tk.LEFT)
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    combo_mes = ttk.Combobox(mes_frame, values=meses, state="readonly", width=15)
    combo_mes.current(datetime.now().month - 1)
    combo_mes.pack(side=tk.LEFT, padx=5)
    
    # Botón para mes actual
    tk.Button(mes_frame, text="Mes actual", command=lambda: combo_mes.current(datetime.now().month - 1)).pack(side=tk.LEFT, padx=10)
    
    # Botón de mostrar
    tk.Button(frame, text="Mostrar Calendario", command=mostrar_calendario, 
             bg="#2196F3", fg="white", font=("Arial", 11)).pack(pady=(0, 15))
    
    # Área de texto para el calendario
    texto_frame = tk.Frame(frame)
    texto_frame.pack(fill=tk.BOTH, expand=True)
    
    texto_calendario = tk.Text(texto_frame, font=("Courier New", 10), wrap=tk.WORD)
    texto_calendario.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
    
    scrollbar = tk.Scrollbar(texto_frame, command=texto_calendario.yview)
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    texto_calendario.config(yscrollcommand=scrollbar.set)
    
    # Mostrar calendario inicial
    mostrar_calendario()
    
    root.mainloop()

if __name__ == "__main__":
    from datetime import datetime
    main_gui()