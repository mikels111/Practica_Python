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

    def mostrar(self, usuario)
        print("Estas son tus notas: ")

        nota = modelo_nota.Nota(usuario_id)
        notas = nota.listar()
        print(notas)