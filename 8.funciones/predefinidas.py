# detectar tipado
nombre = "mikel"
tipo = isinstance(nombre, int) # Devuelve True o False
if tipo :
    print("Es un String")
else:
    print("No es un String")

# Limpiar de espacios un string
frase = "      me llamo antonio"
print(frase.strip())

# Eliminar varibles

ano = 2020
print(ano)
del ano

# Comprobar cuantos caracteres tiene una varible

frase = ""
if len(frase) != 0:
    print(f"la varible NO está vacía {len(frase)}")
else:
    print("la variable está vacía")

# Encontrar caracteres

pelicula = "Erase una vez en Hollywood"
print(pelicula.find("Holly"))

# Reemplazar caracteres

otra_pelicula = pelicula.replace("Hollywood", "América")
print(otra_pelicula)

# Mayusculas y minúsculas
print(otra_pelicula)
print(otra_pelicula.lower())
print(otra_pelicula.upper())