numeros = [4, 7, 9, 1, 6, 9, 10, 46]

# Mostrar lista
for num in numeros:
    print(num)

def recorrer_lista(listas_parametro):
    numeros = ""
    for num in listas_parametro:
        numeros = numeros + f" {num}"

    return numeros

print(recorrer_lista(numeros))

# Ordenar lista
numeros.sort()
print(numeros)

# Mostrar longitud
print(f"La lista tiene {len(numeros)} numeros")

# Busqueda en la lista

elemento = int(input("Escribe el elemento que quieres buscar"))
    # Comprobación de que el valor introducido sea int
comprobacion = isinstance(elemento, int)

while not comprobacion or elemento <= 0: # No se puede saber la longitud de un valor numerico
    elemento = int(input("Escribe el elemento que quieres buscar"))
    print(comprobacion)
else:
    print(f"Has introducido el {elemento}")

print(f"El numero {elemento} esta en {numeros.index(elemento)} posicion")

