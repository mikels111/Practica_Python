from tkinter import *

ventana = Tk()
ventana.geometry("700x500")
Label(ventana, text="Mete un texto").pack(side=LEFT, anchor=NW)

def getResult():
    resultado.set(dato.get())
    if len(resultado.get()) >= 1:
        texto_recogido.config(
            bg="green",
            fg="white"
        )
        
dato = StringVar()

resultado = StringVar()

Entry(ventana, textvariable=dato).pack(anchor=NW)
texto_recogido = Label(ventana, textvariable=resultado)
texto_recogido.pack(anchor=NW)
boton = Button(ventana, text="Enviar", command=getResult).pack(anchor=NW)

ventana.mainloop()
