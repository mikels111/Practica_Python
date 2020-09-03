from tkinter import *

ventana = Tk()
ventana.title("Marcos")
ventana.geometry("700x400")

marco = Frame(ventana, width=300, height=100)
marco.config(bg="red",bd=12, relief=RIDGE)
marco.pack(side=BOTTOM, anchor=NW)
marco.pack_propagate(False)# para que el marco no se contraiga
texto = Label(marco, text="Marco rojo")
texto.config(bg="red",fg="white",height=5)
texto.pack(anchor=NE)


ventana.mainloop()
