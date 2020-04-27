# entrada
nombre = input("dime tu numbre: ")
edad = input("dime tu edad: ") # <--todo dentro del método input es un string aunque introduzca un número

# salida
print(f"tu nombre es : {nombre}")
print(f"y tu edad es {edad}")
# print(f" dentro de 5 años tendrás : {int + 5} años") <-- da error
print(f" dentro de 5 años tendrás : {int(edad) + 5} años")