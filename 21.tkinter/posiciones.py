from tkinter import *

ventana = Tk()
ventana.geometry("500x500")

texto_2 = Label(ventana, text= "antonio")# Parametros de palabras clave
texto_2.config(fg="red", bg="black", padx=3, pady=1, font=("Consolas",12), height=4,cursor="spider")
texto_2.pack(side=TOP, fill=X, expand=YES)#side=TOP,side=right
ventana.mainloop()