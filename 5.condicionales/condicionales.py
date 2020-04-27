# condicion if
"""
color = input("escribe el color: ")
color="azul"
if color == "azul":
    print("el color es azul")
else:
    print("el color no es ese")

# operadores de comparación
edad = int(input("escribe tu edad: ")) # <-- ponemos el método int() para que lo que meta el usuario sea entero y no string
continente = input("escribe tu continente")

# ejemplo 1 if y elif
if edad >= 18:
    print("eres mayor de edad")

    if continente != "europa":
        print("NO eres europeo")
    else:
        print("Eres europeo")
elif edad < 18:
    print("NO eres mayor de edad")
    
"""

# ejemplo 2 con dos condiciones
edad = int(input("escribe tu edad: "))
continente = input("escribe tu continente")

if edad >= 18 and continente == "europa":
    print("eres mayor de edad y eres europeo")

elif edad < 18:
    print("NO eres mayor de edad")