import mimodulo
#from mimodulo import getTipo
#from mimodulo import *


var = 23
#mimodulo.getTipo(var)

mimodulo.getTipo(var)

# Modulo fechas

import datetime

print(datetime.date.today())

fecha_completa = datetime.datetime.now()

print(fecha_completa)
print(fecha_completa.year)
print(fecha_completa.month)
print(fecha_completa.day)

fecha_personalizada = fecha_completa.strftime("%d/%m/%Y")
print(fecha_personalizada)

# Modulo de Matemáticas
import math

print("redondear al baja:", math.floor(9.246464))
print("redondear a la alta:", math.ceil(8.61132))

print("raiz cuadrada de  10", math.sqrt(10))
print("Numero pi", math.pi)

# Modulo Python
import random

print("numero aleatorio entre 30 y 56:", random.randint(30, 56))
