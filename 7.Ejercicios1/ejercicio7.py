# mostrar todos los numeros impares que esten entre dos numeros elegidos por el usuario

num1 = int(input("Escribe un el primer número: "))
num2 = int(input("Escribe el segundo numero (tiene que ser más grande que el anterior): "))

if num1 < num2:
    for cont in range(num1, num2 + 1):
        if cont % 2 == 0:
            print(cont)
else:
    print("Has escrito el primer número más pequeño que el segundo, \no los números son iguales")