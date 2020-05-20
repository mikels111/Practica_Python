"""
Herencia: la posibilidad de compartir atributos y métodos
entre clases, y que diferenctes clases hereden de otras

"""
class Persona:

    def get_nombre(self):
        return self.nombre

    def get_apellidos(self):
        return self.apellidos

    def get_altura(self):
        return self.altura

    def get_edad(self):
        return self.edad

    def set_nombre(self, nom):
        self.nombre = nom

    def set_apellido(self, ape):
        self.apellido = ape

    def set_altura(self, alt):
        self.altura = alt

    def set_edad(self, edad):
        self.edad = edad

    def hablar(self):
        return "Estoy hablando"

    def caminar(self):
        return "Estoy caminando"

    def dormir(self):
        return "Estoy durmiendo"

class Informatico(Persona):

    def __init__(self):
        self.lenguajes = "HTML, CSS, JavaScript, Python"
        self.experiencia = 5

    def get_experiencia(self):
        return self.experiencia

    def get_lenguajes(self):
        return self.lenguajes

    def aprender(self, lenguajes):
        self.lenguajes =  lenguajes
        return self.lenguajes

    def programar(self):
        return "Estoy Programando"

    def reparar_pc(self):
        return "He reparado tu pc"

class TecnicoRedes(Informatico):

    def __init__(self):
        super().__init__() # Invocar el contructor de la clase padre para
        #adquirir los valores de los atributos
        self.auditar_redes = "Experto"
        self.experiencia_redes = 15

    def auditoria(self):
        return "Estoy auditando una red"
