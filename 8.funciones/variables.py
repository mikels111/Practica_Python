# variables locales: son sólo accesibles desde las funciones
# Variables globales: son accesibles desde todo el código

def dime_ano():
    global anio # <-- Hace que la variable anio sea global
    anio = 2020
    print(f"Estamos en el año {anio}// --> dentro de la función")

dime_ano()
print(f"{anio} // --> fuera de la función")

