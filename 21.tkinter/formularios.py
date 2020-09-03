from tkinter import *

ventana = Tk()
ventana.geometry("400x500")
ventana.title("Formularios en Tkinter")
# Texto encabezado
encabezado = Label(ventana, text="formularios con tkinter")
encabezado.config(
    fg="white",
    bg="darkgrey",
    font=("open sans",18),
    padx=10
)
encabezado.grid(row=0, column=0, columnspan= 2, sticky=W)# sticky es para que se pegue lo maximo a la direccion indicada

# campo de texto para nombre
campo_texto = Entry(ventana)
campo_texto.grid(row=1, column=2, padx=5, pady=5, sticky=W)

# Label para el campo
label = Label(ventana, text="Nombre")
label.grid(row=1, column=0, sticky=W)

# Campo de texto para el apellido
campo_apellido = Entry(ventana)
campo_apellido.grid(row=2, column=1, padx=5, pady=5, sticky=W)
campo_apellido.config(justify="right",state="disabled")# state para deshabilitar

# Label para el apellido
label = Label(ventana, text="Apellido")
label.grid(row=2, column=0, sticky=W)

# Label para el texto grande
label = Label(ventana, text="Descripcion")
label.grid(row=3, column=0, sticky=W)

# Campo de texto grande
campo_grande = Text(ventana)
campo_grande.grid(row=3, column=1, padx=5, pady=5, sticky=W)
campo_grande.config(width=30, height=5)

# Boton
boton = Button(ventana, text="Enviar", height=7)
boton.grid(row=4, column=1, sticky=W, pady=20, padx=5)
boton.config(bg="green")



ventana.mainloop()
print("hola mundo")

