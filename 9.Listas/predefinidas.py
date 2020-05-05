# Funciones y métodos para las listas
numeros = [4, 8, 6, 9, 1, 3]
peliculas = ["Uno De Los Nuestros", "Toro Salvaje", "Star Wars"]

# ordenar lista
print(numeros)
numeros.sort()
print(numeros) 

# añadir elementos
print(peliculas)
peliculas.append("Los Siete Samurais")
peliculas.insert(2, "Taxi Driver") # 2 es el índice donde quiero la película
print(peliculas)

#Eliminar elementos

peliculas.pop(3)
peliculas.remove("Los Siete Samurais")
print(peliculas)

# Dar la vuelta (orden inverso)

peliculas.reverse()
print(peliculas)

# Buscar elementos en una lista

print("Toro Salvaje" in peliculas) # Es sensible a mayusculas

# contar elentos

print(len(peliculas))

# Cuantas veces aparece un elemento en una lista

print(peliculas.count("Taxi Driver"))

# conseguir índice

print(peliculas.index("Uno De Los Nuestros"))

# Unir listas

peliculas.extend(numeros)
print(peliculas)