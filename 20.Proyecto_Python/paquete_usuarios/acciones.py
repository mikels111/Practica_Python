import paquete_usuarios.usuario as modelo_usuario

class Acciones:
    
    def registro(self):
        print("Has elegido registro")

        nombre = input("Introduce tu nombre: ")
        apellidos = input("Introduce tus apellidos: ")
        email = input("Introduce tu email: ")
        password = input("Introduce una constraseña: ")

        usuario = modelo_usuario.Usuario(nombre, apellidos, email, password)
        registro = usuario.registrar()

        if registro[0] >= 1:# <-- regitro [0] es el indice 0, es decir el id del usuario
            print(f"Registro realizado, nombre: {registro[1].nombre}, email: {registro[1].email}")

        else:
            print("Usuario no registrado")

    def entrar(self):
        print("Has elegido entrar")

        email = input("Introduce tu email: ")
        password = input("Introduce una constraseña: ")