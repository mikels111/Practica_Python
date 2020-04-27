# operadores aritmeticos
num1 = 90
num2 = 50 # operador de asignación

resta = num1 - num2
suma = num1 + num2
multiplicacion= num1 * num2 
division = num1 / num2
resto = num1 % num2

# estos son métodos print() que se pasa un string y una variable numérica
print("suma es =" , suma)
print("resta es =" , resta)
print("multiplicacion es =" , multiplicacion)
print("division es =" , division)
print("resto es =" , resto)

# estos son un métodos print() con formato
print("la suma entre {} y {} es {}".format(num1,num2,suma))
print(f"la resta entre {num1} y {num2} es {resta}")