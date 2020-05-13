import os
import shutil
# Crear carpeta
if not os.path.isdir("./mi_carpeta"):
    os.mkdir("./mi_carpeta")
    print("Carpeta creada")
else: 
    print("La carpeta ya existe")

# Eliminar carpeta
#os.rmdir("./mi_carpeta")

# Copiar carpeta
ruta_original = "./mi_carpeta"
ruta_nueva = "./mi_carpeta_copiada"

if not os.path.isdir("./mi_carpeta_copiada"):
    shutil.copytree(ruta_original,ruta_nueva)
else:
    print("La carpeta ya existe")

# listar el contenido del directorio
contenido = os.listdir(".")
for elemento in contenido:
    print(elemento)