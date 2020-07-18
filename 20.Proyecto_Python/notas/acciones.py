import notas.nota as modelo_nota

class Acciones:

    def crear(self, usuario):

        print("Creación de notas")
        titulo = input("Introduce el titulo de la nota| ")
        descripcion = input("introduce el contenido de la nota| ")

        nota = modelo_nota.Nota(usuario[0], titulo, descripcion)
        guardar = nota.guardar()

        if guardar[0] >= 1:
            print(f"Has guardado una nota, titulo: {nota.titulo}")
        else:
            print("no se ha guardado la nota")

    def mostrar(self, usuario):
        print("Estas son tus notas: ")

        nota = modelo_nota.Nota(usuario[0])
        notas = nota.listar()

        for nota in notas:
            print("#############################")
            print(f"Titulo de la nota: {nota[2]}")
            print(f"Contenido de la nota: {nota[3]}")

    def eliminar(self, usuario):
        titulo = input("Introduce el titulo de la nota que quieres eliminar")
        nota = modelo_nota.Nota(usuario[0], titulo)
        eliminar = nota.eliminar()

        if eliminar[0] >= 1:
            print(f"La nota {nota.titulo} ha sido eliminada")
        else:
            print(f"La nota {nota.titulo} no ha sido eliminada")