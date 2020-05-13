from io import open
import pathlib


# abrir archivo
ruta = str(pathlib.Path().absolute()) + "/14.sistema-archivos/fichero_texto.txt" # absolute es la carpeta principal
archivo = open(ruta, "a+")

# Escribir 
archivo.write("Esto es un texto\n")

# Cerrar archivo

archivo.close()

# abrir archivo
ruta = str(pathlib.Path().absolute()) + "/14.sistema-archivos/fichero_texto.txt"
archivo_lectura = open(ruta, "r+")


# Leer contenido
#contenido = archivo_lectura.read()
#print(contenido)

# Leer contenido  y guardar en una lista

lista = archivo_lectura.readlines()
archivo_lectura.close()

#print(lista) # <-- comentar el "leer contenido" de arriba
for frase in lista:
    print(frase)

# Copiar archivo
import shutil

ruta_original = str(pathlib.Path().absolute()) + "/14.sistema-archivos/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_copiado.txt"
ruta_alternativa = str(pathlib.Path().absolute()) + "/../fichero_copiado.txt"

shutil.copyfile(ruta_original, ruta_nueva)

# Mover archivo
"""ruta_original = str(pathlib.Path().absolute()) + "/14.sistema-archivos/fichero_texto.txt"
ruta_nueva = str(pathlib.Path().absolute()) + "/fichero_texto_movido.txt"
shutil.move(ruta_original, ruta_nueva)"""

# Eliminar archivo

"""import os
os.remove(ruta)"""

# Comprobar si existe 

import os.path
print("-->", os.path.abspath("."))

ruta_comprobar = str(pathlib.Path().absolute()) + "/fichero_texto_movido.txt"
if os.path.isfile(ruta_comprobar):
    print("el archivo existe")
else:
    print("El archivo NO existe")



