"""
Diccionario: 
Un tipo de dato que almacena un conjunto de datos en formato clave valor

"""
persona = {
    "nombre" : "Mikel",
    "apellido" : "Seara",
    "edad" : 20,
    "num" : 68868845,
    1 : "hola"
    }

print(str(persona[1]) + " " + persona["nombre"] + " Tienes " + str(persona["edad"]) + " años")

# Diccionarios dentro de listas 
contactos = [   # Contactos es una Lista
    { # Primer diccionario
        "nombre" : "Mikel",
        "apellido" : "Seara"
    },
    {
        "nombre" : "Antonio",
        "apellido" : "Palotes"
    }
]

print(contactos)
contactos[1]["nombre"] = "Antoñito"
print(contactos[1]["nombre"])

for contacto in contactos:
    print( "---" + contacto["nombre"] + " " + contacto["apellido"])
