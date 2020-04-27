# Imprimir los cuadrados de los primeros 60 números

for contador in range(1, 61):
    print(f"{contador} x {contador} ="+str(contador * contador))

contador = 1
while contador <= 60:
    print(f"{contador} x {contador} = {contador * contador}")
    contador += 1
