Examinar archivos
Como primer punto a trabajar en la actividad, me base en averiguar una manera en la que pudiera seleccionar un archivo desde el explorador de archivos para poder trabajarse, así que cree la función def examinar_archivo la cual use funciones para acceder al explorador de archivos utilizando fedialog para capturar por parte del usuario el archivo y leerlo seguidamente.
Una vez encargado de la función para capturar un archivo de texto, decidí crear una función para poder capturar la frecuencia de los caracteres y mostrar el árbol de Huffman, así que tenía que crear funciones específicas para la elaboración de este, pero debería primeramente  de implementar una función especifica para procesar el algoritmo de Huffman y así poder tomar como consecuente el calculo de la frecuencia de los caracteres, así que implemente la clase class NodoHuffman: la cual tuvo como propósito los nodos del árbol de huffman para posteriormente poder realizar las otras funciones del programa, como dato extra esta es una de lsa parte de la actividad de las que me llevo mas tiempo debido a ciertos errores en la implementación de los nodos.



Frecuencia de caracteres y árbol de Huffman
Una vez resuelto el algoritmo de Huffman en la clase, me decidí por optar en crear las acciones correspondientes  para poder calcular la frecuencia de los caracteres de un archivo de texto así que cree 2 fundiciones, la función def calcular_frecuencia()  y def mostrar_frecuencia la cual como sus nombres lo indican, servirían para calñcular los carcateres en el archivo de manera en la que accedía al archivo y mediante un bucle for para recorrer el archivo de texto con ayuda de la calse del algoritmo y así mismo interactuar con la otra función de  def mostrar_frecuencia para poder visualizar los datos requeridos en la interfaz.
compresión
una vez finalizadas estas opciones, decidí que era prudente implementar la opción de comprimir el archivo, así que lo elaboré de la manera siguiente
•	Atreves de una función especifica llamada def comprimir_archivo: la cual primeramente obtiene el nombre del Archivo original,
La primera línea archivo_original = texto_original_entry.get() obtiene el nombre del archivo seleccionado por el usuario desde el campo de entrada en la interfaz gráfica
•	A continuación, el programa abre el archivo original en modo lectura ('r') y lee su contenido en la variable texto_original utilizando with open(archivo_original, 'r') as file: y texto_original = file.read(). De esta manera, el programa obtiene el contenido completo del archivo original como una cadena de texto.
•	Después de leer el contenido del archivo original, se construye el árbol de Huffman utilizando la función construir_arbol(texto_original). Una vez construido el árbol, se generan los códigos Huffman correspondientes utilizando la función generar_codigos_huffman(arbol).
•	Con los códigos Huffman generados, se procede a comprimir el texto original utilizando la función comprimir_texto(texto_original, codigos). Cada carácter en el texto original se reemplaza por su código Huffman correspondiente, resultando en un texto comprimido.
•	Finalmente, el texto comprimido se guarda en un nuevo archivo de texto con el mismo nombre que el archivo original, pero con "_comprimido" agregado al nombre del archivo y extensión ".txt". El archivo comprimido se guarda en el mismo directorio que el archivo original.

Descompresión 
Una vez que termine esta función, implemente finalmente la opción de descomprimir un archivo que ya haya sido comprimido con el mismo programa, entonces implemente la función def descomprimir_archivo(): 
•	Primeramente, abrimos un cuadro de diálogo para que el usuario seleccione un archivo comprimido de texto. El diálogo solo muestra archivos con la extensión ".txt" y se limita a archivos de texto comprimidos.
•	Utilizando el texto comprimido, se reconstruye el árbol de Huffman. Aunque normalmente el árbol de Huffman se reconstruye a partir de los datos del archivo comprimido, en este caso, por simplicidad, se utiliza el texto comprimido directamente para construir el árbol. Esto se hace con la línea arbol = construir_arbol(texto_comprimido).
•	Una vez que se reconstruye el árbol de Huffman, se utiliza para descomprimir el texto comprimido. Esto se realiza con la función descomprimir_texto(texto_comprimido, arbol), que recorre el árbol de Huffman para reconstruir el texto original a partir del texto comprimido.
•	Después de descomprimir el texto, se guarda el texto descomprimido en un nuevo archivo. El nombre del archivo descomprimido se forma eliminando la extensión del archivo comprimido y añadiendo "_descomprimido.txt".

