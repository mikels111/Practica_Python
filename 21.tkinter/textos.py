from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

texto = Label(ventana, text= "bienvenido a mi programa")
texto.config(fg="red", bg="black", padx=3, pady=3, font=("Consolas",12), height=4,cursor="spider")# foreground y background
texto.pack(anchor=CENTER)# Posicionar el texto

def pruebas(nombre):
    return f"hola {nombre}"

texto_2 = Label(ventana, text= pruebas(nombre="antonio"))# Parametros de palabras clave
texto_2.pack()
ventana.mainloop()