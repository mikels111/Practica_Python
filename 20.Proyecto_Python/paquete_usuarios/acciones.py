import paquete_usuarios.usuario as modelo_usuario
import notas.acciones
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

        #try:
        email = input("Introduce tu email| ")
        password = input("Introduce una constraseña| ")

        usuario = modelo_usuario.Usuario("", "", email, password)
                
        login = usuario.identificar()

        if email == login[3]:
            print(f"Bienvenido {login[1]} fecha de registro: {login[5]}")
            self.proximas_acciones(login)
        #except Exception as e:
            #print(type(e).__name__)
        print("No ha sido posible entrar")

    def proximas_acciones(self, usuario):
        
        print("""
        Acciones disponibles:
        -Crear nota (crear)
        -Mostrar nota (mostrar)
        -Eliminar nota (elimar)
        -Salir (salir)
        """)

        accion = input("Introduce un comando para la siguiente acción| ")
        accion_nota = notas.acciones.Acciones()

        if accion == "crear":
            accion_nota.crear(usuario)
            self.proximas_acciones(usuario)

        elif accion == "mostrar":
            accion_nota.mostrar(usuario)
            self.proximas_acciones(usuario)

        elif accion == "eliminar":
            print("Eliminar")
            self.proximas_acciones(usuario)

        elif accion == "salir":
            print("Hasta pronto")
            exit()
