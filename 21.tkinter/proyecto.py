"""
Crear un programa que tenga

- Ventana -
- Tamaño fijo -
- No redimensionable -
- Un menu -
- Diferentes pantallas -
- Formulario de añadir productos
- Guardar datos temporalmente
- Mostrar datos listados en la pantalla home
- Opción de salir
"""

from tkinter import *
import os.path

# Ventana home
ventana = Tk()
ventana.geometry("300x600")
ventana.resizable(0, 0)

# Ventana de añadir productos
#ventana2 = Tk()
#ventana2.geometry("300x300")
#ventana2.resizable(0, 0)

# Titulo de la ventana
ventana.title("Proyecto Tkinter")

# Icono de la venta 
ruta_icono = os.path.abspath("./imagenes/egg.ico")
ventana.iconbitmap(ruta_icono)

# Menu
mi_menu = Menu(ventana)
ventana.config(menu=mi_menu)

nomb = StringVar()

def nombrar():
    label.config(text=nombre)

def abrirNueva():
    nuevaVent = Toplevel(ventana)# Abre una nueva ventana

nuevaVent = Tk()   
nuevaVent.geometry("300x400")
Label(nuevaVent, text="Introduce el nuevo producto").grid(row=0, column=0, padx=0, pady=0, sticky=W)
   
Label(nuevaVent, text="nombre").grid(row=1, column=0, padx=0, pady=0, sticky=W)
nombre = Entry(nuevaVent)
nombre.grid(row=2, column=0, padx=0, pady=0, sticky=W)
    
Label(nuevaVent, text="Codigo de producto").grid(row=1, column=1)
cod = Entry(nuevaVent)
cod.grid(row=2, column=1)
    
Label(nuevaVent, text="Precio del producto").grid(row=3, column=0, padx=0, pady=0, sticky=W)
precio = Entry(nuevaVent)
precio.grid(row=4, column=0, padx=0, pady=0, sticky=W)
    
boton = Button(nuevaVent, text="Guardar", command=nombrar)
boton.grid(row=6, column=0, padx=0, pady=0, sticky=W)
    
label = Label(nuevaVent,text="asdf").grid(row=7, column=0, padx=0, pady=0, sticky=W)    
nombreProducto = Label(ventana).grid(row=1, column=1)


mi_menu.add_command(label="Añadir productos", command=abrirNueva)
mi_menu.add_command(label="Mostrar productos")

ventana.mainloop()



