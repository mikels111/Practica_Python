from tkinter import *

ventana = Tk()
ventana.geometry("400x500")

# Encabezados
encabezado = Label(ventana, text = "Formularios 2")

encabezado.config(
    padx=15,
    pady=15,
    fg="white",
    bg="green",
    font=("Consolas", 20)
)

#encabezado.pack(anchor=N,side=TOP,fill=X, expand=YES)
encabezado.grid(row=0, column=0, columnspan=5)

# Botones check
def mostrarProfesion():
    texto = ""
    if web.get():
        texto += "Desarrollo Web "
    if app.get():
        if not web.get():
            texto = "Desarrolo de aplicaciones"
        else:
            texto += "y Desarrolo de aplicaciones"

    mostrar.config(text=texto)

web = IntVar()
app = IntVar()

Label(ventana, text = "¿ A que te dedicas ?").grid(row=1, column=0)
Checkbutton(ventana, text="Desarrollo Web", variable=web, onvalue=1, offvalue=0, command=mostrarProfesion).grid(row=2, column=0, sticky=W)
Checkbutton(ventana, text="Desarrollo de Aplicaciones", variable=app, onvalue=1, offvalue=0, command=mostrarProfesion).grid(row=3, column=0, sticky=W)

mostrar = Label(ventana)
mostrar.grid(row=4, column=0, sticky=W)

# Radio buttons
def marcar():
    marcado.config(text=opcion.get())

opcion = StringVar()
opcion.set(None)

Radiobutton(ventana, text = "Femenino", value= "Femenino", variable = opcion, command=marcar).grid(row=5, column=0, sticky=W)
Radiobutton(ventana, text = "Masculino", value= "Masculino",  variable = opcion, command=marcar).grid(row=6, column=0, sticky=W)

marcado = Label(ventana)
marcado.grid(row=7, sticky=W) 

# Option menu
opcion = StringVar()
opcion.set("opcion ")
Label(ventana, text = "Selecciona una opcion").grid(row=5, column=1)

select = OptionMenu(ventana, opcion, "Opcion 1", "Opcion 2", "Opcion 3", "Opcion 4")
select.grid(row=6, column=1)

ventana.mainloop()