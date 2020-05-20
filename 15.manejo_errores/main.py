# Capturar excepciones y manejar errores en código susceptible a fallos
try:
    nombre = input("¿Cual es tu nombre?")

    if len(nombre) > 1:
        nombre_usuaario = "El nombre es" + nombre

    print(nombre_usuaario)
except:
    print("Ha ocurrido un error")
else:
    print("Todo ha funcionado correctamente")
finally:
    print("Fin del Try")

# Ejercicio 1 de la carpeta ejercicios 2 con manejo de excepcion
numeros = [4, 7, 9, 1, 6, 9, 10, 46]

comprobacion = False
elemento = None
while not comprobacion:
    try:
        elemento = int(input("Escribe el elemento que quieres buscar "))
        comprobacion = True
    except Exception as e:
        print(type(e).__name__)
else:
    print(f"Has introducido el {elemento}")

try:
    print(f"El numero {elemento} esta en la posicion {numeros.index(elemento)}")
except:
    print("El elemento no está")

# Multiples excepciones
numeros = [4, 7, 9, 1, 6, 9, 10, 46]

comprobacion = False
elemento = None
while not comprobacion:
    try:
        elemento = int(input("Escribe el elemento que quieres buscar "))
        comprobacion = True
    except TypeError:
        print("La variable Elemento no es un int")
    except ValueError:
        print("El valor introducido no es un número")
else:
    print(f"Has introducido el {elemento}")

try:
    print(f"El numero {elemento} esta en la posicion {numeros.index(elemento)}")
except:
    print("El elemento no está")

# Excepción personalizadas o lanzar excepción

nombre = str(input("introduce el nombre "))
edad = int(input("introuduce la edad "))

if edad < 5 or edad > 110:
    raise ValueError("la edad no es real")
elif len(nombre) < 1:
    raise ValueError("El nombre no está completo")
else:
    print("Bienvenido :" + nombre)


