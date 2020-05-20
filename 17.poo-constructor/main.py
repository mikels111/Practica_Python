from coche import Coche

carro = Coche("Gris", "Renault", "Clio", 130, 200, 4)
carro1 = Coche("Verde", "Seat", "Leon", 200, 400, 4)

print(carro.getColor())
print(carro.getInfo())

# Detectar tipado

carro = "hola"

if type(carro) == Coche:
    print("Es un objeto correcto")
else:
    print("No es un objeto")

print(carro1.get_privado())
