# bucle for con variable iterativa range

contador = 0
suma = 0

for contador in range(1, 9):
    print("voy por el número "+str(contador))
    suma += contador
    if contador == 4:
        break #<--- en el contador 4 termina la iteración sin llegar al final del range    
else:
    print("se han terminado lo números")

print(f"suma de los números {suma}")

