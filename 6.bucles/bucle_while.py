# bucle while
contador = 1
muestra = str(0)

while contador <= 10:
    print(contador)
    muestra = muestra + ", " + str(contador) # <--al string original le añade otro string con una coma y un contador, ya así salen los numeros separados por coma
    contador += 1
print(muestra)