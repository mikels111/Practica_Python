# Tkinter modulo para crear interfaces graficas de usuario

from tkinter import *
import os.path

class Programa:
    def __init__(self, titulo, tamano):
        self.title = titulo
        self.ico = "./imagenes/egg.ico"
        self.ico_alt = "./21.tkinter/imagenes/egg.ico"
        self.size = tamano
        self.resizable = False

    def cargar(self):

        #Crear venta raiz
        ventana = Tk()
        self.ventana = ventana

        # Titulo de la ventana
        ventana.title(self.title)

        # comprobar si existe un archivo
        ruta_icono = os.path.abspath(self.ico)
        #esto es para que a la hora de ejecutar encuentre la imagen .ico si no estas dentro de la carpeta 21.tkinter
        if not os.path.isfile(ruta_icono):
            ruta_icono = os.path.abspath(self.ico_alt)

        # Icono de la venta 
        ventana.iconbitmap(ruta_icono)

        # mostrar texto en la ventana
        texto = Label(ventana, text = ruta_icono)
        texto.pack()

        # Cambio en el tamaño de la ventana
        ventana.geometry(self.size)

        # Bloquear el tamaño de la ventana
        if self.resizable == False:
            ventana.resizable(0, 0) # No permite redimensionar la venta
        else:
            ventana.resizable(1, 1)
        # ventana.resizable(0, 1) solo perminte redimensionar el alto de la venta
        # ventana.resizable (1, 0) solo perminte redimensionar el ancho de la venta

        # Arrancar y mostrar la ventana hasta que se cierre
        #ventana.mainloop()

    def addTexto(self):
        texto = Label(self.ventana, text="hola mundo")
        texto.pack()

    def mostrar(self):
        # Arrancar y mostrar la ventana hasta que se cierre
        self.ventana.mainloop()

# cargar programa
programa = Programa("antonio", "500x450")

programa.cargar()
programa.addTexto()
programa.mostrar()