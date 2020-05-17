# Clase coche

class Coche:
    color = "Rojo"
    marca = "Ferrari"
    modelo = "F40"
    velocidad = 250
    caballaje = 400
    plazas = 3

    # Métodos, son acciones que hace el objeto (coche)
    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def get_velocidad(self):
        return self.velocidad
# Fin de la clase

# Crar objetos /Instanciar clase
coche = Coche() # Crear objeto de la clase Coche
print("Coche Nuevo--------------------------")
print(coche.marca, coche.modelo, coche.color)
print("Velocidad actual: ", coche.velocidad)

coche.setColor("Verde")
coche.setModelo("Testarossa")

print(f"{coche.marca} {coche.getModelo()} {coche.getColor()}")

coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()
coche.acelerar()

print("Nueva velocidad: ", coche.get_velocidad())

print("Coche Nuevo 2 ---------------------")
coche2 = Coche()
coche2.setModelo("Italia")
coche2.setColor("Amarillo")
print(coche2.marca)
print(coche2.getModelo(), coche2.getColor())