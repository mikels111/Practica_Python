# Clase coche

class Coche:
    color = "Rojo"
    marca = "Ferrari"
    modelo = "F40"
    velocidad = 250
    caballaje = 400
    plazas = 3

    # Métodos, son acciones que hace el objeto (coche)

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def get_velocidad(self):
        return self.velocidad
# Fin de la clase

# Crar objetos /Instanciar clase
coche = Coche()
print("Coche Nuevo--------------------------")
print(coche.marca, coche.modelo, coche.color)
print("Velocidad actual: ", coche.velocidad)

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

print("Nueva velocidad: ", coche.get_velocidad())