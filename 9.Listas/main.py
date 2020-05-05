"""
Listas (Arrays)

"""
# Definir listas
peliculas = ["E.T El Extraterrestre", "Lawrence De Arabia", "Uno De Los Nuestros"]
series = list(["Mad Men", "Los Soprano", "Juego De Tronos"])
variada = [2007, "Mad Men", 2011, "Juego De Tronos", True]

lista_peliculas = (list(peliculas))

year = list(range(2007, 2012))

print(peliculas)
print(series)
print(lista_peliculas)
print(variada)
print(year)

# Indices

peliculas[1] = "La Gran Belleza"
peliculas[2] = "Toro Salvaje"
print(peliculas)

print(series[0])
print(series[-2]) # El último de la lista sería el -1
print(series[0:2]) # Imprme desde el índice 0 hasta la 2
print(series[1:]) # Imprime a partir del indice 1

# Añadir elementos a una lista 

peliculas.append("Mulholland Drive")
peliculas.append("Serpico")
series.append("Los Simpsons")

print(peliculas)
print(series)

# Recorrer Lista

for peli in peliculas:
    print(f"{peliculas.index(peli) + 1}.- {peli}")

    # Añadir peliculas iterando
while peli != "":
    peli = input("Introduce una nueva película: ")
    if peli != "":
        peliculas.append(peli)

print(peliculas)

# Listas Multidimensionales

agenda = [["mikel", "mikel@gmail.com"],["antonio", "antonio@gmail.com"]]
print(agenda[0][1])

for contacto in agenda:
    for elemento in contacto:
        if contacto.index(elemento) == 0:
            print(elemento)


print(agenda[0][1])

