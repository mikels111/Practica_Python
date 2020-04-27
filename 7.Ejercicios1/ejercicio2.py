# Mostrar por pantalla todos los números pares del 1 al 120 

contador = 1

while contador <= 120:
    if contador % 2 == 0:
        print(contador)

    contador += 1

# otra manera

for contador1 in range(1,121):
    if contador1 % 2 == 0:
        print(contador1)