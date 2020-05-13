
def mostrar_nombre():# Creacion de la función
    print("mikel")

mostrar_nombre()# Llamada a la función

# Misma función con parámetro

def mostrar_nombre_edad(nombre,edad):
    print("Tu nombre es: "+nombre)

    if edad >= 18:
        print("Tu edad es " + str(edad) + " y eres mayor de edad")
    else:
        print("Tu edad es " + str(edad) + "y NO eres mayor de edad")

nom = input("Escribe tu nombre: ")
edad = int(input("Escribe tu edad: "))

mostrar_nombre_edad(nom, edad)

# tablas de multiplicar con una funcion

def tablas_de_multiplicar(num):
    for tabla in range(1, 11):
        print(f"{num} x {tabla} = {tabla * num}")
    print("////")

for tabla in range(1, 11):
    tablas_de_multiplicar(tabla)

# Parámetros opcionales

def getEmpleado(nombre, dni = None):# <-- El dni puedes ponerlo "none" o "false"
    print(f"Nombre del empleado: {nombre}")
    if dni != None:
        print(f"DNI del empleado: {dni}")
        
nombre = input("Tu nombre: ")
dni = input("tu dni: ")
getEmpleado(nombre, dni)

# Return en funciones
def get_suma(num1, num2):
    suma = num1 + num2
    return suma

print(get_suma(4 , 9))

# Una función dentro de otra
def dime_nombre(nom):
    nombre = f"El nombre es: {nom}"
    return nombre

def dime_edad(anos):
    edad = f"La edad es: {anos}"
    return edad

def dimelo_todo(nomb, edad):
    print(f"{dime_nombre(nomb)} {dime_edad(edad)}")
    
dimelo_todo("mikel",20)

# Función lambda

get_ano = lambda ano : f"El año en el que estamos es {ano}"

print(get_ano(2020))