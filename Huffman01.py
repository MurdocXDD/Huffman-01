from tkinter import *
from tkinter import ttk
def contar(nombre_archivo,archivo_salida):
    try:
        with open(nombre_archivo, "r", encoding="utf-8") as archivo:
            contenido = archivo.read()
            contador = {}

            for caracter in contenido:
                if caracter in contador:
                    contador[caracter] +=1
                else:
                    contador [caracter] +=1
            caracteres_order = sorted(contador.items(),key=lambda x:x[1],reverse = True)
            
        with open(archivo_salida,"w")as archivo_salida:
            for caracter,frecuencia in caracteres_order: 
                archivo_salida.write(f"{caracter}:{frecuencia} \n")
            return "Resulados guardados"
    except FileNotFoundError:
        return "Error del archivo"
    
    
def seleccionar_archivo():
    pass

def comprmir_archivo():
    pass

def descomprimir_arcivo():
    pass
    
 
 #INTERFAZ
archivo = "Gullivers_Travels.txt"
salida = "Resultados.txt"
resultado = contar(archivo,salida)
print(resultado)

root = Tk()
root.geometry("600x300")

ventana = Tk()
ventana.geometry("300x300")
ttk.Label(ventana,text="Otra Ventana profe").grid(column=8,row=8)


ttk.Label(root,text="Algoritmo de Huffman").grid(column=0,row=0)
ttk.Button(root, text = "Seleccionar archivo",command=seleccionar_archivo).grid()
ttk.Button(root, text = "Comprimir Archivo").grid()
ttk.Button(root, text = "Descomprimir Archivo").grid()
ttk.Button(text="Quitar", command=root.destroy).grid()
root.mainloop()
