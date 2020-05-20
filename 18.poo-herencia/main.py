import clases

persona1 = clases.Persona()

persona1.set_nombre("Mikel")
persona1.set_apellido("Seara")
persona1.set_altura("180cm")
persona1.set_edad("50")

print(f"la persona es {persona1.get_nombre()}")
print(persona1.hablar())

# Informatico

informatico = clases.Informatico()
informatico.set_nombre("mikel")
informatico.set_edad(19)
print("El informatico és " + informatico.get_nombre() + " y tiene "
+ str(informatico.get_edad()))

print(informatico.get_lenguajes())
print(informatico.caminar())
print(informatico.get_experiencia())

# Clase tecnico de redes que hereda de Informatico

tecnico = clases.TecnicoRedes()
tecnico.set_nombre("Antonio")
print(tecnico.get_nombre(), tecnico.get_lenguajes())# Para poder llamar al
#metodo get_lenguajes(), en la clase TecnicoRedes hay que invocar al
#constructor de la clase padre (Informatico)


