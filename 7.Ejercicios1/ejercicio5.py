# imprimir todos numeros que se encuentren en el transito de dos números dados por los números
num1 = int(input("Escribe un numero para dividirlo con otro numero: "))
num2 = int(input("Escribe un número más bajo que el anterior: "))

contador2 = 0
if num1 < num2:
    for contador in range(num1, num2):
        print(contador)
        print(contador2)
else:
    print("El número uno tiene que ser mas grande que el segundo")
    