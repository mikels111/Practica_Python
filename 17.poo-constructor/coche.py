# Clase coche

class Coche:
    color = "Rojo"
    marca = "Ferrari"
    modelo = "F40"
    velocidad = 250
    caballaje = 400
    plazas = 3

    soy_publico = "Soy un atributo publico"
    __soy_privado = "Soy un atributo privado" # Dos guiones al principio para
    #definir un atributo privado


    def __init__(self, color, marca, modelo, velocidad, caballaje, plazas):
        self.color = color
        self.marca = marca
        self.modelo = modelo
        self.caballaje = caballaje
        self.plazas = plazas

    # Métodos, son acciones que hace el objeto (coche)

    def get_privado(self):
        return self.__soy_privado

    def setColor(self, color):
        self.color = color

    def getColor(self):
        return self.color

    def setModelo(self, modelo):
        self.modelo = modelo

    def getModelo(self):
        return self.modelo

    def setMarca(self, marca):
        self.marca = marca

    def getMarca(self):
        return self.marca

    def acelerar(self):
        self.velocidad += 1

    def frenar(self):
        self.velocidad -= 1

    def get_velocidad(self):
        return self.velocidad

    def getInfo(self):
        info = "------Información del Coche"
        info += "\nColor: " + self.getColor()
        info += "\nMarca: " + self.getModelo()
        info += "\nModelo: " + self.getModelo()
        info += "\nVelocidad: " + str(self.get_velocidad())

        return info

# Fin de la clase
