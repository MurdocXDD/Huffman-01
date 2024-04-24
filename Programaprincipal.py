import tkinter as tk
from tkinter import filedialog, messagebox
import heapq
import os

# Funcion para calcular la frecuencia de cada carácter en el archivo
def calcular_frecuencia(texto):
    frecuencia = {}
    for caracter in texto:
        if caracter in frecuencia:
            frecuencia[caracter] += 1
        else:
            frecuencia[caracter] = 1
    return frecuencia

# Clase para representar un nodo en el árbol de Huffman
class NodoHuffman:
    def __init__(self, caracter, frecuencia):
        self.caracter = caracter
        self.frecuencia = frecuencia
        self.izquierda = None
        self.derecha = None

    # Comparador para heapq
    def __lt__(self, otro):
        return self.frecuencia < otro.frecuencia

# Función para construir el arbol de Huffman
def construir_arbol(texto):
    frecuencia = calcular_frecuencia(texto)
    cola_prioridad = [NodoHuffman(caracter, frecuencia) for caracter, frecuencia in frecuencia.items()]
    heapq.heapify(cola_prioridad)

    while len(cola_prioridad) > 1:
        nodo_izquierda = heapq.heappop(cola_prioridad)
        nodo_derecha = heapq.heappop(cola_prioridad)
        nuevo_nodo = NodoHuffman(None, nodo_izquierda.frecuencia + nodo_derecha.frecuencia)
        nuevo_nodo.izquierda = nodo_izquierda
        nuevo_nodo.derecha = nodo_derecha
        heapq.heappush(cola_prioridad, nuevo_nodo)

    return cola_prioridad[0]

# Funcion para generar los codigos Huffman recursivamente
def generar_codigos_huffman(arbol, prefijo='', codigos={}):
    if arbol.caracter is not None:
        codigos[arbol.caracter] = prefijo
    else:
        generar_codigos_huffman(arbol.izquierda, prefijo + '0', codigos)
        generar_codigos_huffman(arbol.derecha, prefijo + '1', codigos)
    return codigos

# Funcion para comprimir el texto utilizando los códigos Huffman generados
def comprimir_texto(texto, codigos):
    texto_comprimido = ''.join(codigos[caracter] for caracter in texto)
    return texto_comprimido

# Funcion para descomprimir el texto utilizando los códigos Huffman generados
def descomprimir_texto(texto_comprimido, arbol):
    texto_descomprimido = ""
    nodo_actual = arbol
    for bit in texto_comprimido:
        if bit == '0':
            nodo_actual = nodo_actual.izquierda
        else:
            nodo_actual = nodo_actual.derecha
        if nodo_actual.caracter is not None:
            texto_descomprimido += nodo_actual.caracter
            nodo_actual = arbol
    return texto_descomprimido

# Funcion para abrir el explorador de archivos y seleccionar un archivo
def examinar_archivo():
    archivo = filedialog.askopenfilename(filetypes=[("Archivos de texto", "*.txt")])
    if archivo:
        with open(archivo, 'r') as file:
            texto_original = file.read()
        texto_original_entry.delete(0, tk.END)
        texto_original_entry.insert(0, archivo)
        return texto_original

# Funcion para calcular la frecuencia de los caracteres y mostrarlos en una lista
def mostrar_frecuencia():
    archivo = texto_original_entry.get()
    if archivo:
        with open(archivo, 'r') as file:
            texto_original = file.read()
        
        frecuencia = calcular_frecuencia(texto_original)
        arbol = construir_arbol(texto_original)
        
        frecuencia_window = tk.Toplevel()
        frecuencia_window.title("Frecuencia de Caracteres y Árbol de Huffman")
        
        tk.Label(frecuencia_window, text="Frecuencia de Caracteres:").pack()
        for caracter, freq in frecuencia.items():
            tk.Label(frecuencia_window, text=f"'{caracter}': {freq}").pack()
        
        tk.Label(frecuencia_window, text="Árbol de Huffman:").pack()
        mostrar_arbol_huffman(frecuencia_window, arbol)
 
# Funcion auxiliar para mostrar el árbol de Huffman en texto plano
def mostrar_arbol_huffman(window, arbol, nivel=0):
    if arbol.caracter is not None:
        tk.Label(window, text=f"{'  ' * nivel} '{arbol.caracter}' - Frecuencia: {arbol.frecuencia}").pack()
    else:
        tk.Label(window, text=f"{'  ' * nivel} Nodo interno - Frecuencia: {arbol.frecuencia}").pack()
        mostrar_arbol_huffman(window, arbol.izquierda, nivel + 1)
        mostrar_arbol_huffman(window, arbol.derecha, nivel + 1)

# Funcion para comprimir el archivo y guardar el resultado
def comprimir_archivo():
    archivo_original = texto_original_entry.get()
    if archivo_original:
        with open(archivo_original, 'r') as file:
            texto_original = file.read()
        
        arbol = construir_arbol(texto_original)
        codigos = generar_codigos_huffman(arbol)
        texto_comprimido = comprimir_texto(texto_original, codigos)
        
        ruta, extension = os.path.splitext(archivo_original)
        archivo_comprimido = ruta + "_comprimido.txt"
        
        with open(archivo_comprimido, 'w') as file:
            file.write(texto_comprimido)
        messagebox.showinfo("Comprimir", "Archivo comprimido guardado como {}".format(archivo_comprimido))

# Funcion para descomprimir el archivo y guardar el resultado
def descomprimir_archivo():
    archivo_comprimido = filedialog.askopenfilename(filetypes=[("Archivos de texto comprimidos", "*.txt")])
    if archivo_comprimido:
        with open(archivo_comprimido, 'r') as file:
            texto_comprimido = file.read()

        arbol = construir_arbol(texto_comprimido)  # Se utiliza el texto comprimido para construir el árbol
        texto_descomprimido = descomprimir_texto(texto_comprimido, arbol)

        ruta, _ = os.path.splitext(archivo_comprimido)
        archivo_descomprimido = ruta + "_descomprimido.txt"

        with open(archivo_descomprimido, 'w') as file:
            file.write(texto_descomprimido)
        messagebox.showinfo("Descomprimir", "Archivo descomprimido guardado como {}".format(archivo_descomprimido))

# Creacio de la interfaz grafica
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
