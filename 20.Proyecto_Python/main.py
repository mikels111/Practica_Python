"""
Proyecto Python:
    -abrir asistente
    -login o registro
    -si elegimos registrno, creará un usuario en la bbdd
    -si elegimos login, identifica al usuario y nos preguntará
    -crear nota, mostrar nota, borrarlas

"""
# Import del modulo acciones.py desde el paquete_usuarios
from paquete_usuarios import acciones 

print("""
Acciones disponibles:
    -registro
    -entrar
""")

# Objeto Acciones del modulo acciones.py
objectAcciones = acciones.Acciones()

accion = input("¿Que quieres hacer?: ")

if accion == "registro" :
    objectAcciones.registro() # Llamada al método registro del objeto "accion"

elif accion == "entrar":
    objectAcciones.entrar()
