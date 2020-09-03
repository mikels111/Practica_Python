from tkinter import *
from tkinter import messagebox as MessageBox
ventana =  Tk()
ventana.geometry("500x600")

def sacarAlerta():
    MessageBox.showerror("Alerta", "Hola soy Mikel Seara")

def salir(nombre):
   resultado = MessageBox.askquestion("Salir", "Quieres continuar con la aplicacion")
   if resultado != "yes":
       MessageBox.showinfo("Alerta", f"Hasta otra {nombre}")
       ventana.destroy()

Button(ventana, text="Alerta", command=sacarAlerta).pack()
Button(ventana, text="Salir", command=lambda:salir("mikel")).pack()
ventana.mainloop()
