import tkinter as tk
from tkinter import filedialog, messagebox
import heapq
import os

# Creacio de la interfaz grafica

def examinar_archivo():
    pass

def mostrar_frecuencia():
    pass

def comprimir_archivo():
    pass

def descomprimir_archivo():
    pass

app = tk.Tk()
app.title("Compresor de Archivos de Texto")

texto_original_label = tk.Label(app, text="Archivo de Texto:")
texto_original_label.grid(row=0, column=0, padx=5, pady=5, sticky=tk.W)

texto_original_entry = tk.Entry(app, width=50)
texto_original_entry.grid(row=0, column=1, padx=5, pady=5)

examinar_button = tk.Button(app, text="Examinar", command=examinar_archivo)
examinar_button.grid(row=0, column=2, padx=5, pady=5)

mostrar_frecuencia_button = tk.Button(app, text="Mostrar Frecuencia", command=mostrar_frecuencia)
mostrar_frecuencia_button.grid(row=1, column=1, padx=5, pady=5)

comprimir_button = tk.Button(app, text="Comprimir", command=comprimir_archivo)
comprimir_button.grid(row=2, column=1, padx=5, pady=5)

descomprimir_button = tk.Button(app, text="Descomprimir", command=descomprimir_archivo)
descomprimir_button.grid(row=3, column=1, padx=5, pady=5)

app.mainloop()